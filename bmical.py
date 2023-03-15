import math as m;

weight = float(input("몸무게를 kg 단위로 입력하시오 | "));
height = float(input("키를 m 단위로 입력하시오 | "));

bmi = weight / m.pow(height, 2);

if (bmi < 18.5):

    result = "저체중"

elif (bmi >= 18.5 and bmi < 25.0):

    result = "표준"

elif (bmi >= 25.0 and bmi < 30.0):

    result = "과체중"

elif (bmi >= 30):

    result = "비만"
    
print("당신의 bmi는 " + str(bmi) + "이고, " + result + "입니다.");