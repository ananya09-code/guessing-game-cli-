#guessing game manu
import random
import time 
import json
try:
       with open("score.json", "r") as file:
         high_score= json.load(file)
except FileNotFoundError:
     high_score = {
     "point": None,
     "time": None}
def save_score():
       with open("score.json", "w") as file:
        json.dump(high_score, file, indent=4)
while True:
    print(" _ _ _Welcome to the Number Guessing Game!_ _ _")
    print("I'm thinking of a number between 1 and 100")
    print("You have 5 chances to guess the correct number.")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("to exit the game inter(0)")
    if high_score["point"] is not None:
       print(f"🏆 High Score: {high_score['point']} tries in {high_score['time']} seconds!")
    else: 
        print("no high score yet!")
    choice=int(input("Enter your choice: "))
    if choice==0:
        print("exiting....")
        break
    ans=random.randint(1,100) 
    start_time=time.time()
    if choice==1:
        chances=10
        print("you have 10 chances!")
    elif choice==2:
        chances=5
        print("you have 5 chances!")
    elif choice==3:
        chances=3
        print("you have 3 chances!")
    for point in range(chances):
        guess=int(input("enter your answer: "))
        if guess==ans:
              end_time=time.time()
              gone_time=round(end_time-start_time)
              timo=point+1
              print(f"congraulaion! you got the answer in {timo} try! ")
              print(f"You took", round(gone_time),"seconds to finish the game!")
              if high_score["point"] is None:
                 high_score["point"]=timo
                 high_score["time"]=gone_time
              elif timo<high_score["point"]:
                 high_score["point"]=timo
                 high_score["time"]=gone_time
              elif timo==high_score["point"] and gone_time<high_score["time"]:
                 high_score["point"]=timo
                 high_score["time"]=gone_time
              save_score()      
              break
        
        elif guess<ans:
            print("too low!")
        elif guess>ans:
            print("too high!")
        print(f"you have {chances-point-1} chances left! ")
    else:
        print(f"Sorry, you're out of chances! The number was {ans}.")
    play_more=input("Do you want to play again? (y/n): ").lower()
    if play_more !="y":
        print("exiting....")
        break
    

    