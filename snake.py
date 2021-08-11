from turtle import Turtle
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        location = 0
        for location in POSITIONS:
            self.add_segment(location)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
             new_x = self.segments[seg_num - 1].xcor()
             new_y = self.segments[seg_num - 1].ycor()
             self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


