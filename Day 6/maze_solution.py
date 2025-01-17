# Maze solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()


# Alternate solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        if right_is_clear():
            turn_right()
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if not wall_in_front():
            move()
    