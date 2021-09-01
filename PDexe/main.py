import turtle
import pandas as pd
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# answer_state = screen.textinput(title="Guess the state", prompt="Which state is this?r")

data_file = pd.read_csv(r"50_states.csv")
all_states = data_file.state.to_list() # You didn't know .to_list() method here, and got stuck!!
guessed_states = []
missing_states = []

while len(guessed_states) < 51:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Which state is this?").title()

    def get_mouse_click_cord(x, y):
        print(x, y)
        answer_x_cord = x
        answer_y_cord = y
        print(answer_x_cord)
        print(answer_y_cord)

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        print(missing_states)
        break




    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data_file[data_file.state == answer_state]
        print(state_data)
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())# Fetches only raw value u can swap it with answer_state tho.
        print("fck me sideways...")

    else:
        print("That's wrong try again")

turtle.onscreenclick(get_mouse_click_cord)
turtle.mainloop()
