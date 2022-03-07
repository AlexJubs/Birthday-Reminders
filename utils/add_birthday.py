# Written by Alex Jabbour june 26
import boto3
from pprint import pprint

dynamo = boto3.client("dynamodb")

def create_entry(birthday, name):

	# make sure the birthdate is correct format
	if int(birthday[:2]) > 31 or int(birthday[3:]) > 12 or len(birthday) != 5:
		print("haram birthday")
		return

	Item = {
		'person': {'S': name},
		'birthday': {'S': birthday}
		}

	if (check_if_exists(Item) == False):
		print("This birthday already exists in the database")
		return

	print("adding {} to the database".format(name))
	
	# put the item in the database
	dynamo.update_item(TableName='birthday-sms', Key=Item)


def check_if_exists(item):
	response = dynamo.get_item(
		TableName='birthday-sms', Key=item
	)
	# condition for true response
	return not ("item" in response)


if __name__ == "__main__":
	# get birthday, and pass it through funct
	name = input("Please enter the person's Full name: ")
	birthday = input("Please enter person's birthday (DD/MM): ")
	create_entry(birthday, name)