import random

def play_game()->None:
    min = 1
    max = 10
    count = 0
    target = random.randint(min, max)
    print(target)
    print("===============guess number===============:\n")
    while(True):
        count += 1
        keyin = int(input("number range: {0}~{1}:".format(min, max)))
        if(keyin >=min and keyin <= max):
            if(keyin == target):
                print("Bingo! You're right! The number is:", target)
                print("You guessed it in ",count," times.")
                break
            elif (keyin > target):
                max = keyin
                print("Smaller")
            elif (keyin < target):
                min = keyin
                print("Greater")
            print("Yout guessed it in",count," times\n")
        else:
            print("Please enter the nunber in adequate range.")

while(True):
    play_game()
    play_again = input("Play again?(y,n):")
    if(play_again == 'n'):
        break

print("Game Over!")