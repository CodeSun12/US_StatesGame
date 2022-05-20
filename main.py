import turtle
import pandas


screen = turtle.Screen()
screen.title("US. States Game")

image = "blank_states_img.gif"
# TODO This line is used for adding image file
screen.addshape(image)
turtle.shape(image)
# screen.setup(width=900, height=580)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    text_popup = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What is another state name?").title()
    print(text_popup)
    if text_popup == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break
    if text_popup in all_states:
        guessed_states.append(text_popup)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        h_state = data[data.state == text_popup]
        t.goto(int(h_state.x), int(h_state.y))
        t.write(text_popup)


# screen.exitonclick()
# TODO this function is used to get the x,y coordinates on python turtle map
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


