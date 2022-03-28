import random
from inspect import signature

colours = ["Golden", "Silver", "Shining", "Royal", "White", "Red"]
animals = ["Dragon", "Phoenix", "Unicorn", "Kylin", "Turtle", "Tiger"]
directions = ["East", "West", "North", "South", "Center"]
landmark = ["Bridge", "Tower", "Palace", "River"]
names = ["Wong", "Wang", "Zhang", "Liu", "Chen", "Zhao", "Huang", "Wu"]
words = ["Zilver", "Dynasty", "Chopsticks", "Feng Shui", "Ginkgo", "Hanfu"]

param_to_list_map = {
    'descriptor': [colours, directions],
    'noun': [animals, landmark],
    'ch_name': [names],
    'word': [words],
}

formats = [
    lambda descriptor=None, noun=None: f'{descriptor} {noun} Restaurant',
    lambda ch_name=None: f'Mr {ch_name}\'s',
    lambda word=None: f'{word} Chinese'
]

func = formats[random.randint(0, len(formats) - 1)]
sig = signature(func)

args = []
for param in sig.parameters:
    choice_types = param_to_list_map[param][random.randint(0, len(param_to_list_map[param]) - 1)]
    argument = choice_types[random.randint(0, len(choice_types) - 1)]
    args.append(argument)

print(f'\n\n{func(*args)}\n\n')
