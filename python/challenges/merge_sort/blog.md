1. In the first pass we evaluate if the length of the list is greater than 1
then we assign every half of the list to variables left and right  and we keep calling the function and divide the left and right until every list will have 1 element (the length is one)

[8,20,18,12,5,-2] -> [8,20,18] [12,5,-2] -> [8,20][18][12,5][-2]->[8][20][18]...[12][5][-2]

2. in the second pass we merge the the left and right lists in order "sorted" way .

    [8]                      [12]

  [8,20]                    [5,12]

[8,18,20 ]                [-2,5,12 ]

       [-2,5,8,12,18,20]
