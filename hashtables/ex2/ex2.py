#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Hash each ticket so the starting location is the key and the desination is the value.
    for ticket in tickets:
        print(ticket.source)
        print(ticket.destination)
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Find the n-th location in the route by checking the hashtable for the n-1th
    print(hashtable.storage)

    # print(current_ticket)

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)