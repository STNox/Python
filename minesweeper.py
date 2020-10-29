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
            count = (table[i-1][k-1] == '*') + (table[i-1][k] == '*') + (table[i-1][k+1] == '*') + (table[i][k-1] == '*') \
                  + (table[i][k+1] == '*') + (table[i+1][k-1] == '*') + (table[i+1][k] == '*') + (table[i+1][k+1] == '*')
            mine_row.append(str(count))
    mine.append(mine_row)

for i in range(9):
    for k in range(9):
        print(mine[i][k], end=' ')
    print()