# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
import random
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionSendRequest(Action):
    def name(self) -> Text: 
        return "action_generate"
    
    def run(self, dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get data from the tracker (e.g., user's message)
        user_message = tracker.latest_message.get("text")

        # Define the FastAPI endpoint URL
        fastapi_url = "http://localhost:8000/chatbot"

        # Send a POST request to the FastAPI endpoint
        response = requests.post(fastapi_url, json={"input_text" : user_message})

        # If response status is OK
        if response.status_code == 200:
            response_data = response.json()
            # Process the response data
            dispatcher.utter_message(text=response_data["response"])
        else:
            dispatcher.utter_message(text="Error: Unable to generate response")

        return []


class ActionGenerateGreeting(Action):
    def name(self) -> Text: 
        return "action_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        personality_tone = {
            "friendly": ["Hi there!", "How can I help you today?", "Nice to chat with you!"],
            "professional": ["Greetings!", 'How may I assist you professionally?', "I'm here for your inquiries."],
            "humorous": ["Hey! Ready for some laughs?", "What's up, comedian?", "Let's keep it light and fun!"]
        }
       
        input_personality = tracker.get_slot("personality_type").lower()
        # removes any spaces 
        user_personality = list(input_personality.replace(" ",""))
        print(user_personality)
        if user_personality[0] == 'e':
            user_tone = "friendly"
            response = random.choice(personality_tone[user_tone])
        else:
            user_tone = "professional"
            response = random.choice(personality_tone[user_tone])
        
        print(response)
        dispatcher.utter_message(text=response)
        return [SlotSet("user_tone", user_tone)]

class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    def computer_choice(self):
        generated_num = random.randint(1,3)
        if generated_num == 1:
            computer_choice = "rock"
        elif generated_num == 2:
            computer_choice = "paper"
        elif generated_num == 3:
            computer_choice = "scissors"
        return computer_choice

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("rps")
        user_choice = tracker.get_slot("rps_choice").lower()
        dispatcher.utter_message(text=f"You chose {user_choice}")
        my_choice = self.computer_choice()
        dispatcher.utter_message(text=f"I chose {my_choice}")
        
        if user_choice == "rock" and my_choice == "scissors":
            dispatcher.utter_message(text="...")
        elif user_choice == "rock" and my_choice == "paper":
            dispatcher.utter_message(text="EASY")
        elif user_choice == "paper" and my_choice == "scissors":
            dispatcher.utter_message(text="lol")
        elif user_choice == "paper" and my_choice == "rock":
            dispatcher.utter_message(text="Again")        
        elif user_choice == "scissors" and my_choice == "rock":
            dispatcher.utter_message(text="?")    
        elif user_choice == "scissors" and my_choice == "paper":
            dispatcher.utter_message(text="You got lucky")
        else:
            dispatcher.utter_message(text="It was a tie")

        return []

# class AskForVegetarianAction(Action):
#     def name(self) -> Text:
#         return "action_ask_vegetarian"


#     def run(self, dispatcher: CollectingDsipatcher,
#             tracker:Tracker,
#             domain:Dict) -> List[EventType] :
#         dispatcher.utter_message(text="wOULD you lke>\?",
#                                  buttons = [
#                                      {"title" : "Yes", "payload" : "/affirm"}
#                                      {'title' : 'No' , "payload" : "/deny"}
#                                  ])
    
#     def validate_vegetarian(self, 
#                             slot_value:Any,
#                             dispatcher:CollectingDispatcher,
#                             tracker : Tracker, 
#                             domain : DomainDict,
#                             ) -> Dict[Text,Any]:
#         if tracker.get_intent_of_last_message() == "affirm" :
#             dispatcher.utter_message(text = "I will remember you")
#             return {"vegetarian" : True}
#         dispatcher.utter_message(text="I didnt get that ")
#         return {"vegetarian" : None}