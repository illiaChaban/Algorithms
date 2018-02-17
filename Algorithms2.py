#algorithms 2

#######################1#####################
# #######################################
# Algorithm #1
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# #########################################


# def smallest_divisible(start_range, end_range):
#     n = 0
#     while True:
#         n += end_range - 1
#         correct = True
#         for x in range(start_range, end_range):
#             if n % x != 0:
#                 correct = False
#                 break
#         if correct:
#             break
#     return n  

# a = smallest_divisible(1,21)
# print a





# list_of_asserts = range(1, 21)
# for i in list_of_asserts:
#     assert a % i == 0, "Your code sucked at %d stage" % i

# assert a % 1234213123 == 0, "Your code sucks at %d" % 1234212123


#########################################################
##############################################
# Find the largest palindrome made from the product of two 3-digit numbers.
########################################################

# biggest_polindrom = 0
# i = 100
# for i in xrange(100, 1000):
#     for j in xrange(100, 1000):
#         if str(i * j) == str(i * j)[::-1] and i * j > biggest_polindrom:
#             biggest_polindrom = i * j 

# print biggest_polindrom

#############################
###############################   3   ######################

# for i in range(99, 0, -1):
#     if i % 7 == 0 and i % 5 == 0:
#         x = "Miller Lite"
#     elif i % 7 == 0:
#         x = "Miller"
#     elif i % 5 == 0:
#         x = "Lite beer"
#     else:
#         x = "beer"
#     print "%d Bottles of %s, take one down, pass it around, %d bottles of beer on the wall" % (i, x, i -1)

################################################# 4 #####################
#######################################

# for i in range(99, 0, -1):
#     x = 'beer'
    
#     while i % 7 == 0:
#         x = "Miller"
#         break
#     while i % 5 == 0:
#         x = "Lite beer"
#         break
#     while i % 7 == 0 and i % 5 == 0:
#         x = "Miller Lite"
#         break
#     print "%d Bottles of %s, take one down, pass it around, %d bottles of beer on the wall" % (i, x, i -1)

def beer_check(number):
    return number % 7 == 0, number % 5 == 0

beer_list = {
    (True, True): "Milter Lite",
    (True, False): 'Miller',
    (False, True): 'Lite beer',
    (False, False): 'beer'
}

for i in range(99, 0, -1):
    print "%d Bottles of %s, take one down, pass it around, %d bottles of beer on the wall" % (i, beer_list[beer_check(i)], i -1)
