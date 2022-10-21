# get value of m
m = 0
while m < 2:
    m_str = input("Please enter the number of items in the list, m: ")
    try:
        m = int(m_str)
        if m < 2:
            print(f'{m} < 2. n must be greater than or equal to 1. Please try again.\n')
    except ValueError:
        print(f'This is not an integer: "{m_str}". Please try again.\n')

# get value of n
n = 0
while n <= 1:
    n_str = input("Please enter the number of times to swap, n: ")
    try:
        n = int(n_str)
        if n <= 1:
            print(f'{n} <= 1. n must be larger than 1. Please try again.\n')
    except ValueError:
        print(f'This is not an integer: "{n_str}". Please try again.\n')


def get_num_combinations(lst, swap_times, original_lst):
    if swap_times == 0:
        return 1 if lst == original_lst else 0
    
    total = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            new_lst = lst[:]
            new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
            total += get_num_combinations(new_lst, swap_times - 1, original_lst)
    return total

lst = [ x for x in range(m) ]
print(get_num_combinations(lst, n, lst))
