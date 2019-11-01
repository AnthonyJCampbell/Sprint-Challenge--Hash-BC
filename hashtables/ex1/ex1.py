#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    ht = HashTable(16)
    # Loop over weights
    for i in range(length):
        # Take value and subtract it from limit to make the to_complete
        to_complete = limit - weights[i]
        # print(to_complete)

        if hash_table_retrieve(ht, to_complete) is None:
            # store weights[i] in the Hastable with a value of i
            hash_table_insert(ht, weights[i], i)
        
        else:
            answer = (str(weights[i]), str(to_complete) )
            print_answer(answer)
            return
    
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)