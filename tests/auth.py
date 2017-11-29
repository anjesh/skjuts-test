import os, sys, inspect, requests

sys.path.append(os.getcwd() + '/util/')
from helper import respond, env

# will be changed; temporary implementation
headers = {'Content-Type': 'application/json'}

def login():
    query = """
        mutation {
            login(input: {username: \"%s\", password: \"%s\"}) {token}
        }
    """ % (env('username'), env('password'))

    print query

    respond(
        requests.post(env('url'), json = {'query': query}, headers = headers),
        inspect.currentframe().f_code.co_name
    )


# def register():
#     # authHeaders = {'Content-Type': 'application/json', 'Authorization': os.environ.get('token')}
#     query = """
#         mutation {
#             register(email: \"sbs1@sbs.com\") {token}
#         }
#     """

#     print query


#     respond(requests.post(os.environ.get('url'), json = {'query': query}, headers = headers),
#         inspect.currentframe().f_code.co_name)
