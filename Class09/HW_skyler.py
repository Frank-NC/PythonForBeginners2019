mov = ["Star wars the fourth", "Star wars the fifth", "Star wars the sixth"]
print(list(enumerate(mov)))
mov.append("Star wars the seventh")
print(list(enumerate(mov)))
mov.pop(0)
print(list(enumerate(mov)))
mov.reverse()
print(list(enumerate(mov)))
color_list = ["Red","Green","White" ,"Black", "Blue", "Grey", "Orange"]
print(color_list[0], color_list[-1])
fruits = {"papaya", "dragon fruit", "star fruit", "apple"}
bad_fruits = {"apple", "peach", "orange", "banana"}
print(fruits.intersection(bad_fruits))
print(fruits.difference(bad_fruits))
schlop = {"USA" : "Washington DC", "China" : "Beijing", "UK" : "London", "France" : "Paris", "Spain" : "Madrid"}
print(schlop.items())
print(schlop.values())
schlop["Italy"] = "Rome"
print(schlop["Italy"])
print("China" in schlop)
print("Shanghai" in schlop)
peopleDict = {'Ralph Williams' : 'Football',
'Michael Tippett' : 'Basketball',
'Edward Elgar' : 'Baseball',
'Rebecca Clarke' : 'Netball',
'Ethel Smyth' : 'Badminton',
'Frank Bridge' : 'Rugby'}
peopleDict["Ethel Smyth"] = "Tennis"
print(peopleDict["Ethel Smyth"])
print(peopleDict.items())
print(peopleDict.values())