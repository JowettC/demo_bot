from flask import Flask, jsonify, request
import requests

token = "6201149929:AAHPq7cdZQXPI3kD5rOKwbhrxGwqyqQszr4"


app = Flask(__name__)

def send_to_telegram(message):

    apiToken = '6201149929:AAHPq7cdZQXPI3kD5rOKwbhrxGwqyqQszr4'
    chatID = '-1001725235189'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        return { 'statusCode' : 200, 'body' : 'Success' , 'data' : data }
    else:
        send_to_telegram("Testing Notification")
        return { 'statusCode' : 200, 'body' : 'Success'}

@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        send_to_telegram(data)
        return { 'statusCode' : 200, 'body' : 'Success' , 'data' : data }
    else:
        send_to_telegram("There is something wrong on kubernetes cluster!")
        return { 'statusCode' : 200, 'body' : 'Success'}
    
if __name__ == "__main__":
    app.run(debug=True)