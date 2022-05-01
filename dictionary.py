thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "Year": 1964,
    "electric": False,
    "colors": ["red", "white", "blue"]
}
print(thisdict["brand"])
print(len(thisdict))

x = thisdict["model"]
x = thisdict.get("model")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

del thisdict["model"]
thisdict.clear()

for x in thisdict.values():
  print(x)
  
  
mydict = thisdict.copy()
print(mydict)

#Nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}