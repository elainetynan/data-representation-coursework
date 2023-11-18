from studentDAO import studentDAO

#create
latestid = studentDAO.create(('mark', 45))

# find by id
result = studentDAO.findByID(latestid);
print ("test create and find by id")
print (result)
print ("~~~~~~~~~~~~~~~~~~~~~~~")

#update
studentDAO.update(('Fred',21,latestid))
result = studentDAO.findByID(latestid);
print("test update")
print (result)
print ("~~~~~~~~~~~~~~~~~~~~~~~")

# get all 
print("test get all")
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)
print ("~~~~~~~~~~~~~~~~~~~~~~~")

# delete
print("test delete")
studentDAO.delete(latestid)
allStudents = studentDAO.getAll()
for student in allStudents:
  print(student)
print ("~~~~~~~~~~~~~~~~~~~~~~~")