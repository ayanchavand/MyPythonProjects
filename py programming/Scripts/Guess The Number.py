from random import *

print("                                                WELCOME TO GUESS THE NUMBER GAME!!!\n\n")
points = 0
how = int(input("How many times you want to play : "))
print("\n")
for _ in range(how):
   value = randint(0,5)
   a = int(input("  guess a number between 0 to 5 = "))

   if value == a:
      print("  you guessed right!!\n")
      points = points + 1
      
   else : 
      print("  sorry wrong number!!\n")

score = open("score.txt","a+")
score.write("\nyour score is " + str(points) +" out of " + str(how) + " !!")
score.close()

print("your score is " + str(points) +" out of " + str(how) + " !!") 

input(" ")
