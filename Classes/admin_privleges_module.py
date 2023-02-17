#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
from user_module import User

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
       
        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=["can delete post", 'Can ban post', "can add post", 'can add users']):
        self.privileges = privileges
       

    def  show_privileges(self):
        print(f"these are the privileges an admin has over other users  ")
        for i in self.privileges:
            print("He ",i)


