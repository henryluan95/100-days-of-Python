def turn_right():
    turn_left()
    turn_left()
    turn_left()


def navigate_left():
    while wall_in_front():
        turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
    if wall_in_front():
        navigate_left()
    else:
        move()