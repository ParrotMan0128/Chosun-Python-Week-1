import turtle as t;

t.shape("turtle");

length = int(input("정사각형 한 변의 길이를 입력해주세요 | "));

#length만큼 앞으로 이동 후 angle만큼 direction방향으로 회전
def goForwardAndTurn(length, angle, direction):

    if (direction == "left"):

        t.forward(length);
        t.left(angle);

    elif (direction == "right"):

        t.forward(length);
        t.right(angle);

for i in range(4):

    goForwardAndTurn(length, 90, "left");

t.mainloop();
t.Terminator();