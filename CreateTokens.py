import json

import requests


url="https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "6148d6e7b45b3f0b0cc0b38f6739a45b",
    "redirect_uri" : "https://localhost.com",
    "code" : "bhUNmd6TCMuk8Z8vYejWydbGvKmQ54si7yEjvl2O3yDcLzKKhqk3E4TjcMExJYfXT7Wo7Ao9dJcAAAF66RQ9UA"
}

response = requests.post(url, data=data)

if response.status_code != 200 :
    print("error! because ", response.json())
else :
    tokens = response.json()
    print(tokens)
    with open("kakao_token.json", "w") as fp:
        json.dump(tokens, fp)

'''
{'access_token': '07ARBNfH9hTSeoE6y3WeaNGfX2WuzmEsRxKPAAopcFEAAAF66Obt2w', 'token_type': 'bearer', 'refresh_token': 'r-Tj9KWLlPHqAPI3NBzVm3nnPwEiHy_9Mf1qYAopcFEAAAF66Obt2Q', 'expires_in': 21599, 'scope': 'account_email profile_image talk_message profile_nickname', 'refresh_token_expires_in': 5183999}

'''