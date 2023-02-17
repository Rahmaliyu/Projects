#

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


class ice_cream_stand(Restaurant):
#An ice cream stand is a specific kind of restaurant.
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; just pick the one you like better. 
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.ice_cream_flavours = ['strawberry', 'Vannilla', 'chocolate']


#Write a method that displays these flavors
  def flavours(self):
    print('The ice cream has the following flavours : ')
    for i in self.ice_cream_flavours:
      print (i)


      



icecream = ice_cream_stand('Rufaidah', 'International')
icecream.describe_restaurant()
#Create an instance of IceCreamStand, and call this method.
icecream.flavours()

