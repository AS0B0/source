f1 = open("test.txt", 'a')
while True:
    key_input = input("텍스트를 입력하세요: ")
    if key_input == '999' : break
    f1.write(key_input)
    f1.Write("\n")

f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
