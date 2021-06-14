def ins_sort(num_list):
    for i in range(1, len(num_list)):
        x = i - 1
        temp_list = num_list[i]

        while x >= 0 and temp_list < num_list[x]:
            print(temp_list ,num_list[i] ,  num_list[x])
            num_list[x + 1] = num_list[x]
            x -= 1
        num_list[x+1] = temp_list

    return num_list

# print(ins_sort([2,3,5,7,13,11]))

print(ins_sort([20,18,12,8,5,-2]))
# print(ins_sort([100,3,9,7,13,11]))
