dict1 = {'a':1,'b':2,'c':3}
dict2 = {'d':4,'e':5,'c':4,'f':'6'}

dict3 = dict1.copy() #it will copy first dict into new dict
dict3.update(dict2) #it will overwrite the existing key values to the new values so final output will be new value for the same key
print("After merginf two dictionaries the new dictionary is:")
print(dict3)
