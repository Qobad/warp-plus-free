import json
import requests
import time
# insert your desired GB
_YourGB = 1000000
# insert your Device ID something like this 
_yourID = "047e57ef-49b3-462b-afc0-e32a0ebd11e5"

def handle():
    return requests.post("https://api.cloudflareclient.com/v0a745/reg", data=json.dumps({"referrer": _yourID}))


for i in range(_YourGB):
    _res = handle()
    _json_res = _res.json()
    print("You got {}GB data!!".format(i+1))
    if (i+1)%3 == 0:
        time.sleep(60)
