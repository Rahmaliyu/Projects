
#9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters.


from random import choice

Random_nos= [1,2,3,4,5,6,7,88,99,20,'x', 'y', 'v','z']
ticket =[]
for i in Random_nos:
    wins= choice(Random_nos)
    # Randomly select four numbers or letters from the list and
    if len(ticket) < 4:
        ticket.append(wins)
# print a message saying that any ticket matching these four numbers or letters wins aprize.
print("Any ticket matching these four numbers or letters wins a prize ", ticket)    
        



