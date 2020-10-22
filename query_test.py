import boto3
from boto3.dynamodb.conditions import Key

name = 'Alex Jabbour'
print(boto3.client("dynamodb").query(
    TableName="Birthdays",
    KeyConditionExpression=Key("key_name").eq(name)
    ))