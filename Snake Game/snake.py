from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = [] # FIRST 3 SEGMENTS
        self.create_snake()
        self.head = self.segments[0] # THE HEAD OF THE SNAKE

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()  # NO LINE AFTER
        new_segment.color("white")  # WHITE COLOR OF THE SQUARE
        new_segment.goto(position)  # (0, 0), (-20, 0), (-40, 0)
        self.segments.append(new_segment)  # 1 MORE SQUARE

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE) # 20

    def up(self):
        if self.head.heading() != DOWN: #270
            self.head.setheading(UP) # 90

    def down(self):
        if self.head.heading() != UP: #90
            self.head.setheading(DOWN) #270

    def left(self):
        if self.head.heading() != RIGHT: # 0
            self.head.setheading(LEFT) # 180

    def right(self):
        if self.head.heading() != LEFT: # 180
            self.head.setheading(RIGHT) # 0

