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
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        delta_index = hash_table_retrieve(ht, limit - weight)
        if delta_index is not None:
            return (delta_index, i)


    return None
    
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)