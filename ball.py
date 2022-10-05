class Ball1:
    def __init__(self, ball_type=None):
        if ball_type is None:
            self.ball_type = "regular"
        else:
            self.ball_type = ball_type


class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


balltype = 'super'
ball = Ball(balltype)
print(ball.ball_type)
