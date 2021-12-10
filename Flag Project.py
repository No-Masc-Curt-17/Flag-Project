#import statements
import turtle as trtl
import random as rand
import time
#config turtles
Flag_drawer = trtl.Turtle()
Flag_drawer.speed(0)
Flag_drawer.penup()
Flag_drawer.goto(-247, -130)
Flag_drawer.pendown()
wn = trtl.Screen()
t = trtl.Turtle()
t.speed(0)
#create outline with dimensions of American Flag
for i in range(2):
    Flag_drawer.forward(494)
    Flag_drawer.left(90)
    Flag_drawer.forward(260)
    Flag_drawer.left(90)

#Description of game
game_description = print("Welcome to the Flag Game. Guess a number between number 1-10 to choose the color(s) of the American Flags stripes, banner, and stars. Choose the correct combination of numbers to color the American Flag correctly. Remember, the right answers don't change, so once you get it right, keep the same number. Good luck!")

#reconfig turtles
Flag_drawer.hideturtle()
t.hideturtle()
Flag_drawer.penup()
Flag_drawer.setheading(0)
stripe = 0
Flag_drawer.pendown()

#user picks number for the stripe colors
user_input = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))
#5 is correct, everything else is incorrect
if user_input != 5:
  print("Too bad. You chose the wrong stripe color!")
else:
  print("Good job! You chose the right stripe color!")

#for if the user picks a number not between 1 and 10
while user_input > 10 or user_input < 1:
  print("Error. Try again.")
  user_input = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))

#uses the users number to check if right or wrong
def stripe_color():
    #if wrong produces random colors
    if user_input != 5:
        colors = ["blue", "red", "green","pink", "yellow", "black", "brown", "cyan", "silver"]
        random = rand.randint(1,8)
        color = colors[random]
        Flag_drawer.fillcolor(color)
    #if correct, colors alternate between red and white
    elif user_input == 5:
        colors = ["red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red"]
        Flag_drawer.fillcolor(colors[stripe])

#creates and fills in the 6 longer stripes
while stripe <= 5:
    Flag_drawer.begin_fill()
    stripe_color()
    for i in range(2):
        Flag_drawer.forward(494)
        Flag_drawer.left(90)
        Flag_drawer.forward(20)
        Flag_drawer.left(90)
    Flag_drawer.end_fill()
    Flag_drawer.left(90)
    Flag_drawer.forward(20)
    Flag_drawer.right(90)
    stripe += 1

Flag_drawer.fd(200)
#creates and fills in the shorter stripes
while stripe < 13:
    Flag_drawer.begin_fill()
    stripe_color()
    for i in range(2):
        Flag_drawer.forward(294)
        Flag_drawer.left(90)
        Flag_drawer.forward(20)
        Flag_drawer.left(90)
    Flag_drawer.end_fill()
    Flag_drawer.left(90)
    Flag_drawer.forward(20)
    Flag_drawer.right(90)
    stripe += 1

#user guesses for the box color
user_input_2 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the box color: "))
#if their number is not between 1 and 10
while user_input_2 > 10 or user_input_2 < 1:
  print("Error. Try again.")
  user_input_2 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the banner color: "))
#creates a function that will set the banner color
def banner_color():
    #creates a function that will set the banner color
    if (user_input_2 == 2):
        Flag_drawer.fillcolor("blue")
        print("Good job. You chose the right banner colors!")
    #if they get it wrong, the color could be any of the colors below
    else:
        colors = ["black", "brown", "cyan", "silver", "gold"]
        random = rand.randint(1,4)
        color = colors[random]
        Flag_drawer.fillcolor(color)
        print("Too bad. You chose the wrong banner color!")
        Flag_drawer.penup()
        Flag_drawer.goto(rand.randint(-400,400),rand.randint(-400,400))
        Flag_drawer.pendown()

#this creates the banner
banner_color()
Flag_drawer.penup()
Flag_drawer.goto(-247,-10)
Flag_drawer.penup()
Flag_drawer.begin_fill()
for i in range(2):
    Flag_drawer.forward(200)
    Flag_drawer.left(90)
    Flag_drawer.forward(140)
    Flag_drawer.left(90)
Flag_drawer.end_fill()

#Prompts the user to choose a number 1-10 to guess the star colors
user_input_3 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the star colors: "))
#Makes sure that the input is in between 1-10
while user_input_3 > 10 or user_input_3 < 1:
  print("Error. Try again.")
  user_input_3 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))
#Definition that contains the drawing of the stars, the coloring of it, and the amount of it
def stars():
    #Definition that sees if the user is correct or not
    def star_color():
        #if the user guesses 4, the stars become the right color (white)
        if (user_input_3 == 4):
            t.color("white")
        #if the user doesn't guess 4, the stars become random colors
        elif (user_input_3 != 4):
            colors = ["blue", "red", "green","pink", "yellow"]
            random = rand.randint(1,4)
            color = colors[random]
            t.color(color)
    #Sees if the user got it right; if they did, it prints that they did; else, it prints that they didn't         
    def reaction():
        if (user_input_3 != 4):
            print("Too bad. You picked the wrong star color!")
        else:
          print("Good job! You chose the right star color!")
    reaction()    
    #Calculates the number of rows, and the x/y positions of the rows containing 5 or 6 rows    
    star_row = 0
    x_cor = -257
    y_cor = 115
    x_cors = -242
    y_cors = 105
    while(star_row<9):
      star_row+=1
      #code containing rows with 6 stars
      if(star_row == 1 or star_row == 3 or star_row == 5 or star_row == 7 or star_row == 9):
        t.penup()
        t.goto(x_cor,y_cor)
        t.pendown()
        y_cor-= 25
        for i in range(6):
          t.penup()
          t.fd(28)
          t.pendown()
          t.begin_fill()
          star_color()
          for i in range(5):
            t.fd(12)
            t.right(144)
          t.end_fill()
      #code containing the rows with 5 stars    
      if(star_row == 2 or star_row == 4 or star_row == 6 or star_row == 8):
          t.penup()
          t.goto(x_cors,y_cors)
          t.penup()
          y_cors -= 25
          for i in range(5):
            t.penup()
            t.fd(28)
            t.pendown()
            t.begin_fill()
            star_color()
            for i in range(5):
              t.fd(12)
              t.right(144)
            t.end_fill()

#uses the user inputs to see if they got all 3 colors right; if they did, a check mark moves across the screen, and it prints on the
# window that they won; if they didn't, an x moves accross the screen, and prints on the window that they lost
def attempts():
  t.pencolor("Black")
  fontchoice = ('Times New Roman', '69', 'bold')
  if (user_input == 5 and user_input_2 == 2 and user_input_3 == 4):
    t.penup()
    t.goto(-225,-50)
    t.pendown()
    winner = t.write("You won!!!",move='Center', font=fontchoice)
    x=0
    t.speed(3)
    time.sleep(5)
    for i in range(10):
      randomnesss = rand.randint(-300,300)
      randomss = rand.randint(-300,300)
      t.st()
      wn.addshape('checkmark.gif')
      t.penup()
      t.goto(randomnesss,randomss)
      t.pendown()
      t.shape('checkmark.gif')
  else:
    t.penup()
    t.goto(-175,-50)
    t.pendown()
    lost = t.write("You lost.",move='Center', font=fontchoice)
    x=0
    time.sleep(3)
    Flag_drawer.speed(4)
    for i in range(10):
      randomness = rand.randint(-300,300)
      randoms = rand.randint(-300,300)
      Flag_drawer.st()
      wn.addshape('x.gif')
      Flag_drawer.goto(randomness,randoms)
      Flag_drawer.shape('x.gif')
    
#calls the stars and attempts function
stars()
attempts()
wn.mainloop()