import urllib.request
import urllib.parse
#define a function
def myFunction():
    print("Hey There")
myFunction() #funcftion call

def myFunction2(arg):
    return arg*2
print(myFunction2(4)) #funcftion call

# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://www.sap.com/community.html')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)
result = urllib.parse(data)
print (result)