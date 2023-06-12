import random

print("Welcome to Richard's Word Game")
print("We are gonna play hangman")
gamerun = True
endgame = 0
alreadyguessed = []
wrongguesses = []
wrongcount = 0

words = ["snake", "book", "python", "words", "game"]
result = random.choice(words)
result_split = [*result]

def displayguessed():
    total_correct_letters = 0
    displaystring = ""
    for i in result_split:
        if i in alreadyguessed:
            displaystring += i
            displaystring += ' '
            total_correct_letters += 1
        else:
            displaystring += '_'
            displaystring += ' '
    return displaystring, total_correct_letters

def displayhangman(failcount):
    match failcount:
        case 1:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |                               |
            |       |                               |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
            
        case 2:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |           |                   |
            |       |                               |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        case 3:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |         --|                   |
            |       |                               |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        case 4:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |         --|--                 |
            |       |                               |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        case 5:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |         --|--                 |
            |       |          /                    |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        case 6:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |           O                   |
            |       |         --|--                 |
            |       |          / \                  |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        case default:
            print('''
            =========================================
            |       __        ___          __       |
            | |__| |__| |\ | | __  |\  /| |__| |\ | |
            | |  | |  | | \| |___| | \/ | |  | | \| |
            |       -------------                   |
            |       |           |                   |
            |       |                               |
            |       |                               |
            |       |                               |
            |       |                               |
            |       _________________               |
            ''')
            print(f"            |               {displayguessed()[0]}")
            print("             =========================================\n")
        
                

while gamerun:
    
    print(f"        Wrong letters: {(''.join(wrongguesses))}")
    displayhangman(wrongcount)
    
    guess = input("Guess a letter\n")
    
    if len(guess) > 1:
        print("You can only guess one letter at a time!")
    else:
        guess = guess.lower()
        if guess in alreadyguessed:
            print("You already guessed that letter!")
        elif guess in result_split:
            print(f"{guess} is in the word!\n")
            alreadyguessed.append(guess)
            # print(displayguessed()[1])
            # print(len(result_split))
            # print(displayguessed())
            if displayguessed()[1] == len(result_split):
                endgame = 0
                gamerun = False
        else:
            print(f"{guess} is not in the word!")
            wrongguesses.append(guess)
            wrongcount += 1
            if wrongcount == 6:
                endgame = 1
                gamerun = False
    
print(f"        Wrong letters: {(''.join(wrongguesses))}")
displayhangman(wrongcount)
if endgame == 0:
    print("YOU WIN")
else:
    print("YOU LOST")
print(f"The word was {result}")