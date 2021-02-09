def collision_wall(head):
    if head.pos()[0] > 280 or head.pos()[0] < -280 or head.pos()[1] > 280 or head.pos()[1] < -280:
        print("Collision wall!!!")
        return True


def collision_body(body):
    # I have to check if the snake head's distance from any of its part is inferior to 10
    for x in range(1, len(body)):
        if body[0].distance(body[x]) < 10:
            print("Collision body!!!")
            return True
