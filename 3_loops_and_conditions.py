#loops

#for loop with range 
for i in range(5):
    print(i)

#for each loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#for each loop with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

#while loop
count = 0
while count < 5:
    print(count)
    count += 1

#infinite loop
while True:
    print("This will run forever")
    # To stop this loop, you can use a break statement or interrupt the kernel



#conditions
if count == 5:
    print("Count is five")
elif count < 5:
    print("Count is less than five")
else:
    print("Count is greater than five")