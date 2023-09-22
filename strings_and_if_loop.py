name = "Georgia" #string variable
age = 52 #integer variable
hair_color = "brown" #string variable

print(name) #repeated function

s = "hi"
print(s[1]) #i selecting indexed items
print(len(s)) #2
print(s + ' there')

if time_hour >= 0 and time_hour <=24: # if it's anytime during the day
    print('Suggesting a drink option...') #suggest different drinks
    if mood == 'sleepy' and time_hour < 10: #10 am or earlier = coffee
        print('coffee')
    elif mood == 'thirsty' or time_hour < 2: #between 10 and 2 --> lemonade
        print('lemonade')
    else:
        print('water') #2 and midnight --> water