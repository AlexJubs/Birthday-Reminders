# Written by Alex Jabbour june 26
import boto3
from pprint import pprint

dynamo = boto3.client("dynamodb")

def create_entry(birthday, name):

	Item = {
		'key-name': {'S': name},
		'val-birthday': {'S': birthday}
		}

	if (check_if_exists(Item)):
		print("This birthday already exists in the database")
		return

	# put the item in the database
	dynamo.update_item(TableName='Birthdays', Key=Item)

def check_if_exists(Item):
	response = dynamo.get_item(
		TableName='Birthdays', Key=Item
	)
	# condition for true response
	return not ("item" in response)


if __name__ == "__main__":
	# get birthday, and pass it through funct
	name = input("Please enter the person's Full name: ")
	birthday = input("Please enter person's birthday (DD/MM): ")
	create_entry(birthday, name)