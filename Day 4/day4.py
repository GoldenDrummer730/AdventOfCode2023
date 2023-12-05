
points = 0

with open(r'Day 4\input.txt') as input:
    for line in input:
        winning_nums = list(line.split(':')[1].split('|')[0].strip().split(' '))
        winning_nums = [int(x) for x in winning_nums if x != '']
        my_nums = list(line.split(':')[1].split('|')[1].strip().split(' '))
        my_nums = [int(x) for x in my_nums if x != '']

        is_first = True
        card_total = 0
        for num in my_nums:
            try:
                if (num in winning_nums):
                    if (is_first):
                        card_total += 1
                        is_first = False
                    else:
                        card_total = card_total * 2
            except Exception as e:
                continue
        points += card_total
print(f'Part 1: {points}')

data = ''
length = 0
original_nums = []
original_draw = []
totals = {}

with open(r'Day 4\input.txt') as input:
    for line in input:
        data += line
        length += 1
        totals.update({length:1})

card = 1
for line in data.split('\n'):
    onum = list(line.split(':')[1].split('|')[0].strip().split(' '))
    original_nums = ([int(x) for x in onum if x != ''])
    odraw = list(line.split(':')[1].split('|')[1].strip().split(' '))
    original_draw = ([int(x) for x in odraw if x != ''])

    for x in range(totals.get(card)):
        matches = 0
        for d in original_draw:
            if d in original_nums:
                matches += 1
        
        for i in range(card + 1, card + matches + 1):
            if (totals.get(i) >= 0):
                totals.update({i: totals.get(i) + 1})
            else:
                totals.update({i: 0})
    # print(f'Current {card} totals: {totals}\n')
    card += 1

card_total = 0
for k,v in totals.items():
    card_total += v

print(f'Part 2: {card_total}')