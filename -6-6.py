import turtle as t;

length = 100;
angle = 90;

#length만큼 앞으로, angle만큼 direction 방향으로 회전
def goFowardAndTurn(length, angle, direction):

    if direction == "left":

        t.forward(length);
        t.left(angle);

    elif direction == "right":

        t.forward(length);
        t.right(angle);

t.shape("turtle");

goFowardAndTurn(length, angle, "left");
goFowardAndTurn(length, angle, "right");
goFowardAndTurn(length, angle, "right");
goFowardAndTurn(length, angle, "left");
t.forward(length);

t.mainloop();
t.Terminator();

