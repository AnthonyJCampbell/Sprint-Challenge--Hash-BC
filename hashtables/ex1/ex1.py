#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # Loop over weights
        # Take value and subtract it from limit to make the to_complete

        # if ht[to_complete] is None:
            # store weights[i] in the Hastable with a value of i
        
        # else:
            answer = (weights[i], to_complete )
            print_answer(answer)
            return
    

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
