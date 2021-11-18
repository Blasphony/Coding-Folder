num1 = 42
# variable declaration integer
num2 = 2.3
# variable declaration float
boolean = True
# variable declaration boolean
string = 'Hello World'
# variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# list initialize with strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# dictionary
fruit = ('blueberry', 'strawberry', 'banana')
# tuple
print(type(fruit))
# print tuple blueberry strawberry banana
print(pizza_toppings[1])
# print Sausage from pizza_toppings list
pizza_toppings.append('Mushrooms')
# add Mushrooms to pizza_toppings list
print(person['name'])
# print John from dictionary person
person['name'] = 'George'
# change person dictionary name to George
person['eye_color'] = 'blue'
# change person eye_color to blue
print(fruit[2])
# print banana from fruit tuple
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# if else condition print It's lower
if len(string) < 5:
    print("It's a short word!")
# if condition that does not print anything
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# elif condition that prints Just right!
for x in range(5):
    print(x)
# for loop that prints 0,1,2,3,4
for x in range(2,5):
    print(x)
# for loop that prints 2,3,4
for x in range(2,10,3):
    print(x)
# for loop that prints 2,5,8
x = 0
while(x < 5):
    print(x)
    x += 1
# while loop that 0,1,2,3,4
pizza_toppings.pop()
# pops off the last entry of topping
pizza_toppings.pop(1)
# pops off the second entry of topping
print(person)
# prints the dictionary person
person.pop('eye_color')
# pops off eye_color from person dictionary
print(person)
# prints person dictionary
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# print After 1st if statement 3 times
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# declare custom function print_hello_ten_times that prints hello 10 times
print_hello_ten_times()
# prints hello ten times
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
# declare custom function that prints hello zero times
print_hello_x_times(4)
# calls the function 4 times Hello
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# print hello ten times

print_hello_x_or_ten_times()
# print nothing
print_hello_x_or_ten_times(4)
# print hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)