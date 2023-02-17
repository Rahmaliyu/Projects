#9-4. Number Served: Start with your program from Exercise 9-1 (page 162).

#Create an instance called restaurant from this class. Print the number of customers the
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the numberof customers that have been served.
#  Call this method with a new number andprint the value again.
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, a
#day of business.


class Restaurant:
 
 # A class to model a restaurant
 def __init__(self, restaurant_name, cuisine_type):
  self.rest_name = restaurant_name
  self.cuisine= cuisine_type
  #Add an attribute called number_served with a default value of 0. 
  self.number_served = 1

 def describe_restaurant(self):
  print(f" Hello ! welcome to {self.rest_name} Restaurant")
  print(f"{self.rest_name} is here to serve the best {self.cuisine} food you have ever tasted")
  print(f'{self.rest_name} has served {self.number_served} customers')

 def open_restaurant(self):
  print(f"{self.rest_name} us now open")

 def set_number_served(self ):
    print(f'{self.rest_name} has served {self.number_served} customers')
 
 def increment_number_served(self,number):
    self.number_served= number
    print(f'{self.rest_name} has  now served {self.number_served} customers')

  
  

restaurant = Restaurant('Rahmas Kitchen', "Traditional")
restaurant.number_served = 3

print(f'Hello welcome to {restaurant.rest_name}')
print(f'In {restaurant.rest_name} we do have the best {restaurant.cuisine} cuisine')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(6 )
