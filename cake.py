#cake problem interview
# You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.

# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

# Each type of cake has a weight and a value, stored in a tuple with two indices:

# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British shillings
# For example:

#   # weighs 7 kilograms and has a value of 160 shillings
# (7, 160)

# # weighs 3 kilograms and has a value of 90 shillings
# (3, 90)

# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

# For example:

#   cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20

# max_duffel_bag_value(cake_tuples, capacity)
# # Returns 555 (6 of the middle type of cake and 1 of the last type of cake)

# Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our algorithms flexible and comprehensive.

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20


def max_duffel_bag_value(cake_tuples, capacity):
    duffel_bag_value = 0
    cake_tuples.sort(reverse = True, key = lambda x: x[1]/x[0])
    min_weight = min([x[0] for x in cake_tuples])
    
    while capacity >= min_weight:
        for i in cake_tuples:
            if capacity >= i[0]:
                duffel_bag_value += i[1]
                capacity -= i[0]
                break
    
    return duffel_bag_value


print max_duffel_bag_value(cake_tuples, capacity)
#

