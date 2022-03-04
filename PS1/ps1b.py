###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    if (target_weight, egg_weights) in memo:
      result = memo[(target_weight, egg_weights)]
    if egg_weights==() or target_weight == 0:
      result =(0,())
    elif egg_weights[0] > target_weight:
      result =dp_make_weight(egg_weights[1:], target_weight, memo)
    else:
      consider=egg_weights[0]
      withVal, withToTake =dp_make_weight(egg_weights, (target_weight-consider), memo)
      withVal += 1
      result = (withVal,withToTake+(consider,))
      
    return (result)
  

    
# TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    egg_weights =egg_weights[::-1]
    n = 99
    number_eggs , list_eggs = dp_make_weight(egg_weights, n)
    eggs_dict ={}
    for egg in list_eggs:
      if egg not in eggs_dict:
        eggs_dict[egg] = 1
      else:
        eggs_dict[egg] +=1
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", number_eggs, eggs_dict)
    print()
