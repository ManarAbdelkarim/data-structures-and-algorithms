from challenges.Insertion_sort.insertion_sort import ins_sort


def test_Reverse():
    Reverse_sorted = [20,18,12,8,5,-2]
    actual = ins_sort(Reverse_sorted)

    expect= [-2, 5, 8, 12, 18, 20]
    assert actual == expect

def test_uniques():
    Few_uniques = [5,12,7,5,5,7]
    actual = ins_sort(Few_uniques)

    expect=[5, 5, 5, 7, 7, 12]
    assert actual == expect

def test_Nearly():
    Nearly_sorted= [2,3,5,7,13,11]

    actual = ins_sort(Nearly_sorted)

    expect= [2, 3, 5, 7, 11, 13]
    assert actual == expect
