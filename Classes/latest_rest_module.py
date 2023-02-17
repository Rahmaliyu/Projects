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
