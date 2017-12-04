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


def register():
    query = """
        mutation {
            register(email: \"sachit.singh@yipl.com.np\") {token}
        }
    """

    print query

    respond(requests.post(os.environ.get('url'), json = {'query': query}, headers = headers),
        inspect.currentframe().f_code.co_name)

def verifyCode():
    headers.update({'Authorization': os.environ.get('token')})

    query = """
        mutation {
            verifyCode(code: \"47308\") { status message User { firstName lastName email } }
        }
    """

    respond(requests.post(os.environ.get('url'), json = {'query': query}, headers = headers),
        inspect.currentframe().f_code.co_name)
