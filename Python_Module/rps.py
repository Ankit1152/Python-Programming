import random
l = ["Rock","Paper","Scissor"]

while True:
    uc = int(input('''
Game Start 
1 Yes
2 No | Exit    
    
    '''))
    ucount = 0
    Ccount = 0
    if uc == 1:
        for a in range(1,6):
            userInput = int(input('''
1 Rock
2 Paper
3 Scissor            
            
            '''))

            if userInput == 1:
                uchoice = "Rock"
            elif userInput == 2:
                uchoice = "Paper"
            elif userInput == 3:
                uchoice = "Scissor"

            Cchoice = random.choice(l)

            if uchoice == Cchoice:
                print("Computer Choice ",Cchoice)
                print("User Choice ",uchoice)
                print("Game Tie...")
                ucount = ucount+1
                Ccount = Ccount+1

            elif(uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Computer Choice ",Cchoice)
                print("User Choice ",uchoice)
                print("You Win")  
                ucount = ucount + 1

            else:
                print("Computer Choice ",Cchoice)
                print("User Choice ",uchoice)
                print("Computer Win")   
                Ccount = Ccount+1
        
        if ucount == Ccount:
            print("Final Game is Tie...")
            print("Computer's Score ",Ccount)
            print("Your Score ",ucount)
        elif ucount > Ccount:
            print("You win the Final Game")
            print("Computer's Score ",Ccount)
            print("Your Score ",ucount)
        else:
            print("Computer wins the Final Game")
            print("Computer's Score ",Ccount)
            print("Your Score ",ucount)
    else:
        break