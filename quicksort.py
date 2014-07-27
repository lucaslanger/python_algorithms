from random import randint

comparison_count = 0
test_type = 0

def quickSort(intArray, start, end):
    
    global comparison_count

    if end - start < 2:
        return intArray
    
    pivot_index = choosePivot(intArray, start, end)
    
    p_array, piv_new_index = partitionArray(intArray, pivot_index, start, end)
    
    comparison_count += end - start - 1

    quickSort(p_array, start, piv_new_index)
    

    quickSort(p_array, piv_new_index + 1, end)
    
    return p_array

def partitionArray(p_array, pivot_index, start, end):
    swap(p_array, start, pivot_index) # swap pivot with beggining of array

    j = 0
    pivot_value = int(p_array[start])

    #print "TEST " + str(p_array ), start, end
    for i in range(start+1,end):
        if p_array[i] < pivot_value:
            #print "****"
            swap(p_array, i, start + j+1)
            j+= 1

  
    
    swap(p_array, start, start + j) #j has already been swapped, p_array[j] is therefore smaller than pivot
    #print "PARTITION RESULT " + str(p_array), j

    return p_array, start + j

def choosePivot(intArray, start, end):
    if test_type == 0:
        return start
    elif test_type == 1:
        return end -1
    elif test_type == 2:
        mid = (end-start-1)/2 + start
        
        a = intArray[ mid]
        b = intArray[ start]
        c = intArray[ end-1]

        if (a==b or a==c or b==c) and end-start-1>3 :
            print "Disaster, equal elements ..."
            print a,b,c, end-start-1

        val = sorted([a,b,c])[1]
        if val ==a:
            return mid
        elif val ==b:
            return start
        elif val ==c:
            return end-1

'''
        agb = a>b
        agc = a>c
        bgc = b>c
        if (agb and agc==False) or (agc and agb ==False):
            return mid
        elif (agb and bgc) or (bgc==False and agb==False):
            return start
        else:
            return end - 1

'''

        

            
            
            
    

def swap(array, first_ind, second_ind):
    temp = array[first_ind]
    array[first_ind] = array[second_ind]
    array[second_ind] = temp # moves pivot to first slot

def makeLargeTest(size, rng):
    keys = {}
    array = []

    for i in range(size):
        r = randint(1, rng)
        while r in keys == True:
            r = randint(1, rng)
        array.append(r)
        keys[r] = True
    return array

def test():
    global test_type
    global comparison_count

    t_array = [3,8,2,5,1,4,7,6]

    t2_array = makeLargeTest(200, 10e5)

    with open("QuickSort.txt", "r") as f:
        
        file_a = [int( l.strip("\n") ) for l in f.readlines()]
        print "Printing first and last 10 lines:"
        print file_a[:10]
        print file_a[-10:]
        print "Done ..."
        print ""
        
        for i in range(3):
        
            s = quickSort(file_a[:], 0, len(file_a) )
            assert( sorted(file_a) == s)
            print "Test Case " + str(test_type) + " Number of Comparisons: " + str(comparison_count)
            test_type += 1
            comparison_count = 0
    #test_type = 2
   # print choosePivot([1,1,1,1,1,8,2,4,5,7,1], 5, 6+5)

def test_partition():
    with open("test_file_10_example_0.txt", "r") as f:
            
        file_a = [int(l.strip("\n")) for l in f.readlines()]

    print partitionArray(file_a, 0,0, len(file_a))

test()
