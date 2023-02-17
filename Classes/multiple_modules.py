#9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 

from admin_privleges_module import Admin
from user_module import User

#In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly
me = Admin('Haru', "Ilya")
me.privileges.show_privileges()