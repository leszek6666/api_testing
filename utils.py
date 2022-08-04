from fixtures import *
import requests

def construct_url(common_url, api):
    return common_url + api

def get_token():
    url = construct_url(BASIC_URL, TOKENS)
    payload={'email':'test@airportgap.com',"password":'airportgappassword'}
    response = requests.post(url,json=payload)
    assert response.status_code == 200, print("Got wrong status code, expected is: ?{}, actual is {}".format("200", r.status_code))
    print(response.content)
    print(response.status_code)
    r = response.json()
    token = r['token']
    return token