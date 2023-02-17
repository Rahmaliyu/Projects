from user_module import User

class User:

    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"user's first name is {self.first_name} , and his last name is {self.last_name} ")

    def greet_user(self):
        print(f"Hello there {self.first_name}  {self.last_name} . How are you doing")        
        
class Privileges(User):
    def __init__(self,privileges=["can delete post", 'Can ban post', "can add post", 'can add users']):
        self.privileges = privileges


    def  show_privileges(self):
        print(f"these are the privileges an admin has over other users  ")
        for i in self.privileges:
            print("He ",i)


class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        
        self.privileges = Privileges()
 