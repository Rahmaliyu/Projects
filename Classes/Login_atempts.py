




class User:

    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name
        # Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162).
        self.login_attempts = 0

    def describe_user(self):
        print(f"user's first name is {self.first_name} , and his last name is {self.last_name} ")

    def greet_user(self):
        print(f"Hello there {self.first_name}  {self.last_name} . How are you doing")        

#Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
    def    increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name}  {self.last_name} has attempted to login {self.login_attempts} times")

#Write another method called reset_login_attempts() that resets the value of login_attempts to 0.        
    def reset_login_attempts(self):
        self.login_attempts=0
    



user = User('Kande', 'Ibro')
#Make an instance of the User class and call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

user.reset_login_attempts()
print("The number of login attempts is now " ,user.login_attempts)