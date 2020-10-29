import random

row = []
row_mod = []
for k in range(9):
        mine = ['-', '*']
        row.append(random.choice(mine))
for item in row:
    if k == 0:
        item_mod = item.replace('-', str(row[0:k+2].count('*')))
    elif k == 8:
        item_mod = item.replace('-', str(row[k-1:8].count('*')))
    else:
        item_mod = item.replace('-', str(row[k-1:k+2].count('*')))
    row_mod.append(item_mod)

print(row_mod)
