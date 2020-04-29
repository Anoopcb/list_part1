## Lists are data structures
### ordered collection of items
####you can store anything in lists , like int, float, string
#### and list inside a list

numbers = [1, 2, 3, 4]
print(numbers)

words = ["word1", "word2", "word3"]
print(words)

mixed = numbers + words
print(mixed)
print(mixed[::-1])
print(mixed[-1][-2])
numbers[1]= 34
print(numbers)


## adding data to lists
## methods used to add data, append(), insert() and extend()

fruits = ["grapes", "apples"]
fruits.append("mangos")
print(fruits)
fruits.insert(1, "banana")
print(fruits)
fruits1 = ["peach", "cherries"]
fruits.extend(fruits1)
print((fruits))
fruits.append(fruits1)
print(fruits)


## how to delete data from list using methods, pop() del, remove()

fruits.pop(1)
print(fruits)
del fruits[2]
print(fruits)
fruits.remove("peach")
print(fruits)

print(fruits)

fruits = ["grapes", "apples"]
if "apples" in fruits:
    print("yes, this is in the list")
else:
    print("not there")





















