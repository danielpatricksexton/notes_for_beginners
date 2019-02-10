

# store values in a list. You can store strings, numbers, booleans etc

friends = ["Nate", "Will", "Rob", "Justin", "John"]
print(friends)          # print the array
print(friends[0])       # print nate in index position 0
print(friends[1])       # print will
print(friends[2])       # print rob
print(friends[-1])      # print john from back of list
print(friends[1:3])     # prints index pos 1 through 3
print(friends[0:])      # will access the array starting from 0
print(friends[1:])      # will access the array starting from 1
friends[1] = "Mike"     # change values in an array
print(friends[1])       # index position 1 will now print mike

# list functions

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Nate", "Will", "Rob", "Justin", "John"]

print(friends.sort())               # prints list into alphabetical and numerical order
print(friends.reverse())            # prints list backwards
print(friends.index("Justin"))      # locate an element with index
print(friends.count("Justin"))      # number of justin values

friends2 = friends.copy()
print(friends2)         # copy a list

friends.extend(lucky_numbers)
print(friends)          # extend and combine lists

friends.append("Jim")
print(friends)          # append a name to the end of the list

friends.insert(1, "Kelly")
print(friends)          # select position and add a name

friends.remove("Rob")
print(friends)          # remove an element from a list

friends.pop()
print(friends)          # pop an item off the end of the list

friends.clear()
print(friends)          # completely remove a list
