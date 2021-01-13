# Swaroop Lama
# Submission for sorting a list
# MLH day 3 - Sorting a list

def sorted_list(data):

    for i in range(0, len(data)-1):
        min_value = i 

        for j in range(i+1, len(data)):
            if data[j] < data[min_value]:
                min_value = j
            
        if min_value != i:
            data[min_value], data[i] = data[i], data[min_value]
        
    return data

#list to be sorted
data = [9,5,6,7,2,1,3,4,8,10]

#sorted list
print(sorted_list(data))