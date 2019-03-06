# STEP 1: Get the input
nr_of_elements = int(input())
set_elements = set(map(int, input().split()))
nr_of_commands = int(input())
supported_commands = ['pop', 'remove', 'discard',]
input_com = [ input() for i in range(nr_of_commands)]

# STEP 2: Execute commands
for i in range(nr_of_commands):
    com = input_com[i].split()
    if len(com) <= 1:
        eval(f'set_elements.{com[0]}()')
    else:
        eval(f'set_elements.{com[0]}({com[1]})')

print(sum(set_elements))
