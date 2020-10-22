import boto3
from boto3.dynamodb.conditions import Key

# data migration util
dynamo = boto3.client("dynamodb")


name = 'Alex Jabbour'
print(boto3.client("dynamodb").query(
    TableName="birthday-reminders",
    KeyConditionExpression="person = :person",
    ExpressionAttributeValues = {
        ":person": {'S': name}
    }
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