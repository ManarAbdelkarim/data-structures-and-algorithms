from challenges.data_structure.hash_map.hash_map import *


def left_join(hash1, hash2):
    output = []
    for key in hash1.keys():
        if key in hash2.keys():
            output.append([key, hash1[key], hash2[key]])
        else:
            output.append([key, hash1[key], "NULL"])
    return output


if __name__ == "__main__":
    hash1 = {
        "fond": "enamored",
        "wrath": "anger",
        "diligent": "employed",
        "outfit": "garb",
        "guide": "usher",
        "hello": "everyone",
    }
    hash2 = {
        "fond": "averse",
        "wrath": "delight",
        "diligent": "idle",
        "guide": "follow",
        "flow": "jam",
    }
    print(left_join(hash1, hash2))
