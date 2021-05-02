# my_list =[1,2,3,4,7,6]
import time


# def reverse1(my_list):
#     reversed_list = my_list[::-1]
#     return reversed_list


def reverse(my_list):
    if type(my_list) != list:
        return f"{my_list} is not a list"
    elif len(my_list) ==0:
        return 'list should not be empty'
    reverse = []
    for item in my_list:
        reverse.insert(0, item)
    return reverse


# except1 = [1]
# start = time.time()
# reverse(except1)
# end = time.time()

# print(f"Runtime of the function is {end - start}")

if __name__ == "__main__":
    riddle_index = 0
