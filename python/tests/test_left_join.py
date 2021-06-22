from challenges.left_join.left_join import *


def test():
    hash1 = Hashmap(1024)
    hash2 = Hashmap(1024)
    hash1.add("manar", "student")
    hash1.add("Noor", "female")
    hash1.add("Abed", "26")
    hash1.add("Tala", "math")
    hash2.add("manar", "programmer")
    hash2.add("Noor", "beauty")
    hash2.add("Abed", "190.5cm")
    hash2.add("Farah", "TA")

    actual = left_join(hash1, hash2).__str__()
    expected = "Tala: ['math', None] -> Noor: ['female', 'beauty'] -> Abed: ['26', '190.5cm'] -> manar: ['student', 'programmer']"
    assert expected == actual


def test1():
    hash1 = Hashmap(1024)
    hash2 = Hashmap(1024)
    hash2.add("manar", "programmer")
    hash2.add("Noor", "beauty")
    hash2.add("Abed", "190.5cm")
    hash2.add("Farah", "TA")

    actual = left_join(hash1, hash2).__str__()
    expected = ""

    assert expected == actual
