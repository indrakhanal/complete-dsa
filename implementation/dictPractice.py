
def count_word_frequency(words):
    # TODO
    dist_ = {}
    for w in words:
        dist_[w] = w_count
        if dist_[w] == w:
            print("yess")
            w_count+=1
            # dist_[w]=w_count
            # w_count -=1
            
    return dist_
    
# print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))

def merge_dicts(dict1, dict2):
    # TODO
    merged_dict = {k:dict1.get(k, 0)+dict2.get(k,0) for k in dict1 | dict2}

    return merged_dict
                
#Alternative approach
def merge_dicts_alt(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result
            
print(merge_dicts_alt({'a': 1, 'b': 2, 'c': 3}, {'b': 3, 'c': 4, 'd': 5}))

def max_value_key(my_dict):
    # TODO
   
    highest_val = 0
    dict_u = {}
    for i in my_dict:
        if my_dict[i] > highest_val:
            dict_u = {}
            highest_val = my_dict[i]
            dict_u[i] = highest_val 
    return dict_u.get
    
    
print(max_value_key({'a': 5, 'b': 9, 'c': 10, 'd':4, 'e':45}))

def reverse_dict(my_dist):
    updated_dist = {}
    for key, value in my_dist.items():
        updated_dist[value] = key
    return updated_dist

print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)
        
