#9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 




class Die:
    
    def __init__(self, sides=6):
        self.sides = sides

    #Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.    
    def roll_die(self):
        from random import randint
        return(randint(1, self.sides))

#Make a 6-sided die and roll it 10 times.  
print('After Rolling a 6 sided die 10 times')  
Sided_6 = Die()
for i in range(10):
     print (Sided_6.roll_die())

        
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print('Rolling a 10 sided die 10 times')       
Sided_10 = Die()
Sided_10.sides=10
for i in range(10):
    
    print (Sided_10.roll_die())

print('Rolling a 20 sided die 10 times')       
Sided_20 = Die()
Sided_20.sides = 20
for i in range(10):
    print (Sided_20.roll_die())