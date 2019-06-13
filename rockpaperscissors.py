from random import randint



def user_choice():
    user = input('Which one will you choose? ').lower()
    usernum = 0
    if user == 'rock':
        usernum = 1
    elif user == 'paper':
        usernum = 2
    elif user == 'scissors':
        usernum = 3
    elif user == 'score':
        score()
    else:
        user_choice()
    return usernum

def computer_choice():
    randomchoice = randint(1,3)
    return randomchoice

def compare(user, computer):
    if computer == user:
        return 'Draw'
    if abs(computer - user) == 1:
        if computer > user:
            return 'Computer'
        else:
            return 'User'
    if abs(computer - user) == 2:
        if computer > user:
            return 'User'
        else:
            return 'Computer'

def outcome(comparednums, computer, user):
    rps = {1:'rock', 2:'paper', 3:'scissors'}
    print('User played ' + rps[user])
    print('Computer played ' + rps[computer])
    if comparednums == 'Draw':
        print('It was a draw.')
    else:
        print(comparednums + ' won.')

def score():
    pass

def main():
    print('Rock paper scissors game')
    print('---')
    user = user_choice()
    computer = computer_choice()
    comparednums = compare(user, computer)
    outcome(comparednums, computer, user)

main()

