#9-1. Restaurant: Make a class called Restaurant. The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant:
 
 # A class to model a restaurant
 def __init__(self, restaurant_name, cuisine_type):
  self.rest_name = restaurant_name
  self.cuisine= cuisine_type

 def describe_restaurant(self):
  print(f" Hello ! welcome to {self.rest_name} Restaurant")
  print(f"{self.rest_name} is here to serve the best {self.cuisine} food you have ever tasted")
    

 def open_restaurant(self):
  print(f"{self.rest_name} us now open")


restaurant = Restaurant('Rahmas Kitchen', "Traditional")
print(f'Hello welcome to {restaurant.rest_name}')
print(f'In {restaurant.rest_name} we do have the best {restaurant.cuisine} cuisine')

restaurant.describe_restaurant()
restaurant.open_restaurant()








