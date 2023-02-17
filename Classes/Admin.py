#9-7. Admin: An administrator is a special kind of user. 



class User:

    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"user's first name is {self.first_name} , and his last name is {self.last_name} ")

    def greet_user(self):
        print(f"Hello there {self.first_name}  {self.last_name} . How are you doing")        
        


#Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
#Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.

        self.privileges= ["can delete post", 'Can ban post', "can add post", 'can add users']

#Write a method called show_privileges() that lists the administrator’s set of privileges.
    def  show_privileges(self):
        print(f"these are the privileges an {self.first_name} {self.last_name} has over other users is that ")
        for i in self.privileges:
            print("He ",i)



Administrator = Admin('Sallau', 'Musa')
#Create an instance of Admin, and call your method.
Administrator.show_privileges()


