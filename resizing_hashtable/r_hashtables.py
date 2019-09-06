# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 5381
    for x in string:
        hash = ((( hash << 5) + hash) + ord(x)) & 0xFFFFFFFF
    return hash


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if key == hash_table.storage[index].key:
            hash_table.storage[index].value = value
        else:
            current_linked_pair = hash_table.storage[index]
            while current_linked_pair.next != None:
                current_linked_pair = current_linked_pair.next
            new_linked_pair = LinkedPair(key, value)
            current_linked_pair.next = new_linked_pair
    else:
        new_linked_pair = LinkedPair(key, value)
        hash_table.storage[index] = new_linked_pair



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if hash_table.storage[index].key == key:
            hash_table.storage[index] = hash_table.storage[index].next
            return
        if hash_table.storage[index].next != None:
            current_linked_pair = hash_table[index]
            while current_linked_pair != None:
                if current_linked_pair.next.key == key:
                    current_linked_pair.next = current_linked_pair.next.next
                    return
                current_linked_pair = current_linked_pair.next
    else:
        print(f"{key} not found in hash table, cannot be removed.")


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hash_key = hash(key)
    index = hash_key % hash_table.capacity
    if hash_table.storage[index] != None:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
        if hash_table.storage[index].next != None:
            current_linked_pair = hash_table.storage[index].next
            while current_linked_pair != None:
                if current_linked_pair.key == key:
                    return current_linked_pair.value
                current_linked_pair = current_linked_pair.next
    else:
        print(f"{key} not found in hash table, cannot be removed.")


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    new_hash_table.storage = [None] * new_hash_table.capacity
    for i in range(len(hash_table.storage)):
        new_hash_table.storage[i] = hash_table.storage[i]
        hash_table.storage[i] = None
    return new_hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
        + " to " + str(new_capacity) + ".")


Testing()