import re

data = ''

number_set = []

pattern = '[^\.a-zA-Z0-9\n]'
pattern2 = '\d+'

with open(r'Day 3\input.txt') as input:
    for line in input:
        data += f'{line}'

line_length = re.search("\n", data).end()
# print(line_length)


number_list = []
symbol_list = []

for match in re.finditer(pattern='(\d+)', string=data):
    number_list.append(match)

for match in re.finditer(pattern='[^\.a-zA-Z0-9\n]', string=data):
    symbol_list.append(match)

def get_number_match(index: int):
    for number in number_list:
        if (index in range(number.start(), number.end())):
            return number.group()
    return -1
# Part 1
with open('out.txt', 'w') as o:
    for match in number_list:
        local_set = set()
        # print(f'Match: {match.group()}\tStart: {match.start()}\tEnd: {match.end()}')
        for i in range(match.start(), match.end()):
            try:
                o.write(f"To Match: {data[i]} @ {i}\n")
                # Check top left
                if(re.match(pattern=pattern, string=data[(i - line_length) - 1])):
                    local_set.add(match.group())
                    o.write(f'Top Left Found\n')
                # Check top
                if(re.match(pattern=pattern, string=data[i - line_length])):
                    local_set.add(match.group())
                    o.write(f'Top Found\n')
                # Check top right
                if(re.match(pattern=pattern, string=data[(i - line_length) + 1])):
                    local_set.add(match.group())
                    o.write(f'Top Right Found\n')
                # Check left
                if(re.match(pattern=pattern, string=data[i - 1])):
                    local_set.add(match.group())
                    o.write(f'Left Found\n')
                # Check right
                if(re.match(pattern=pattern, string=data[i + 1])):
                    local_set.add(match.group())
                    o.write(f'Right Found\n')
                # Check bottom left
                if(re.match(pattern=pattern, string=data[(i + line_length) - 1])):
                    local_set.add(match.group())
                    o.write(f'Bottom Left\n')
                # Check bottom
                if(re.match(pattern=pattern, string=data[i + line_length])):
                    local_set.add(match.group())
                    o.write(f'Bottom\n')
                # Check bottom right
                if(re.match(pattern=pattern, string=data[(i + line_length) + 1])):
                    local_set.add(match.group())
                    o.write(f'Bottom Right Found\n')
            except IndexError as e:
                continue
        if (len(local_set) > 0):
            number_set.append(local_set.pop())
        o.write(f'==============\n')
    o.flush()

result = sum([int(x) for x in number_set])
print(f'Part 1: {result}')


symbol_list = [x for x in symbol_list if x.group() == '*']
prod_set = []
# Part 2
with open('out2.txt', 'w')as o:
    for match in symbol_list:
        local_gears = set()
        # print(f'Match: {match}\tStart: {match.start()}\tEnd: {match.end()}')
        try:
            o.write(f"To Match: {match.group()} @ {match.start()}\n")
        # Check top left
            top_left = re.match(pattern=pattern2, string=data[(match.start() - line_length) - 1])
            if(top_left):
                local_gears.add(get_number_match(index = (match.start() - line_length) - 1))
                o.write(f'Top Left Found: {local_gears}\n')
            # Check top
            top = re.match(pattern=pattern2, string=data[match.start() - line_length])
            if(top):
                local_gears.add(get_number_match(index = match.start() - line_length))
                o.write(f'Top Found: {top.group()}\n')
            # Check top right
            top_right = re.match(pattern=pattern2, string=data[(match.start() - line_length) + 1])
            if(top_right):
                local_gears.add(get_number_match(index = (match.start() - line_length) + 1))
                o.write(f'Top Right Found: {top_right.group()}\n')
            # Check left
            left = re.match(pattern=pattern2, string=data[match.start() - 1])
            if(left):
                local_gears.add(get_number_match(index=match.start() - 1))
                o.write(f'Left Found: {left.group()}\n')
            # Check right
            right = re.match(pattern=pattern2, string=data[match.start() + 1])
            if(right):
                local_gears.add(get_number_match(index=match.start() + 1))
                o.write(f'Right Found: {right.group()}\n')
            # Check bottom left
            bottom_left = re.match(pattern=pattern2, string=data[(match.start() + line_length) - 1])
            if(bottom_left):
                local_gears.add(get_number_match(index=(match.start() + line_length) - 1))
                o.write(f'Bottom Left: {bottom_left.group()}\n')
            # Check bottom
            bottom = re.match(pattern=pattern2, string=data[match.start() + line_length])
            if(bottom):
                local_gears.add(get_number_match(index=match.start() + line_length))
                o.write(f'Bottom: {bottom.group()}\n')
            # Check bottom right
            bottom_right = re.match(pattern=pattern2, string=data[(match.start() + line_length) + 1])
            if(bottom_right):
                local_gears.add(get_number_match(index=(match.start() + line_length) + 1))
                o.write(f'Bottom Right Found: {bottom_right.group()}\n')
        except IndexError as e:
            continue
        # print(local_gears)
        if (len(local_gears) == 2):
            prod = int(local_gears.pop()) * int(local_gears.pop())
            # print(prod)
            prod_set.append(prod)
        o.write(f'==============\n')
        o.flush()

result = sum([int(x) for x in prod_set])
print(f'Part 2: {result}')
