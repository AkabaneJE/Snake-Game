import turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:    
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = turtle.Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def move(self):
        for segment_number in range(len(self.segments)-1, 0, -1):
             next_x = self.segments[segment_number -1].xcor()
             next_y = self.segments[segment_number -1].ycor()
             self.segments[segment_number].goto(next_x, next_y) 
        self.head.forward(20) 

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]    



    
        











































