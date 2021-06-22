from challenges.data_structure.hash_map.hash_map import *

def left_join(hash1,hash2):
    hash_map = Hashmap()
    for key in hash1.map :
        if key :
            hash_map.add(key.head.data[0], [key.head.data[1],None])
    for key in hash2.map :
        if key :
            if hash_map.contains(key.head.data[0]):
                hash_map.add(key.head.data[0], [hash1.get(key.head.data[0]),key.head.data[1]])
    return hash_map


if __name__ == "__main__":
    hash1=Hashmap(1024)
    hash2=Hashmap(1024)
    hash1.add('manar','student')
    hash1.add('Noor','female')
    hash1.add('Abed','26')
    hash1.add('Tala','math')
    hash2.add('manar','programmer')
    hash2.add('Noor','beauty')
    hash2.add('Abed','190.5cm')
    hash2.add('Farah','TA')

    print(left_join(hash1, hash2))
