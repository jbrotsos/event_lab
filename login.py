import requests
from django.http import HttpResponse
from sqlite3 import *

email = requests.POST['email']
password = requests.POST['password']

sql = "select * from users where (email ='" + email + "' and password ='" + password + "')"

cursor = connection.cursor()
cursor.execute(sql)
row = cursor.fetchone()
if row:
  loggedIn = "Logged Success"
else:
  loggedIn = "Login Failure"
        
return HttpResponse("Logged In Status:" + loggedIn)
 
