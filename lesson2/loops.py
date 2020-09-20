# for index in range(10):
#     print(index)

#indexes    0    1    2    3 
symbols = ['a', 'b', 'c', 'd']
# print(symbols[0]) # a
# print(symbols[3]) # d

# for index in symbols:
#     print(index)
# number = 20
# while number > 0:
#     print(number)
#     number -= 1

while True:
    age = int(input('Enter your age: '))
    print(age)
    playAgain = input('Do you want to play agin? (yes/no)').lower().startswith('y') 
    if not playAgain:
        break

