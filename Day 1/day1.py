import re

sum = 0

conv = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open(r'\Day 1\input.txt') as input:
    for line in input:
        pattern = re.compile(
            '(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
        )
        matches = pattern.findall(line)

        if (conv.get(matches[0])):
            matches[0] = conv.get(matches[0])

        if (conv.get(matches[-1])):
            matches[-1] = conv.get(matches[-1])

        curr = int(matches[0] + matches[-1])

        sum += curr

print(sum)
