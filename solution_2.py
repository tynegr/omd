def max_div3_sum(numbers: list) -> int:
    max_sum_mod0 = 0
    max_sum_mod1 = float('-inf')
    max_sum_mod2 = float('-inf')

    for num in numbers:
        if num % 3 == 0:
            max_sum_mod0 += num
            if max_sum_mod1 != float('-inf'):
                max_sum_mod1 += num
            if max_sum_mod2 != float('-inf'):
                max_sum_mod2 += num
        elif num % 3 == 1:
            new_sum_mod0 = max(max_sum_mod0, max_sum_mod2 + num)
            new_sum_mod1 = max(max_sum_mod1, max_sum_mod0 + num)
            new_sum_mod2 = max(max_sum_mod2, max_sum_mod1 + num)
            max_sum_mod0, max_sum_mod1, max_sum_mod2 = new_sum_mod0, new_sum_mod1, new_sum_mod2
        elif num % 3 == 2:
            new_sum_mod0 = max(max_sum_mod0, max_sum_mod1 + num)
            new_sum_mod1 = max(max_sum_mod1, max_sum_mod2 + num)
            new_sum_mod2 = max(max_sum_mod2, max_sum_mod0 + num)
            max_sum_mod0, max_sum_mod1, max_sum_mod2 = new_sum_mod0, new_sum_mod1, new_sum_mod2

    return max_sum_mod0

def solution():
    numbers = [int(x) for x in input().split()]
    result = max_div3_sum(numbers)
    print(result)

if __name__ == '__main__':
    solution()
