import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="", # Usrname on computer
  #passwd="password" # for my computer
)

cursor = db.cursor()

cursor.execute("create DATABASE datarepresentation")

db.close()
cursor.close()