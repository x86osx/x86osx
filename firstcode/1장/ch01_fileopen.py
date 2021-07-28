#파일 쓰기
data = "Hello"
with open("../text.txt", "w") as fp:
    fp.write(data)

#파일 읽기
with open("../text.txt", "r") as fp:
    print("==== [파일 읽기 결과] ====")
    print(fp.read())
