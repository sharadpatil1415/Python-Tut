#string
a = '''hey!!! my name is sharad I am from Kolhapur!!!!'''
b = len(a) #show length
print(a) 
print(b) 
print(a[0:20]) # here we get 0th to 19th index its does not print 20th index

#Strings methods

print(a.upper()) #display characters in upper case 
print (a.lower())#display characters in lower case
print(a.capitalize())#display first character in capital
print(a.rstrip("!")) #remove THE last ! 
print(len(a))#length of the string 
print(a.center(100)) #its became cemtre within 100 characters
print(a.replace("sharad" , "samiksha")) #its replace given strings
print(a.count("a")) #counts "a"string
print(a.center(100 , ".")) #giving dots insted of black space
print(a.endswith("!")) #if its ends with given character thn its print true either false
print(a.startswith("!")) #if its start with 
print(a.find("I")) #it finds chars. and words in string
print (a.isalnum()) #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
print (a.isalpha()) # if string contains any numbers or symbole its return false

