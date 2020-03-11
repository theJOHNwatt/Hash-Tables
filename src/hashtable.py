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
        hash = 5381
        for c in key:
            hash = (hash*33) + ord(c)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        new_hash_index = LinkedPair(key, value)
        hash_index = self._hash_mod(key)

        if self.storage[hash_index] is not None:
            if self.storage[hash_index].key == key:
                self.storage[hash_index] = new_hash_index
                return 
            current = self.storage[hash_index]
            while current.next is not None:
                if current.key == key:
                    current = new_hash_index
                    break
                current = current.next 
            current.next = new_hash_index
        else:
            self.storage[hash_index] = new_hash_index
        

        # hash_index = self.storage[self._hash_mod(key)]
        # if hash_index == None:
        #     hash_index = LinkedPair(key, value)
        #     self.storage[self._hash_mod(key)] = hash_index            
        




    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        bucket = self._hash_mod(key)
        if self.storage[bucket] is not None:
            if self.storage[bucket].key == key:
                self.storage[bucket] = None 
                return 
            else: 
                while self.storage[bucket].key is not key and self.storage[bucket] is not None:
                    self.storage[bucket] = self.storage[bucket].next 
                self.storage[bucket] = None 
                return
        else:
            print("The key is not found")




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        bucket_index = self._hash_mod(key)
        
        if self.storage[bucket_index] is not None:
            # if the first node at the bucket is equal to the key = there is only 1 node = return value
            if self.storage[bucket_index].key == key:
                return self.storage[bucket_index].value
            # if the first node doesn't equal to the key = iterate through bucket (linked list) until you get the bucket
            else: 
                bucket = self.storage[bucket_index]
                while bucket.key is not key and bucket is not None:
                    bucket = bucket.next 
                return bucket.value
        else:
            return None 
        # return self.storage[self._hash_mod(key)].value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        temp_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket in temp_storage:
            if bucket is None:
                pass
            elif bucket.next is None: 
                self.insert(bucket.key, bucket.value)
            else:
                while bucket is not None:
                    self.insert(bucket.key, bucket.value)
                    bucket = bucket.next



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