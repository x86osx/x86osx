import requests

#이미지가 있는 url 주소
url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

#해당 url로 서버에게 요청
img_response = requests.get(url)

#요청에 성공했다면,
if img_response.status_code == 200 :
    print(img_response.content)

    print("==== [이미지 저장] ====")
    with open("test.jpg", "wb") as fp:  #이미지는 바이너리로 저장 "wb"
        fp.write(img_response.content)