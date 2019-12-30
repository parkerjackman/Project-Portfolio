import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def __draw_head(self):
        turtle.penup()
        turtle.goto(0,-100)
        turtle.pendown()
        turtle.setheading(0)
        turtle.pensize(1)
        if self.__happy:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __draw_eyes(self):
        turtle.penup()
        turtle.goto(-25,25)
        turtle.pendown()
        turtle.pensize(1)
        if self.__dark_eyes:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.circle(10)

        turtle.penup()
        turtle.goto(25, 25)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()

    def __draw_mouth(self):
        turtle.penup()
        if self.__smile:
            turtle.goto(-35, -35)
            turtle.setheading(-45)
        else:
            turtle.goto(35, -45)
            turtle.setheading(135)
        turtle.pendown()
        turtle.pensize(3)
        turtle.circle(50, 90)

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = not self.__smile
        self.draw_face()

    def change_emotion(self):
        self.__happy = not self.__happy
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = not self.__dark_eyes
        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() == True else "smile"
        emotion = "angry" if face.is_happy() == True else "happy"
        eyes = "blue" if face.is_dark_eyes() == True else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
