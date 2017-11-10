import requests

username = 'sachit.singh@yipl.com.np'
password = 'core'
url = 'http://localhost:8080/api'
headers = {'Content-Type': 'application/json'}

def login():

    query = """
        mutation {
            login(input: {username:\"sbs@sbs.com\", password:\"111111\"}) {token}
        }
    """

    print query

    response = requests.post(url, json = {'query': query}, headers = headers)


    print(response.status_code, response.content)

def register():
    headers = {'Content-Type': 'application/json'}
    query = """
        mutation {
            register(email: \"sbs1@sbs.com\") {token}
        }
    """

    print query

    response = requests.post(url, json = {'query': query}, headers = headers)
    print(response.status_code, response.content)

# login()
register()
