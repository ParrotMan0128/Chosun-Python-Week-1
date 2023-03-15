import math as m;

radius = float(input("구의 반지름을 입력하십시오 | "));

volume = (4/3) * m.pi * m.pow(radius, 3); 
square = 4 * m.pi * m.pow(radius, 2);

print("구의 부피는 " + str(volume) + "입니다.");
print("구의 겉넓이는 " + str(square) + "입니다.");