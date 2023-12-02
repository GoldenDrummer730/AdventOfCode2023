import re


red_total = 12
green_total = 13
blue_total = 14

totals = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_possible(sets: list[str]):
    red_shown = 0
    green_shown = 0
    blue_shown = 0
    for game in sets:
        for curr_game in game.split(','):
            curr_game = curr_game.strip()
            if (re.findall('red', curr_game)):
                red_shown += int(curr_game[0, curr_game.find(' ')])
            elif (re.findall('green', curr_game)):
                green_shown += int(curr_game[0, curr_game.find(' ')])
            elif (re.findall('blue', curr_game)):
                blue_shown += int(curr_game[0, curr_game.find(' ')])
            
        print(f'Red: {red_shown}\tGreen: {green_shown}\tBlue: {blue_shown}\n')
        if ((red_shown > red_total) or 
            (green_shown > green_total) or
            (blue_shown > blue_total)):
                return False
    return True

with open(r'Day 2\sample.txt') as input:
    for line in input:
        # First grab the id of the game
        groups = re.split(pattern=':', string=line)
        id = groups[0][-1]
        
        sets = groups[1].replace('\n', '').split(';')
        print(is_possible(sets))
        print('===============')
