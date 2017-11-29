import os, json

from dotenv import load_dotenv
from termcolor import colored

load_dotenv(os.getcwd() + '/.env')


def respond(response, functionName):
    statusCode = response.status_code
    response = json.loads(response.content)

    print '#Response: %s' % response

    if (statusCode == 200 and response['data'][functionName]):
        print colored('--> Test for ' + functionName + ' passed.', 'green')
    else:
        print colored('--> Test for ' + functionName + ' failed.', 'red')
        print colored('--> Response: ' + response['errors'][0]['message'], 'yellow')

def env(key):
    return os.environ.get(key)
