import requests
from fixtures import *
from utils import *

def test_get_airports():
    url = construct_url(BASIC_URL, AIRPORTS)
    response = requests.get(url)
    assert response.status_code == 200, print(
        "Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))
    print('ok')

def test_get_favories():
    url = construct_url(BASIC_URL, FAVORITES)
    token = get_token()
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url,headers=headers)
    assert response.status_code == 200, print("Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))
    

def test_airports_distance():
    url = construct_url(BASIC_URL, AIRPORTS_DISTANCE)
    payload={"from":"KIX","to":"NRT"}
    response = requests.post(url,data=payload)
    assert response.status_code == 200, print("Got wrong status code, expected is: {}, actual is {}".format("200", response.status_code))
    r = response.json()
    distance = r['data']['attributes']['kilometers']


    assert distance == 490.8053652969214, print("Got wrong distance, expected is: {}, actual is {}".format("490.8053652969214", distance))
    print(distance)

