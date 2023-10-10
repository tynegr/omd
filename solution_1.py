def max_even_sum(numbers: list) -> int:
    ans = 0
    odd_min = float('inf')
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            ans += num
        else:
            odd_sum += num
            odd_min = min(num, odd_min)

    if odd_sum % 2 != 0:
        ans -= odd_min

    return ans + odd_sum


def main():
    numbers = [int(x) for x in input().split()]
    result = max_even_sum(numbers)
    print(result)


if __name__ == '__main__':
    main()
