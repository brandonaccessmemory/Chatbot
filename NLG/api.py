from fastapi import FastAPI
from pydantic import BaseModel
# from transformers import GPT2LMHeadModel, GPT2Tokenizer

# # Initialize your chatbot model and tokenizer
# model = GPT2LMHeadModel.from_pretrained("gpt2")
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
app = FastAPI()

# Define a Pydantic model representing the structure of the incoming JSON data
class InputData(BaseModel):
    input_text: str

@app.post('/chatbot')
def generate(input_data: InputData):
    print("hello")
    # Access the input_text attribute of the InputData instance
    input_text = input_data.input_text
    print(input_text)
    #     # Tokenize the input text
    # input_ids = tokenizer.encode(chat_request.input_text, return_tensors="pt")
    
    # # Generate response from the chatbot model
    # output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    # generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    # open my text file and build user dialogue data
    return {"response" : "hello"}

# Run the FastAPI app using uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)