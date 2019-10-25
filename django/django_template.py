import os
import shutil
from subprocess import call
activate_this = "/home/username/pythonenv/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))



projname = input("what is your project name? ")
where = input("where do you want to create it?")
if not where:
    where = '.'

call(['django-admin' 'startproject projname'])


# django-admin startproject dojo_django1;
# cd dojo_django1;


# mkdir apps; cd apps;
# python ../manage.py startapp dojo_d_app1

# cd dojo_django_app1;
# touch urls.py;


# vi dojo_django1/settings.py




# dirName = where + '/' + projname + '/templates'
# dirName2 = where + '/' + projname + '/static'
    
#     # Create target directory & all intermediate directories if don't exists
# try:
#     os.makedirs(dirName)    
#     print("Directory " , dirName ,  " Created ")
#     os.makedirs(dirName2)    
#     print("Directory " , dirName2 ,  " Created ")
# except FileExistsError:
#     print("Directory " , dirName ,  " already exists")
#     print("Directory " , dirName2 ,  " already exists")   
    


# newPath = shutil.copy(mytemplatesfiles + '/index.html', dirName)
# newPath = shutil.copy(mytemplatesfiles + '/server.py', where + '/' + projname)
# newPath = shutil.copy(mytemplatesfiles + '/mysqlconnection.py', where + '/' + projname)