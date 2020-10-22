import boto3
from boto3.dynamodb.conditions import Key

# data migration util
dynamo = boto3.client("dynamodb")


name = 'Alex Jabbour'
print(boto3.client("dynamodb").query(
    TableName="Birthdays",
    KeyConditionExpression=Key("key_name").eq(name)
    ))

exit()

oldTable=''
newTable=''

items = dynamo.scan(TableName=oldTable)["Items"]
for item in items:
	dynamo.update_item(TableName=newTable, Key={
		"person":item["key-name"],
		"birthday":item["val-birthday"]
		})