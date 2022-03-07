# This script was written by Alex Jabbour on June 20th, 2020
import os
import datetime
import requests
import boto3
import credstash

class birthday_sms:
    def __init__(self):
        self.dynamo = boto3.client("dynamodb") # using the python SDK of AWS DynamoDB
        
        # credstash fetching api tokens/client secret
        self.twilio_sid = credstash.getSecret("twilio_sid")
        self.twilio_api_token = credstash.getSecret("twilio_api_token")

    def fetch_birthdays(self):
        today = datetime.datetime.today().strftime('%d/%m') # today in MM/DD

        # query datastore to fetch birthdays for the current date
        birthdays = self.dynamo.query(
            TableName="birthday-sms",
            KeyConditionExpression="birthday = :birthday",
            ExpressionAttributeValues = {
                    ":birthday": {'S': today}
                }
        )["Items"]

        # birthdays are stored as "DD/MM", this list will contain today's birthdays :)
        for birthday in birthdays:
            # send a reminder
            self.send_message("Today is {}'s birthday".format(birthday["person"]["S"]))
            print("sending birthday sms for {}".format(birthday["person"]["S"])) # debugging

    # send message using twilio API
    def send_message(self, body):
        payload = {
            "Body":body,
            "From":"+14083370462",
            "To":"+14164276256"
        }

        # api request to send sms
        response = requests.request("POST", url="https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json".format(self.twilio_sid),
                auth = (self.twilio_sid, self.twilio_api_token),
                data = payload
            )
        # log any errors that might arise 
        if (response.status_code >= 400):
            print(response.json())

if __name__ == "__main__":
    birthday_sms().fetch_birthdays()