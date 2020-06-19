def ans(n,sum,div):
    if n == 0:
        if sum % div == 0:
            return "Yes"
        return "No"
    return ans(n//10, sum + (n % 10), div)

x = int(input())

print(ans(x, 0, (x % 10)))