###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_dict={}
    file_data = open(filename,'r') 
    for line in file_data:
        listed = line.split(',')
        cows_dict[listed[0]] =int(listed[1])
    file_data.close()
    return(cows_dict) 


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips=[]
    cows_cpd = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    while len(cows_cpd) > 0:
        rem_weight =10
        total_weight =0
        trip=[]
        for (name, weight) in cows_cpd.copy():
            item = (name, weight)
            if weight + total_weight <= rem_weight:
                 trip.append(name)
                 total_weight = total_weight + weight
                 cows_cpd.pop(cows_cpd.index(item))                 
        trips.append(trip)

    return(trips)
            
            

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_cpd = cows.copy()
    cows_by_names = list(cows.keys())
    result = []
    for partition in get_partitions(cows_by_names):
        weight_over_limit = False
        for trip in partition:
            weight = 0
            for cow in trip:
                weight += cows_cpd[cow]
            if weight > limit:
                weight_over_limit = True
                break
        if weight_over_limit is True:
            continue
        elif len(result)== 0 or len(partition)< len (result):
            result = partition
    return (result)
        
    # TODO: Your code here
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    filename = 'ps1_cow_data.txt'
    cows = load_cows(filename)
    # testing greedy algorithm 
    start = time.time()
    result = greedy_cow_transport(cows)
    end = time.time()
    print(f'Execution time for greedy algorithm was {end - start}.')
    print(f'Problem was solved within {len(result)} trips.')
    # testing brute force algorithm 
    start = time.time()
    result = brute_force_cow_transport(cows)
    end = time.time()
    print(f'Execution time for brute force algorithm was {end - start}.')
    print(f'Problem was solved within {len(result)} trips.')

if __name__ == '__main__':
    compare_cow_transport_algorithms()
    # TODO: Your code here
    
