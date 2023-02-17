
#9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. \
#Make a list or tuple called my_ticket.
#Write a loop that keeps pulling numbers until your ticket wins. 
#Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice



def lottery_analysis(Random_nos,ticket,other_ticket):
    plays = 0
    tries = []
    while ticket != other_ticket:
        
        for i in Random_nos:
            wins= choice(Random_nos)
            if len(other_ticket) < 4:
                other_ticket.append(wins)
        plays +=1
        print(other_ticket)
    else:
      return('you have won after{plays} tries')       
     


Random_nos= [1,2,3,4,5,6,7,88,99,20,'x', 'y', 'v','z']
ticket =['v', 88, 99, 'x']
other_ticket= []
plays = 0
lottery_analysis(Random_nos,ticket,other_ticket)