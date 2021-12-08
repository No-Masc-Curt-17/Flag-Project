import turtle as trtl
import random as rand
Flag_drawer = trtl.Turtle()
Flag_drawer.speed(0)
Flag_drawer.penup()
Flag_drawer.goto(-247, -130)
Flag_drawer.pendown()
wn = trtl.Screen()
t = trtl.Turtle()
t.speed(0)
for i in range(2):
    Flag_drawer.forward(494)
    Flag_drawer.left(90)
    Flag_drawer.forward(260)
    Flag_drawer.left(90)

Flag_drawer.hideturtle()
t.hideturtle()
Flag_drawer.penup()
Flag_drawer.setheading(0)
stripe = 0
Flag_drawer.pendown()

user_input = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))
while user_input > 10 or user_input < 1:
  print("Error. Try again.")
  user_input = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))

def stripe_color():
    if user_input != 5:
        colors = ["blue", "red", "green","pink", "yellow", "black", "brown", "cyan", "silver"]
        random = rand.randint(1,8)
        color = colors[random]
        Flag_drawer.fillcolor(color)
    elif user_input == 5:
        colors = ["red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red", "white", "red"]
        Flag_drawer.fillcolor(colors[stripe])



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

user_input_2 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the box color: "))
while user_input_2 > 10 or user_input_2 < 1:
  print("Error. Try again.")
  user_input_2 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))
def banner_color():
    if (user_input_2 == 2):
        Flag_drawer.fillcolor("blue")
        print("Good job. You've made it to the next level!")
    else:
        colors = ["blue", "red", "green","pink", "yellow", "black", "brown", "cyan", "silver", "gold"]
        random = rand.randint(1,8)
        color = colors[random]
        Flag_drawer.fillcolor(color)
        print("Too bad. Better luck next time!")
        Flag_drawer.penup()
        Flag_drawer.goto(rand.randint(-400,400),rand.randint(-400,400))
        Flag_drawer.pendown()
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

user_input_3 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the star colors: "))
while user_input_3 > 10 or user_input_3 < 1:
  print("Error. Try again.")
  user_input_3 = int(wn.textinput('Menu',"Pick a number 1-10 to choose the stripe color: "))
def stars():
    def star_color():
        if (user_input_3 == 4):
            t.color("white")
        elif (user_input_3 != 4):
            colors = ["blue", "red", "green","pink", "yellow", "black", "brown", "cyan", "silver", "gold"]
            random = rand.randint(1,8)
            color = colors[random]
            t.color(color)
    def reaction():
        if (user_input_3 != 4):
            print("Too bad. Better luck next time!")
    reaction()        
    star_row = 0
    x_cor = -257
    y_cor = 115
    x_cors = -242
    y_cors = 105
    while(star_row<9):
      star_row+=1
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

def attempts():
  t.pencolor("Black")
  fontchoice = ('Times New Roman', '69', 'bold')
  if (user_input == 5 and user_input_2 == 2 and user_input_3 == 4):
    t.penup()
    t.goto(-225,-50)
    t.pendown()
    winner = t.write("You won!!!",move='Center', font=fontchoice)
    x=0
    t.speed(4)
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
    Flag_drawer.speed(4)
    for i in range(10):
      randomness = rand.randint(-300,300)
      randoms = rand.randint(-300,300)
      Flag_drawer.st()
      wn.addshape('x.gif')
      Flag_drawer.goto(randomness,randoms)
      Flag_drawer.shape('x.gif')
    

stars()
attempts()
wn.mainloop()