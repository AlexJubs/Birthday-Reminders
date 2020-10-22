import boto3
from boto3.dynamodb.conditions import Key

# data migration util

items = boto3.client("dynamodb").scan(TableName="Birthdays")
for item in items:
	item["person"] = item["key-name"]
	item["birthday"] = item["val-birthday"]

exit()
name = 'Alex Jabbour'
print(boto3.client("dynamodb").query(
    TableName="Birthdays",
    KeyConditionExpression=Key("key_name").eq(name)
    ))