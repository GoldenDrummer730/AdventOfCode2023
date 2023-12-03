import re

data = ''

number_set = []

with open(r'Day 3\input.txt') as input:
    for line in input:
        data += f'{line}'

line_length = re.search("\n", data).end()
print(line_length)

with open('out.txt', 'w')as o:
    for match in re.finditer(pattern='(\d{1,})', string=data):
        local_set = set()
        # print(f'Match: {match.group()}\tStart: {match.start()}\tEnd: {match.end()}')
        for i in range(match.start(), match.end()):
            try:
                o.write(f"To Match: {data[i]} @ {i}\n")
                # Check top left
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[(i - line_length) - 1])):
                    local_set.add(match.group())
                    o.write(f'Top Left Found\n')
                # Check top
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[i - line_length])):
                    local_set.add(match.group())
                    o.write(f'Top Found\n')
                # Check top right
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[(i - line_length) + 1])):
                    local_set.add(match.group())
                    o.write(f'Top Right Found\n')
                # Check left
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[i - 1])):
                    local_set.add(match.group())
                    o.write(f'Left Found\n')
                # Check right
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[i + 1])):
                    local_set.add(match.group())
                    o.write(f'Right Found\n')
                # Check bottom left
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[(i + line_length) - 1])):
                    local_set.add(match.group())
                    o.write(f'Bottom Left\n')
                # Check bottom
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[i + line_length])):
                    local_set.add(match.group())
                    o.write(f'Bottom\n')
                # Check bottom right
                if(re.match(pattern='[^\.a-zA-Z0-9\n]', string=data[(i + line_length) + 1])):
                    local_set.add(match.group())
                    o.write(f'Bottom Right Found\n')
            except IndexError as e:
                continue
        if (len(local_set) > 0):
            number_set.append(local_set.pop())
        o.write(f'==============\n')
    o.flush()

sum = sum([int(x) for x in number_set])
print(sum)