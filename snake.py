from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    segment_1 = Turtle(shape="square")

    segments = []
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]#segments is populated with create_snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())#-1 starts counting from the end
        #the segment above is added to the same position as the last segment


    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].xcor(),#other segments follow first one
                                         self.segments[seg_num-1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
