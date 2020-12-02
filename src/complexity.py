#Example of constant time code 
#'array' input could be small, or it could be large

def runs_in_constant_time(array):
    #getting an element from an array via its index
    #return array[-1]  #will get the last item in the array 
    #return array[0]
    #return array[3] 
    return array[1]

#regardless of wether this array holds ten or a million elements,
#this function will run in the same amount of time
#meaning this function is infinitely scalable or

#put another way, the time it takes to run is independent of the size
#of the input
def prints_in_constant_time(array):
    print(array[0]) #constant * constant == constant
    print(array[-1])
    print(array[3])

"""
Examples of constant time operations:

1. Accessing array elements via their index
2. Printing
3. Accessing dictionary values via their keys
4. Adding to the back of an array 
    (using the append or push methods)
5. Initializing variables/empty data structures
"""

def runs_in_linear_time_1(array):
    for i in range(n):
        print(i)

def runs_in_linear_time_2(array):
    #if array has 10 elements, we know that there will be 10 loop iterations
    #if array has 1,000,000 elements, we know that will be 1mil iterations
    # for item in array:
    #     print(item)

    # copy = []
     #linear * constant == linear
    # for item in array:
    #     copy.append(item)
    # return copy

    """
    ^ This is doing the same thing as this ->
    """
    copy = [item for item in array]
    #this is still lopping over all the array elements and  
    #adding them to the copy list
    return copy

def runs_in_quadratic_time(array):
    #linear * linear == quadratic

    #linear loop proportional to the length of 'array'
    for i in range(len(array)):
        #linear loop proportional to the length of 'array'
        for j in range(len(array)):
            print(i, j)
