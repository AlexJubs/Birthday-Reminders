# Bash script written by master Jubs :D
aws dynamodb create-table \
    --table-name Birthdays \
    --attribute-definitions \
        AttributeName=person,AttributeType=S \
        AttributeName=birthday,AttributeType=S \
    --key-schema \
        AttributeName=person,KeyType=HASH \
        AttributeName=birthday,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
