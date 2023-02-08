joseph = Actor("mario")
joseph.pos = 250,100
test = 0

WIDTH = 500
HEIGHT = 300

def draw():
    screen.fill((0,0,0))
    joseph.draw()

def update():
    if joseph.image != "mario_clicked":
        joseph.left = joseph.left+2
        if joseph.left > WIDTH:
            joseph.right = 0

def on_mouse_down(pos):
    if joseph.collidepoint(pos):
        joseph.image = "mario_clicked"
        sounds.boom.play()
        print("you clicked him.")
        test = 1
    else:
        print("you missed")
