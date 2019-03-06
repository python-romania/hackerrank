# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set()
for country in range(n):
    countries.add(input())

print(len(countries))

