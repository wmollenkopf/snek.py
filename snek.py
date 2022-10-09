from turtle import Turtle

MOVE_DISTANCE = 20
UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0

class Snek:

    def __init__(self):
        self.segments = []
        self.__create_snek()
        self.head = self.segments[0]

    def __create_snek(self):
        for i in range(3):
            position = (i * -20, 0)
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        self.segments.append(segment)

    def up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)

    def down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)

    def right(self):
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)
