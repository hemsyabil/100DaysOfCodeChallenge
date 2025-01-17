# https://reeborg.ca/reeborg.html

# Hurdle 1 solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    move_cycle()

# Hurdle 2 solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    move_cycle()
    
# Hurdle 3 solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_cycle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        move_cycle()
    
    
# Hurdle 4 solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_cycle():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    else:
        move_cycle()
    
