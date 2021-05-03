

def reverse(my_list):
    if type(my_list) != list:
        return f"{my_list} is not a list"
    elif len(my_list) ==0:
        return 'list should not be empty'
    reversed_list = my_list[::-1]
    return reversed_list


if __name__ == "__main__":
    riddle_index = 0
