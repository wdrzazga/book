def check_fragment(length, arr: str):
    s1 = arr[:length]
    s2 = arr[length:(length*2)]
    return s1 == s2, s1

numbers = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3]
numbers_str = "".join(map(str, numbers))

for i in range(1, 100):
    result = check_fragment(i, numbers_str)
    if result[0]:
        repetitions = 100 // i
        rest = 100 % i
        _100_elements = (result[1] * repetitions) + result[1][0:rest]
        print(_100_elements)

check_fragment(3, numbers_str)
