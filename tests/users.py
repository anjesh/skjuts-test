import os, sys, inspect, requests

sys.path.append(os.getcwd() + '/util/')
from helper import respond, env

headers = {'Content-Type': 'application/json', 'Authorization': env('token')}


def updateUser():
    userInput = {
        'firstName': 'sbs',
        'lastName': 'sbs',
        'password': '111111',
        'phoneNumber': '+9779841044832',
    }

    query = """
        mutation {
            updateUser(input: {
                firstName: \"%s\",
                lastName: \"%s\",
                password: \"%s\",
                phoneNumber: \"%s\",
                photo: \"\",
                fbId: \"\"
            }) {
                status
                token
                User { email firstName }
            }
        }
    """ % (
           userInput['firstName'],
           userInput['lastName'],
           userInput['password'],
           userInput['phoneNumber']
        )

    print query

    respond(
        userInput,
        requests.post(env('url'), json = { 'query': query }, headers = headers),
        inspect.currentframe().f_code.co_name
    )
