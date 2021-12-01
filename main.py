import turtle
import pandas
screen=turtle.Screen()
screen.title('india state Name')
image='inde16.gif'
screen.addshape(image)
turtle.width(15)
turtle.shape(image)
totalstate = pandas.read_csv('statedata.csv')
guessword=[]
while len(guessword) < 50:
    ans_state=screen.textinput(title=f'{len(guessword)}/50 India State', prompt='what is another state')
    ans_state=ans_state.title()

    #data=totalstate.tolist()
    if ans_state == "Exit":
        missing_state=[]
        for state in totalstate['state'].tolist():
            if state not in guessword:
                missing_state.append(state)
        missing=pandas.DataFrame(missing_state)
        missing.to_csv('missingstate.csv')
        break
    if ans_state in totalstate['state'].tolist():
        guessword.append(ans_state)
        print(ans_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=totalstate[totalstate.state==ans_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(ans_state)

#turtle.mainloop()
screen.exitonclick()