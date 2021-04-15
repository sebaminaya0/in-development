"""

Project # 2

"""

import random as r

def list_duplicates_of(seq,item): # I need to find the indices of the duplicated letters inside the letters list so I search for a solution in stack overflow :)
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


def hangman():
    mode = int(input("Which play mode would you like to play?\n1)1-player mode\n2)2-players mode\n\nChoose your mode here: "))

    if mode == 2:
        word = input("Player 1 please input the word to be guessed: ")
        
        letters = list(word)
        
        print(chr(27) + "[2J")
        
        a = []
        
        for i in range(len(letters)):
            a.append("_")

        b = " ".join(a)
        
        hangmanPrint = [r"   _____ ",r"  |     | ",r"        | ",r"        | ",r"   _____|_",b]
        
        n = 0

        while n < 7:
            
            for i in range(len(hangmanPrint)):
                print(hangmanPrint[i])

            guess = input("\nPlayer 2 please input the letter guessed: ")
            
            if guess in letters:
                c = list_duplicates_of(letters,guess)
                
                for i in c:
                    a[i] = letters[i]

                b = " ".join(a)

                hangmanPrint[-1] = b

                if a == letters:
                    print("\nCongrats! You won!\n")
                    break

            else:
                n += 1
                
                if n == 1:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r"        | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 5 more chances")
                elif n == 2:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r"  |     | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 4 more chances")
                elif n == 3:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|     | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 3 more chances")
                elif n == 4:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 2 more chances")
                elif n == 5:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r" / _____|_",b]
                    print("Ups! Wrong guess... Still have 1 more chances")
                elif n == 6:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r" / \____|_",b]
                    print(f"Ups! Wrong guess... You lost :( The word was {word}")
                    for i in range(len(hangmanPrint)):
                        print(hangmanPrint[i])
                    n += 1
    else:
               
        textToData = "Lorem Ipsum simply dummy textprinting typesetting industry Lorem Ipsum industry standard dummy text when unknown printer took galley type scrambled make type specimen book survived five centuries leap into electronic typesetting remaining essentially unchanged popularised in the with the release Letraset sheets containing Lorem Ipsum passages more recently with desktop publishing software like Aldus PageMaker including versions Lorem Ipsum is long established fact that reader will be distracted by the readable content page when looking layout The point using Lorem Ipsum is that has more-or-less normal distribution letters as opposed to using Content here content here making look like readable English. Many desktop publishing packages web page editors now use Lorem Ipsum as their default model text  search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years sometimes by accident sometimes on purpose injected humour the like"

        listOfWords = textToData.split()

        word = r.choice(listOfWords)
        
        letters = list(word)
                
        a = []
        
        for i in range(len(letters)):
            a.append("_")

        b = " ".join(a)
        
        hangmanPrint = [r"   _____ ",r"  |     | ",r"        | ",r"        | ",r"   _____|_",b]
        
        n = 0

        while n < 7:
            
            for i in range(len(hangmanPrint)):
                print(hangmanPrint[i])

            guess = input("\nPlayer please input the letter guessed: ")
            
            if guess in letters:
                c = list_duplicates_of(letters,guess)
                
                for i in c:
                    a[i] = letters[i]

                b = " ".join(a)

                hangmanPrint[-1] = b

                if a == letters:
                    print("\nCongrats! You won!\n")
                    break

            else:
                n += 1
                
                if n == 1:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r"        | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 5 more chances")
                elif n == 2:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r"  |     | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 4 more chances")
                elif n == 3:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|     | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 3 more chances")
                elif n == 4:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r"   _____|_",b]
                    print("Ups! Wrong guess... Still have 2 more chances")
                elif n == 5:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r" / _____|_",b]
                    print("Ups! Wrong guess... Still have 1 more chances")
                elif n == 6:
                    hangmanPrint = [r"   _____ ",r"  |     | ",r"  O     | ",r" /|\    | ",r" / \____|_",b]
                    print(f"Ups! Wrong guess... You lost :( The word was {word}")
                    for i in range(len(hangmanPrint)):
                        print(hangmanPrint[i])
                    n += 1    
                        
hangman()

