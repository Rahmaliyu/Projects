#9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
#Store the classes User, Privileges, and Admin in one module. 



from privileges_module import Admin
#Create a separate file, make an Admin instance, 
admin = Admin("Rahma ",'Aliyu')
#and call show_privileges() to show that everything is working correctly
admin.privileges.show_privileges()
