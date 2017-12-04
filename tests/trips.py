import os, sys, inspect, requests

sys.path.append(os.getcwd() + '/util/')
from helper import respond, env

# will be changed; temporary implementation
headers = {'Content-Type': 'application/json', 'Authorization': env('token')}

def createTrip():
    tripInput = {
        'description': 'Trip create test',
        'type': 'wanted',
        'tripStart': '{ name: "Kathmandu", countryCode: "NP", coordinates:[20.0,20.0] }',
        'tripEnd': '{ name: \"Pokhara\", countryCode:\"NP\", coordinates:[10.0,20.0] }',
        'stops': '[{name: \"Mugling\", countryCode: \"NP\", coordinates: [11.0,12.0]}]',
        'returnTrip': 'true',
        'dates': '[\"2017-02-11\",\"2017-10-11\"]',
        'time': '02:00',
        'flexibility': '15min',
        'seats': '10'
    }

    query = """
        mutation {
            createTrip(input: {
            description: \"%s\",
            type: %s,
            TripStart: %s,
            TripEnd: %s,
            Stops: %s,
            returnTrip: %s,
            dates: %s,
            time:\"%s\",
            flexibility: \"%s\",
            seats: %s })
            {
                description,
                type,
                TripStart { name countryCode }
                TripEnd { name countryCode }
                Stops { name countryCode }
                returnTrip
                date
                time
                flexibility
                seats
                User { email }
            }
        }
    """ % (
            tripInput['description'],
            tripInput['type'],
            tripInput['tripStart'],
            tripInput['tripEnd'],
            tripInput['stops'],
            tripInput['returnTrip'],
            tripInput['dates'],
            tripInput['time'],
            tripInput['flexibility'],
            tripInput['seats']
        )

    print query

    respond(tripInput, requests.post(env('url'), json = {'query': query}, headers = headers), inspect.currentframe().f_code.co_name)
