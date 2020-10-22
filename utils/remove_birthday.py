# Written by Alex Jabbour june 26
import boto3

def remove_item(name):
    # Python SDK for AWS DynamoDB
    aws_client = boto3.client("dynamodb")

    # find the birthday by scanning the database
    table = aws_client.scan(TableName="Birthdays")["Items"]

    for person in table:

        if person["Name"]["S"] == name:
            print("Removing {} from database".format(name))

            # remove the item from the database, and exit the database
            aws_client.delete_item(TableName="Birthdays", Key=person)
            return

    # after we've checked all the entries and haven't exited
    print("Could not find {} in database".format(Name))

if __name__ == "__main__":
    # get name, and pass it through funct
    name = input("Please enter the person's Full name: ")
    remove_item(name)
