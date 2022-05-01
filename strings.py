#Accessing values in strings
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#updating strings
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Benjamin')

#string formatting
print("My name is %s and weight is %d kg!" %('Benjamin', 21))

# Triple quote
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print(para_str)


name = "Benjamin Okumu"
print(name.title())

first_name = "Benjamin "
last_name = "Okumu"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())

print(f"Hello, {first_name} {last_name}")