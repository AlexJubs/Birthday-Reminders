# Written by Alex Jabbour june 26
import boto3

def remove_item(name):
    # Python SDK for AWS DynamoDB
    aws_client = boto3.client("dynamodb")

    # we scan the table because the values are hashed by birthdate 
    # to allow for retrieving the people's birthdays on each date by the date
    table = aws_client.scan(TableName="birthday-sms")["Items"]

    for person in table:

        if person["person"]["S"] == name:
            print("Removing {} from database".format(name))

            # remove the item from the database, and exit the database
            aws_client.delete_item(TableName="birthday-sms", Key=person)
            return

    # after we've checked all the entries and haven't exited
    print("Could not find {} in database".format(name))

if __name__ == "__main__":
    # get name, and pass it through funct
    name = input("Please enter the person's Full name: ")
    remove_item(name)
