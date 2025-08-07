s = "Rainbow has seven colors"

print(s.capitalize())   #first letter capital
print(s.casefold())     #whole string lowercase
   
print(s.count("o"))     #counts number of times a specified value occurs in a string
print(s.find("has"))    #Searches the string for a specified value and returns the position of where it was found

print(s.endswith("colors")) #Returns true if the string ends with the specified value
print(s.index("color"))     #	Searches the string for a specified value and returns the position of where it was found

print(s.format("has"))      #Formats specified values in a string
print(s.replace("has" , "is")) #Returns a string where a specified value is replaced with a specified value

print(s.split())            #Splits the string at the specified separator, and returns a list
print(s.swapcase())         #upper to lower & upper to lower

print(s.upper())            #upper case
print(s.lower())            #lower case

print(s.isalpha())
print(s.isdigit())

print(s.splitlines())       #breaks the lines into list