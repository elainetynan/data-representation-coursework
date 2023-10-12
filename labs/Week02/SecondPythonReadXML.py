from xml.dom.minidom import parse
filename = "company.xml"

# read file in 2 ways
doc = parse(filename)

# or

#with open(filename) as fp:
#   doc.parse(fp)

# Check it works
print(doc.toprettyxml(), end='')

################
# Not working!!!