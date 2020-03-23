import json
import requests
import time
import random
import string
import os
from nacl.bindings import crypto_scalarmult_base
from base64 import b64encode
import datetime

# insert your desired GB
_YourGB = 1000000
# insert your Device ID something like this
_yourID = "31b7070c-953f-4641-b881-aef236342a87"

# insert your Device "access_token"
_yourToken = "112551e1-cfe8-46b9-becb-6f0cf26764ed" 

key=None



def get_info(_yourID, _yourToken):
	url = 'https://api.cloudflareclient.com/v0i1909221500/reg/' + _yourID.strip()
	headers = {"Authorization": "Bearer " + _yourToken.strip()}
	req = requests.get(url, headers=headers)
	req.raise_for_status()
	return req.json()
	
def show_quota(_yourID, _yourToken):
	info = get_info(_yourID, _yourToken)
	text = "				your Quota is : {}GB \n 		    	Wait 60 sec to increase Quota".format(round(int(info['result']['account']['quota']) / (10 ** 9), 2))
	print(text)	
	




def generate_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))
def generate_key():
        private_key = os.urandom(32)
        public_key = crypto_scalarmult_base(private_key)
        return b64encode(private_key).decode('utf-8'), b64encode(public_key).decode('utf-8')


def handle():
        return requests.post(url, headers=headers, data=json.dumps({"referrer": _yourID}))


for i in range(_YourGB):
    url = 'https://api.cloudflareclient.com/v0a745/reg'
    headers = {'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'}
    install_id = generate_string(11)

    key=generate_key()
    data = {"key": key[1],
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, generate_string(134)),
            "referrer": _yourID,
            "warp_enabled": True,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "en-GB"}


    
    _res = handle()
    _json_res = _res.json()
    print("You got {}GB data!!".format(i+1))
    if (i+1)%2 == 0:
            show_quota(_yourID, _yourToken)
            time.sleep(60)
