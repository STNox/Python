import random

table = []
for i in range(11):
    row = []
    for k in range(11):
        if i == 0 or i == 10 or k == 0 or k == 10:
            row.append('-')
        else:
            mine = ['-', '*']
            row.append(random.choice(mine))
    table.append(row)
print(table)

for i in range(11):
    for k in range(11):
        print(table[i][k], end=' ')
    print()

mine = []
for i in range(1, 10):
    mine_row = []
    for k in range(1, 10):
        if table[i][k] == '*':
            mine_row.append('*')
        else:
            count = 