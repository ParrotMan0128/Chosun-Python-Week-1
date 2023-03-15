print("안녕하세요?\n");

name = str(input("이름이 어떻게 되시나요? "));
print("만나서 만갑습니다." + name + "씨.");
print("이름의 길이는 " + str(len(name)) + "글자 이군요.\n");

age = int(input("나이가 어떻게 되시나요? "));
print("내년이면 " + str(age + 1) + "살이군요.\n");

motherAge = int(input("어머니의 나이가 어떻게 되시나요? "));
print("어머님과 저는 " + str(motherAge - age) + "살 차이입니다.");