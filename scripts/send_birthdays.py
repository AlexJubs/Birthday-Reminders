# This script was written by Alex Jabbour on June 20th, 2020
import os
import datetime
import requests
import boto3
import credstash

class birthday_sms:
    def __init__(self):
        self.aws_client = boto3.client("dynamodb") # using the python SDK of AWS DynamoDB
        
        # credstash fetching api tokens/client secret
        self.twilio_sid = credstash.getSecret("twilio_sid")
        self.twilio_api_token = credstash.getSecret("twilio_api_token")

    def fetch_birthdays(self):
        # query datastore to fetch birthdays for the current month
        items = self.aws_client.scan(TableName="Birthdays")["Items"]

        today = datetime.datetime.today().strftime('%d/%m') # today in MM/DD

        # birthdays are stored as "DD/MM"
        for birthday in items:
            today = datetime.datetime.today().strftime('%d/%m') # today in MM/DD

            # check if anyone's birthday is today
            if birthday["Birthday"]["S"] == today:
                message = "It is {}'s birthday today!".format(birthday["Name"]["S"])

                # send a reminder
                self.send_Message(message)
                print(message) # debugging

    # send message using twilio API - we run the bash script to do this
    def send_Message(self, body):
        payload = {
            "Body":body,
            "From":"+16464806601",
            "To":"+14164276256"
        }

        # api request to send sms
        response = requests.request("POST", url="https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(self.twilio_sid),
                auth = (self.twilio_sid, self.twilio_api_token),
                data = payload
            )

if __name__ == "__main__":
    birthday_sms().fetch_birthdays()