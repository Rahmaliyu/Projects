
#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
class User:

    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"user's first name is {self.first_name} , and his last name is {self.last_name} ")

    def greet_user(self):
        print(f"Hello there {self.first_name}  {self.last_name} . How are you doing")        
