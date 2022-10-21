import random

def parseInput(input_str):
    inputs = input_str.replace(" ", "").split(",")
    if len(inputs) == 0:
        raise ValueError("Your input has zero length.")
    
    if len(inputs) == 1:
        raise ValueError("Your input has only length 1. m must be greater than 1.")
    
    result = []
    for cur_input in inputs:
        try:
            result.append(int(cur_input))
        except ValueError:
            raise ValueError(f'This is not a real number: "{cur_input}".')

    return result

lst = []
while not lst:
    print("Please enter a list of unique integers in this format: " + \
            "1, -3, 5, 3, 60, 4")
    input_str = input("Your input: ")

    try:
        lst = parseInput(input_str)
        print()
    except Exception as error:
        print(error, "Please try again.\n")
m = len(lst)

n = 0
while n < 1:
    n_str = input("Please enter the number of times to swap, n: ")
    try:
        n = int(n_str)
        if n <= 1:
            print(f'{n} <= 1. n must be larger than 1. Please try again.\n')
    except ValueError:
        print(f'This is not an integer: "{n_str}". Please try again.\n')

print("FYI: Indices in the list start from 0 (inclusive) and end at n (exclusive)\n")

for i in range(1, n + 1):
    print("-" * 30)
    print(f"Swap Round #{i}\n")
    
    swap_index_1, swap_index_2 = random.randrange(0, m), random.randrange(0, m)
    while(swap_index_1 == swap_index_2):
        swap_index_2 = random.randrange(0, m)

    print(f"Swap indices: {swap_index_1} and {swap_index_2}")
    print(f"Current list: {lst}")
    i1, i2 = min(swap_index_1, swap_index_2), max(swap_index_1, swap_index_2)
    # TODO: fix the arrow pointing
    # print(" " * len("Current list: ") + " " * (len(str(lst[:i1])) - 1) + "^" + " " * len(str(lst[i1] - 1)) + " " * len(str(lst[i1 + 1:i2])) + "^")
    lst[swap_index_1], lst[swap_index_2] = lst[swap_index_2], lst[swap_index_1]
    print(f"Resulting list: {lst}")

    print()
