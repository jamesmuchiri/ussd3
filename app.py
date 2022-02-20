from flask import Flask, request
import africastalking
import os
import re
import maya
from maya import MayaInterval
from datetime import datetime
import datetime as dt
from dateutil.parser import parse
import mysql.connector
from menu import Menu
app = Flask(__name__)

username = "sandbox"
api_key = "0f54c06969af94baa76c50efbcc1daaecb9b75f254d3388c85edfd9d21ff7ad0"
africastalking.initialize(username, api_key)

sms = africastalking.SMS

    
@app.route('/', methods=['POST', 'GET'])

class Airtime(Menu):
    def Callback(self):
        phone_number = request.values.get("phoneNumber","default")
        text = request.values.get("text","default")
        text_array = text.split("*")
        user_response = text_array[len(text_array) - 1]
        
        

        if user_response == "":     
            return self.home()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
