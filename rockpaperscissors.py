from random import randint


def user_choice(computerscore, userscore, drawscore):
    """
    Takes the user input and returns it.

    Arguments:
    - computerscore (int): How many times the computer has won.
    - userscore (int): How many times the user has won.
    - drawscore (int): How many times a draw has occured.

    Returns:
    - usernum (int): What the user chose.

    """
    user = input('Which one will you choose? ').lower()
    usernum = None
    if user == 'rock':
        usernum = 1
    elif user == 'paper':
        usernum = 2
    elif user == 'scissors':
        usernum = 3
    elif user == 'score':
        score(computerscore, userscore, drawscore)
    else:
        user_choice(computerscore, userscore, drawscore)
    return usernum

def computer_choice():
    """
    Generates the computer's choice.

    Arguments:
    None

    Returns:
    - randomchoice (int): What the computer chose.
    
    """
    randomchoice = randint(1,3)
    return randomchoice

def compare(user, computer):
    """
    Decides the result.

    Arguments:
    - user (int): What the user chose.
    - computer (int): What the computer chose.

    Returns:
    - result (str): The outcome of the game.
    
    """
    result = None
    if computer == user:
        result = 'Draw'
    if abs(computer - user) == 1:
        if computer > user:
            result = 'Computer'
        else:
            result = 'User'
    if abs(computer - user) == 2:
        if computer > user:
            result = 'User'
        else:
            result = 'Computer'
    return result

def outcome(comparednums, computer, user, computerscore, userscore, drawscore):
    """
    Prints the outcome and changes the score.

    Arguments:
    - computerscore (int): How many times the computer has won.
    - userscore (int): How many times the user has won.
    - drawscore (int): How many times a draw has occured.
    - comparednums (str): Whomst won.
    - user (int): What the user chose.
    - computer (int): What the computer chose.

    Returns:
    - computerscore (int): How many times the computer has won.
    - userscore (int): How many times the user has won.
    - drawscore (int): How many times a draw has occured.

    """
    rps = {1:'rock', 2:'paper', 3:'scissors'}
    print('User played ' + rps[user])
    print('Computer played ' + rps[computer])
    if comparednums == 'Draw':
        print('It was a draw.')
        drawscore = drawscore + 1
    elif comparednums == 'Computer':
        computerscore = computerscore + 1
        print('Computer won. ')
    else:
        print('User won. ')
        userscore = userscore + 1
    return computerscore, userscore, drawscore

def score(computerscore, userscore, drawscore):
    """
    Prints the score.

    Arguments:
    - computerscore (int): How many times the computer has won.
    - userscore (int): How many times the user has won.
    - drawscore (int): How many times a draw has occured.

    Returns:
    None

    """
    print(str(drawscore) + ' draws')
    print(str(computerscore) + ' computer wins')
    print(str(userscore) + ' user wins')

def main():
    """
    Initiates the battle.

    Arguments:
    None

    Returns:
    None

    """
    drawscore = 0
    computerscore = 0
    userscore = 0
    while True:
        print('Rock paper scissors game')
        print('---')
        user = user_choice(computerscore, userscore, drawscore)
        if user in [1, 2, 3]:
            computer = computer_choice()
            comparednums = compare(user, computer)
            computerscore, userscore, drawscore = outcome(comparednums, computer, user, computerscore, userscore, drawscore)


main()

