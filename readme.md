The goal of this section is to demonstrate how to connect [chatroom.js](https://github.com/scalableminds/chatroom) with Rasa. 

To run locally, you need to start two webservices. One for the front-end, one for the back-end. 

```bash
# This is the chatroom frontend. 
python -m http.server
# This is the Rasa backend.
rasa run --enable-api --cors="*"
# This is rasa SDK action serve 
rasa run actions
# start virtual environment
.\venv\Scripts\activate
# start fastapi backend server
python api.py
```
