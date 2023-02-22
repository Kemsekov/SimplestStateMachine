# this state machine recognizes sequence of three numbers

sequence=[1,4,3]
currentState = None

def stateError(number):
    return "❌\nWrong sequence!\n"+state0(number)

def state0(number):
    global currentState
    currentState = state1
    return "Enter sequence"

def state1(number):
    global currentState
    if number==sequence[0]:
        currentState=state2
        return "✔"
    else:
        return stateError(number)
    
def state2(number):
    global currentState
    if number==sequence[1]:
        currentState=state3
        return "✔"
    else:
        return stateError(number)

# this is end state
def state3(number):
    global currentState
    if number==sequence[2]:
        currentState=None
        return "✔\nDone!"
    else:
        return stateError(number)

currentState = state0
print(currentState(0))
while currentState!=None:
    number = int(input())
    print(currentState(number))

# there is a way to reduce code duplications by abstracting away 
# body of function that checks if given number is a right one from state1 to state3,
# but I decided to leave it to be this way.