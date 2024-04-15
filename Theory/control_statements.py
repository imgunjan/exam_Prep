# Control statemet are those statement which are used to control the flow of the Program
# If Elif Else are the example of the control satement
# For while loop are also control statement

age = 18
if age >= 18:
    print("You are adult")
else:
    print("You are minor")


list1 = [5, 6, 2, 3, 8, 9, 6]
for i in list1:
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1


for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
