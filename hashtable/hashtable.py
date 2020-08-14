class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
  
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.total_items = 0



    def get_num_slots(self):
        return len(self.hash_table)


    def get_load_factor(self):
        """
        number of items in hash table 
        divided by number of total slots of array
        """
        return self.total_items // self.get_num_slots()
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        return self.djb2(key) % len(self.hash_table)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        # check load factor
        if self.get_load_factor() > 0.7:
                return self.resize(self.capacity*2)
        # hash key and search linked list for key
        # if the key already exists 
            # replace the value
        # else 
            # add new HasTable Entry to the head of the linked list
            # increment counter

        node = self.find(key)
        
        if node is not None:
            self.hash_table[index].value = value
        else:
            self.insert_at_head(HashTableEntry(key, value))
            self.total_items += 1
             
    
    def find(self, key):
        index = self.hash_index(key)
        head = self.hash_table[index]

        

        while head is not None:
            if head.key == key:
                return head

            head = head.next

        return None
        

    def insert_at_head(self, node):
        index = self.hash_index(node.key)
        head = self.hash_table[index]
    
        node.next = head
        head = node


    def delete(self, key):
        # hash the key and get an index
        # search linked list for matching key
        # store value of node
        # delete that node and return value
        # decrement counter

        index = self.hash_index(key)
        node = self.hash_table[index]

        if node.key == key:
            deleted_node = node
            node = node.next
            return deleted_node

        prev = node
        node = node.next
        
        while node is not None:
            if node.key == i:
                prev.next = node.next
                self.total_items -= 1
                return node
            else:
                prev = node
                node = node.next

        return None

        

    def get(self, key):
        # hash the key and get an index
        # get the linked list at the computed index
        # search linked list for the key
        # if key exists return value
        # otherwise return None

        
        i = self.hash_index(key)
        node = self.hash_table[i]

        cur = node
        

        while cur is not None:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next

        return None
        
        
        



    def resize(self, new_capacity):
        """
        make a new array that double the original size
        Go through each linked list in array
            go through each item and rehash it
            then insert items into new index of array
        """
        new_array = [None] * new_capacity

        for head in self.hash_table:
            while head is not None:
                index = self.hash_index(head.key)
                new_array[index] = head
            self.hash_table = new_array

        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
