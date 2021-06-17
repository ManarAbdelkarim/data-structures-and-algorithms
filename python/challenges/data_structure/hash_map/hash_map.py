from  ..linked_list.linked_list import *
class Hashmap:
    """
    this is obviously a hashmap class
    """

    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size


    def hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hashed_key = (sum *19)% self.size
        return hashed_key
    def __str__(self):
        output = []

        for i in self.map:
            if i:
                current = i.head
                while current:
                    output.append(' -> '.join(current.data))
                    current = current.next
        string_hash = ' ,'.join(output)
        return string_hash


    def add(self, key, value):
       hashed_key = self.hash(key)
       if self.contains(key):
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0]:
                    current.data[1] =  value
                current = current.next
                return self
       if not self.map[hashed_key]:
           self.map[hashed_key] = Linked_list()
       self.map[hashed_key].append([ key, value])
       return self.__str__()




    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            current = self.map[hashed_key].head
            while current:
                if key == current.data[0] :
                    return current.data[1]
                current = current.next
        return "not found"



    def contains(self, key):
        index = self.hash(key)
        if self.map[index]:
            current = self.map[index].head
            while current:
                if key == current.data[0]:
                    return True
                current = current.next
        return False


if __name__ == "__main__":
    hash_map = Hashmap()
    print(hash_map.add('Noura','she is sleepy all day'))
    hash_map.add('Noura','she is solving trees all  day')
    hash_map.add('Tala','she is eating all day')
    hash_map.add('Manar','she is studying all day')
    hash_map.add('ranaM','she is Manar but in backward')
    print(hash_map.get('Noura'))
    print(hash_map)
    print('pass')

