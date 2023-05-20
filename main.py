import turtle
import pandas

screen=turtle.Screen()
screen.title("India States Game")
image="india_map.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("india_states.csv")
all_states=data.state.to_list()
guessed_states=[]
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States correct", prompt="Guess a state").title()

    if answer_state=="Exit":
        missing_states= []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # check if the state is a State in the India
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
