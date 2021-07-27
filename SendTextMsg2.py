import json
import requests
import kakao_utils

KAKAO_TOKEN_FILENAME = "res/kakao_message/kakao_token.json"
KAKAO_APP_KEY = "My REST Key"

tokens = kakao_utils.update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)
# 업데이트한 토큰 저장하기
#save_tokens(KAKAO_TOKEN_FILENAME, tokens)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + tokens['access_token']
}

template = {
    "object_type" : "list",
    "header_title" : "초밥 사진",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "1. 광어초밥",
            "description" : "광어는 맛있다",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "2. 참치초밥",
            "description" : "참치는 맛있다",
            "image_url" : "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }

    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]

}

data = {
    "template_object" : json.dumps(template)
}

# 나에게 카카오톡 메시지 보내기 요청(list)
response = requests.post(url, data=data, headers=headers)
print(response.status_code)

# 요청에 실패했다면,
if response.status_code != 200:
    print("error! because ", response.json())
else: # 성공했다면,
    print('메시지를 성공적으로 보냈습니다.')
