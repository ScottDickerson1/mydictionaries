import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook)) #type lets us know what type of object we are dealing with; prints out class 'dict' because its a dictionary

phone = phonebook['Chris'] #KeyError means the key does not exist
print(phone)

print(len(phonebook)) #len gives you the length

mydictionary = dict(m=8, n=9)   #dict creates a new dictionary; m=8 and n=9 is the key-value pair
print(mydictionary)

mydict = []     #empty dictionary; can start off with empty one and add later
print(mydict)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:           #test to see if Chris is in the phonebook dictionary
    print(phonebook[name])      #print(dictionary_name[key])
else:
    print(name, 'not found')




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

#if the key exists, it will be updated; if it does not exist, it will create a new key-value pair; How you update or insert:

print(phonebook)
phonebook['Chris'] = '555-0123'     #Chris does exist in dictionary, so it updates the value in the dictionary
phonebook['Joe'] = '555-4444'       #Joe does not exsit in the dictionary, so it creates a new key-value pair
print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris']      #if key does not exist, it will give you a KeyError
#print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:       #default to iterate through a dictionary is iterating through the keys; default option is automaticcaly iterating through keys
    print(key)              
    print(phonebook[key])   #print out the values

for value in phonebook.values():    #.values() is for iterating through the values
    print(value)

for k,v in phonebook.items():   #.items(): method can iterate through everything; both key and value; 
    print('key:', k, '  value: ', v)    


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


#get allows us to get a specific value from our dictionary
#the difference is you can avoid the key-value error; get method does not break if key is not there

phone = phonebook.get('Chris', 'key not found')
print(phone)

#phonebook.clear()   
#print(phonebook)



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

#remove key-value pair from the dictionary

#remove = phonebook.pop()('Chris', 'key not found')  #pop method puts the value into the variable
#print(remove)                                       
#print(phonebook)




print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#you get both key-value pair and its supposed to be random; random key-value pair

#a = phonebook.popitem()     #random key-value pair so you dont have to provide a key
#print(a)
#print(phonebook)            




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)  #list function to convert dictionary into list; 
print(list_of_keys)             #creates a list of ONLY the keys; 
random_key = random.choice(list_of_keys)
print(random_key)
print(phonebook[random_key])        #gets value for the random key


print(phonebook[random.choice(list(phonebook))])        #doing above in only one lineS

print()
print('*****  end section 9 ********')
print()








