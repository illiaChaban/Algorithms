# Lunar Cycles
# The moon goes through phases because it orbits
#  the earth and the sun hits it differently at 
# different places in its orbit. This means that, 
# depending on where it is in its orbit, you might 
# see a full moon, right quarter moon, or even "no" 
# moon (new moon) at all. It takes 27.3 days for the 
# moon to orbit the Earth, but the actual phase difference
#  from one full moon to the next is 29.5 days because 
# the earth cruises a cool 45 million miles around the sun
#  in that 27.3 days. It takes 2.2 days for the the moon 
# to make up for that distance and get all the way back 
# to where you last saw a full moon.

# Whenever the moon is full twice in one month, the second
#  one is called a "blue moon." This last happened in July
#  of 2015 on the 1st and 31st. The next time is January of
#  2018 (same days). You can research the timing, otherwise
#  you can assume midnight. Write a program that determines
#  how many "blue moons" there will be in third milenia (2000-2999)?

# If you want to be really, really specific, the lunar month is actually 29 days, 12 hours, and 44 minutes.

#create a dictionary of years and full moons
# 21 of junuary = first full moon of 2000

# list_moon = [start + x*29.5 for x in range(0,14) if start + x*29 < 366]


# Month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Leap_month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# month_ranges = [0]
# for i in Month_days:
#     month_ranges.append(month_ranges[-1] + i)

# leap_month_ranges = [0]
# for i in Leap_month_days:
#     leap_month_ranges.append(leap_month_ranges[-1] + i)

# leap_years = [x for x in range(2000, 3000, 4)]

# Dic_full_moon = {}


# year = 2000
# count = 0
# x = 0

# while year < 3000:
#     full_moon_list = []
    
#     while True:
        
#         if x <=29:    
#             if year == 2000:
#                 starting_day = 21
#                 full_moon_list.append(starting_day)
#             else: 
#                 full_moon_list.append(x)

#         x += 29.53055555555555555
#         if year in leap_years:
#             if x > 366:
#                 x = x % 366
#                 break
#         else:
#             if x > 365: 
#                 x =x  % 365
#                 break   
        
#         full_moon_list.append(x)


#     for i in range(0, len(full_moon_list) - 1):
#         if year in leap_years:
#             ranges = leap_month_ranges
#         else:
#             ranges = month_ranges
#         for j in range(0, len(ranges) - 1):
#             if ranges[j]<full_moon_list[i]<=ranges[j+1] and ranges[j]<full_moon_list[i+1]<=ranges[j+1]:
#                 count +=1

#     year +=1

# print count
###############################################################
# Credit Card Validator
# Write a Python program to validate that a credit card number:

# It must have 16 digits, unless it starts with 37 or 34. Then, and only then, it MUST have 15 digits
# It must start with one of the folliowing. Print off "valid" and the type of card
# 6011 = Discover Card
# 37 or 34 = American Express
# 4 = Visa
# 50-55 = MasterCard
####################################################

# def validate(card_number):
#     string_card = str(card_number)
#     master_card = [str(x) for x in range(50, 56)]
#     if (string_card[0:2] == '37' or string_card[0:2] == '34') and len(string_card) == 15:
#         type_of_card = 'American Express'
#     elif len(string_card) == 16:
#         if string_card[0:4] == '6011':
#             type_of_card = "Discover Card"
#         if string_card[0] == '4':
#             type_of_card = 'Visa'
#         if string_card[0:2] in master_card:
#             type_of_card = "MasterCard"
#         else:
#             return 'not valid'

        
#     else:
#         return 'not valid'
#     return 'valid ' + type_of_card


# print validate(376959483829384)
############################################
# Case Converter
# Case Convert

# Write a function caseConvert that accepts two arguments. The first is a string, 
# the second is type. If the type is "camelcase" then convert the string to camelcase
#  (each word except the first is capitalized, no spaces). If type is "snakecase" 
#  then convert the string to snakecase (each word is separated by a - and all lowercase).
#   As a bonus, accept a string or an array. If it's an array, use .join and proceed accordingly.



def caseConvert(string, conversionType):
    convertedStr = string
    convertedStr = convertedStr.split(' ')
    
    if conversionType == 'camelcase':
        
        
        
        # for word in convertedStr:
        #     word = word.capitalize()
        for i in range(len(convertedStr)):
            convertedStr[i] = convertedStr[i].capitalize()
        print convertedStr
        convertedStr = ''.join(convertedStr)
        
    elif conversionType == 'snakecase':
        convertedStr = '-'.join(convertedStr)
    

        

    return convertedStr


x = 'hello world how are you'
y = 'camelcase'
z = 'snakecase'

print caseConvert(x, z)

