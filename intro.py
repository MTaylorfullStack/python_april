# variable declaration



number = 200

counter = 1

# strings and numbers

name = "Anthony"

greeting = f"Hello, greetings to {name}"

counter += number

# print(counter)

# JS: name.length

# print(len(name))

# lists



# print(students[len(students)-1])
# print(len(students))


# JS: students.push()

# students.append("Anthony")

# print(students)

# students.pop()

# print(students)




# dictionaries

ninja = {
    'language': 'python',
    'location': 'Chicago',
    'ninja_knives': 12,
    12: "Knives",
}

print(ninja['location'])

ninja['ninja_knives'] -= 2

print(ninja['ninja_knives'])

# conditionals

# if(condition){
#     //do the thing
# }

score = 50

if score > 25:
    print(f"you're score was {score} and you won the game!")
elif score > 10:
    print(f"that was a good shot, but {score} isn't going to cut it")
else:
    print(f"really? {score} was all you could do?")


# loops

# for(var i=0; i<arr.length; i++){
#     // do some things
# }

# for thing in range( start, end, increment):
#     do the thing

students = ["Ed", "Ally", "Billy", "Jason", "Jeff"]

for student in range(len(students)):
    print(students[student])

# for num in range(256):
#     print(num)

# while condition:
#     do this

for key in ninja:
    print(ninja[key])

# functions
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# function huge(){

# }

# def huge(): # no parameters
#     sum = 0
#     for num in range(500000):
#         if num%2==0:
#             print(f"This number didn't make it: {num}")
#         else:
#             sum += num
#     print(sum)
#     return sum

# huge()



# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

# given something (list of numbers)

# declaring a function, passing in list parameter
# count number of positive values
# require a counter variable
# loop through the list
    # if number is positive, increase counter
# replace last value in list with counter


def count_positives(numbers):
    counter = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            counter += 1
    numbers[len(numbers)-1] = counter

    
print(count_positives([2,5,-9,0,4,-6,-13,2])
