import os, sys, inspect, requests

sys.path.append(os.getcwd() + '/util/')
from helper import respond, env

headers = {'Content-Type': 'application/json', 'Authorization': env('token')}

def group():
    groupInput = {
        'outreach': 'route',
        'tripStart': '{ name: "Kathmandu", countryCode: "NP", coordinates:[20.0,20.0] }',
        'tripEnd': '{ name: \"Pokhara\", countryCode:\"NP\", coordinates:[10.0,20.0] }',
        'stops': '[{name: \"Mugling\", countryCode: \"NP\", coordinates: [11.0,12.0]}]',
        'countryCode': 'NP',
        'name': 'Test Group',
        'description': 'This is a Test Group',
        'type': 'OpenGroup',
    }

    query = """
        mutation {
            group(input: {
                outreach: %s,
                TripStart: %s,
                TripEnd: %s,
                Stops: %s,
                countryCode: \"%s\",
                name: \"%s\",
                description: \"%s\",
                type: %s
            }) {
                name
                description
                User { id email }
                country
                stopsIds
                Stops { name countryCode coordinates }
                type
                outreach
            }
        }
    """ % (
            groupInput['outreach'],
            groupInput['tripStart'],
            groupInput['tripEnd'],
            groupInput['stops'],
            groupInput['countryCode'],
            groupInput['name'],
            groupInput['description'],
            groupInput['type'],
        )

    print query

    respond(groupInput, requests.post(env('url'), json = {'query': query}, headers = headers), inspect.currentframe().f_code.co_name)
