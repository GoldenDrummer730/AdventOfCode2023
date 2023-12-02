import re


red_total = 12
green_total = 13
blue_total = 14

result = 0

def is_possible(sets: list[str]):
    for game in sets:
        for curr_game in game.split(','):
            red_shown = 0
            green_shown = 0
            blue_shown = 0
            
            curr_game = curr_game.strip().split(' ')

            if (re.findall('red', curr_game[1])):
                red_shown += int(curr_game[0])
            
            elif (re.findall('green', curr_game[1])):
                green_shown += int(curr_game[0])
            
            elif (re.findall('blue', curr_game[1])):
                blue_shown += int(curr_game[0])
            
        # print(f'Red: {red_shown}\tGreen: {green_shown}\tBlue: {blue_shown}\n')
            if ((red_shown > red_total) or 
                (green_shown > green_total) or
                (blue_shown > blue_total)):
                    return False
    return True


def least_possible(sets: list[str]):
    power = 0
    min_red = 0
    min_green = 0
    min_blue = 0
    for game in sets:
        for curr_game in game.split(','):
            curr_game = curr_game.strip().split(' ')

            if (re.findall('red', curr_game[1])):
                min_red = max(min_red, int(curr_game[0]))
            
            elif (re.findall('green', curr_game[1])):
                min_green = max(min_green, int(curr_game[0]))
            
            elif (re.findall('blue', curr_game[1])):
                min_blue = max(min_blue, int(curr_game[0]))
        
    #print(f'Red: {min_red}\tGreen: {min_green}\tBlue: {min_blue}\n')

    return min_red * min_green * min_blue


with open(r'Day 2\input.txt') as input:
    for line in input:
        # First grab the id of the game
        groups = re.split(pattern=':', string=line)
        id = int(groups[0].split(' ')[-1])
        
        sets = groups[1].replace('\n', '').split(';')

        # Part 1
        # if(is_possible(sets)):
        #     print(id)
        #     result += id
    
        # Part 2
        result += least_possible(sets)

print(result)
