from xml.dom.minidom import parse

filename = "employees.xml"

# read file in 2 ways
doc = parse(filename)

# or

#with open(filename) as fp:
#   doc.parse(fp)

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList))
for employeeNode in employeeNodeList:
        firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
        firstName = firstNameNode.firstChild.nodeValue.strip()
        print(firstName)