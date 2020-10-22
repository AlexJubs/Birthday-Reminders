import boto3
from boto3.dynamodb.conditions import Key
import datetime

# data migration util
dynamo = boto3.client("dynamodb")
today = datetime.datetime.today().strftime('%d/%m') # today in MM/DD

birthdays = dynamo.query(
    TableName="birthday-sms",
    KeyConditionExpression="birthday = :birthday",
    ExpressionAttributeValues = {
            ":birthday": {'S': "17/07"}
    }
)["Items"]
print(birthdays)
exit()

oldTable=''
newTable=''

items = dynamo.scan(TableName=oldTable)["Items"]
for item in items:
	dynamo.update_item(TableName=newTable, Key=item)