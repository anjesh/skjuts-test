import os, sys, inspect, requests

sys.path.append(os.getcwd() + '/util/')
from helper import respond, env

# will be changed; temporary implementation
headers = {'Content-Type': 'application/json', 'Authorization': env('token')}

def createTrip():
    query = """
        mutation {
            createTrip(input: {
            description: \"Hello World\",
            type: wanted,
            TripStart: { name: \"hawai\", countryCode: \"NP\", coordinates:[20.0,20.0] },
            TripEnd: { name: \"la\", countryCode:\"NP\", coordinates:[20.0,20.0] },
            Stops:[],
            returnTrip: true,
            dates:[\"2017-02-11\",\"2017-10-11\"],
            time:\"02:00\",
            flexibility: \"15min\",
            photo:\"\" })
            {
                id,
                photo,
                date,
                TripStart { name }
                User { firstName }
            }
        }
    """

    print query

    respond(requests.post(env('url'), json = {'query': query}, headers = headers),
        inspect.currentframe().f_code.co_name
    )
