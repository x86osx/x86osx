from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sister;
                and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">tillie</a>;
and they lived at the bottom of well.</p>

<p class="story'>...</p>
</body>
"""


#Beautifulsoup 객체를 생성한다.
soup = BeautifulSoup(html_doc, 'lxml')

#객체.태그 이름
#.태그 이름으로 하위 태그로의 접근이 가능하다.
print("soup.body.p의 결과 :", soup.body.p)

#객체.태그 이름['속성이름']
#객체의 태그 속성은 파이썬 딕셔너리처럼 태그 ['속성 이름']으로 접근이 가능핟.
print("soup.a['href']", soup.a['href'])

#객체.name
## name 변수
print("soup.title.name의 결과 :", soup.title.name)

#객체.string
## string 변수 (참고) NavigableString : 문자열은 태그 안에 텍스트에 사용한다. BeautifulSoup 은 이런 텍스트를 포함하는 NavigableString  클래스를 사용한다.
print("soup.title.string의 결과 :", soup.title.string)

#객체.contents
## 태그의 자식들은 리스트로 반환
print("soup.contents의 결과 ", soup.contents)

print("soup.find()의 결과 :", soup.find('a', attrs={'class' : 'sister'} ))

print("soup.all()의 결과 : ", soup.find_all('a', limit=2))