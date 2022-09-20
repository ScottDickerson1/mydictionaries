person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person) #can update value; cannot update key

#print(type(person['children']))

#print(person['children'][1])    #print certain element in the list that is contained in the dictionary

#print(person['pets']['cat'])    #print a dictionary value that is associated with selected key that is contained within the parent dictionary

#for rec in person['children']:
    #print(rec)

for rec in person['pets']:
    print(rec)                  #you will get the key

print()

for rec in person['pets']:
    print(person['pets'][rec])      #will print the values
