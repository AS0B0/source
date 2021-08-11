f1 = open("test.txt", 'w')
f1.write("Life is too short!")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

user_input = input("저장할 내용을 입력하세요:")
f = open("test.txt",'a')
f.write(user_input)
f.write("\n")
f.close()
