import json
import requests
import datetime
import os

KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"

def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)
    return tokens

def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kakao.com/oauth/token"
    data = {
        "grant_type" : "refresh_token",
        "client_id" : app_key,
        "refresh_token" : tokens['refresh_token']
    }
    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("error! because", response.json())
        tokens = None
    else :
        print(response.json())

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename+"."+now
        os.rename(filename, tokens)

    return tokens

#KAKAO_APP_KEY = "6148d6e7b45b3f0b0cc0b38f6739a45b"
#tokens = update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
#save_tokens(KAKAO_TOKEN_FILENAME, tokens)
