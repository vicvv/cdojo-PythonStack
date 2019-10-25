import os
import shutil

# the path below is the path to your flask files that you want to have in your folders
# please name them as so: server.py. index.html, and of course add mysqlconnection.py
# you need to prepopulate server.py and index.html with data
# for example put html5 and bootstrap links into your index.html

mytemplatesfiles = "/Users/vicky/Desktop/DOJO_all/python_stack/flask/flask_templates/template"
projname = input("what is your project name? ")
where = input("where do you want to create it?")
if not where:
    where = '.'

dirName = where + '/' + projname + '/templates'
dirName2 = where + '/' + projname + '/static'
    
    # Create target directory & all intermediate directories if don't exists
try:
    os.makedirs(dirName)    
    print("Directory " , dirName ,  " Created ")
    os.makedirs(dirName2)    
    print("Directory " , dirName2 ,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
    print("Directory " , dirName2 ,  " already exists")   
    


newPath = shutil.copy(mytemplatesfiles + '/index.html', dirName)
newPath = shutil.copy(mytemplatesfiles + '/server.py', where + '/' + projname)
newPath = shutil.copy(mytemplatesfiles + '/mysqlconnection.py', where + '/' + projname)