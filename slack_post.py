from slack_sdk import WebClient
import os
from dotenv import load_dotenv

from key import SLACK_API_TOKEN

load_dotenv()

os.environ["SLACK_API_TOKEN"]=SLACK_API_TOKEN

client = WebClient(token=os.getenv("SLACK_API_TOKEN"))

def post_results_on_slack(channel, results):

    # Creating a message from the results
    message = "Here are the answers to your questions:\n"
    for question, answer in results.items():
        message += f"Q: {question}\nA: {answer}\n\n"
    
    # posting the message
    response = client.chat_postMessage(channel=channel, text=message)
    if not response['ok']:
        print(f"Failed to send message to Slack: {response['error']}")

