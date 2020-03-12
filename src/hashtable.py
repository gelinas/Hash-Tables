# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_djb2 = 5381
        for c in key:
            hash_djb2 = (hash_djb2 * 33) + ord(c)
        return hash_djb2


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # return self._hash_djb2(key) % self.capacity
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''


        # FIRST PASS: does not overwrite keys but does insertions with singly linked list
        # index = self._hash_mod(key)
        # # if index in use, chain the LinkedPair to the last value in the chain
        # if self.storage[index]:
        #     # traverse list to tail
        #     node = self.storage[index]
        #     while node.next:
        #         node = node.next
        #     node.next = LinkedPair(key, value)
        # else:
        #     self.storage[index] = LinkedPair(key, value)

        # SECOND PASS: need to check key and overwrite if matches
        # psudeocode:
        # check index. 
        #   If there's a node, check key. 
        #       If key matches, overwrite
        #       else key does NOT match 
        #           if there's a next, check key

        # index = self._hash_mod(key)
        # if self.storage[index]:
        #     node = self.storage[index]
        #     # check first item, overwrite if matches
        #     if node.key == key:
        #         node.value = value
        #         return
        #     # if first item doesn't match, check for a next with key and repeat
        #     while node.next:
        #         if node.next.key == key:
        #             node.next.value = value
        #             return
        #         else:
        #             node = node.next
        #     # if no more node.next's, add new linked pair to end
        #     node.next = LinkedPair(key, value)
        #     return
        # # else bucket is empty, add first node
        # else:
        #     self.storage[index] = LinkedPair(key, value)
        #     return

        # THIRD PASS: single while loop
        index = self._hash_mod(key)
        # if something in bucket, check keys and overwrite if matches. Otherwise add to end
        if self.storage[index]:
            node = self.storage[index]
            while node.key:
                if node.key == key:
                    node.value = value
                    return

        # else bucket is empty, add first node
        else:
            self.storage[index] = LinkedPair(key, value)
            return



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            # traverse list to tail
            node = self.storage[index]
            while node.next:
                node = node.next
            return node.value
        else:
            print("ERROR: key not found")



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            # traverse list to tail for matching key
            node = self.storage[index]
            while node.key != key:
                node = node.next
            return node.value
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage.copy()
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        # if there is an item at a given index in old_storage, copy to the new self.storage
        for item in old_storage:
            if item is not None:
                # insert first item into new list
                node = item
                self.insert(node.key, node.value)
                # check if there are chained items and insert them as well
                while node.next:
                    self.insert(node.next.key, node.next.value)
                    node = node.next
                    



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
