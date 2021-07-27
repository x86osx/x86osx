import json

import requests


url="https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "My REST Key",
    "redirect_uri" : "https://localhost.com",
    "code" : "My Code"
}

response = requests.post(url, data=data)

if response.status_code != 200 :
    print("error! because ", response.json())
else :
    tokens = response.json()
    print(tokens)
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)

