# Bash script written by master Jubs :D
aws dynamodb create-table \
    --table-name birthday-reminders \
    --attribute-definitions \
        AttributeName=person,AttributeType=S \
        AttributeName=birthday,AttributeType=S \
    --key-schema \
        AttributeName=birthday,KeyType=HASH \
        AttributeName=person,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
