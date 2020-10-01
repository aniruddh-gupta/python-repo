import turtle
import time

wn=turtle.Screen()
wn.title("Animation")
wn.bgcolor("black")

player = turtle.Turtle()
player.shape("square")
player.color("green")

def player_animate():
    if player.shape() == "square":
        player.shape("circle")
    elif player.shape() == "circle":
        player.shape("square")
    
    #Set timer
    wn.ontimer(player_animate, 500)
   
player_animate()

while True:
    wn.update()
    print("Welcome! to Animation")
   
wn.mainloop()