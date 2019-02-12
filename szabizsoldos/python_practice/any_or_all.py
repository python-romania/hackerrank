def is_palindromic(input_nums):
    palindromic = 0
    if all(i >= 0 for i in input_nums):
        for num in input_nums:
            reversed_num = int(str(num)[::-1])
            if reversed_num == num:
                palindromic += 1
        if palindromic > 0:
            return True
        else:
            return False
    else:
        return False


elements = int(6)
nums = "1 2 3 4 5 -9"
int_nums = list(map(int, nums.split()))

print(is_palindromic(int_nums))
