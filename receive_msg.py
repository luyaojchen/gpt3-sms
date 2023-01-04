from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
import wandb

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # info from sender
    text = request.form['Body']
    # get make twilio response structure
    resp = MessagingResponse()
    # get resp from gpt3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # append to message
    resp.message(response.choices[0].text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)