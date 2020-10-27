# Birthday SMS
A simple python script to send a SMS to my number reminding me whenever someone's birthday is coming or happpening.

SMS using Twilio SMS API <br>
Datastore to be used: `AWS DynamoDB` - a simple NoSQL key=value database <br>
Credstash is used to get API keys - integrates well with AWS KMS 🧼 <br>

Additionally, this repo contains my own APIs for adding or removing a birthday from the database

As of now (June 2020), this script is ran daily on `AWS Lambda` (Using my personal AWS account)

Coming soon:
- A form which lets you submit your birthday so I can be reminded 😄
- Script to parse my Facebook friend's birthdays using Puppeteer, and add them to my list 🧠
