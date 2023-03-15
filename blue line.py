import turtle as t;

#초기 설정
length = 100;
angle = 90;
width = 10;

colors = ["red", "green", "blue"];

t.shape("turtle");
t.width(width);
t.color(colors[2]);

#length만큼 앞으로, angle만큼 direction방향으로 회전
def goForwardAndTurn(length, angle, direction):

    if direction == "left":

        t.forward(length);
        t.left(angle);

    elif direction == "right":

        t.forward(length);
        t.right(angle);

#main
goForwardAndTurn(length, angle, "left");
t.forward(length);

t.mainloop();
t.Terminator();