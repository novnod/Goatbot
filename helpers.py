import random

words = ['fifth','reaction', 'furniture', 'experience', 'ground',
        'fang', 'sidewalk', 'discussion', 'nation', 'rhythm',
        'balls', 'stamp', 'popcorn', 'sign', 'paint', 'baseball',
        'brush', 'governor', 'income', 'fog', 'drain', 'kitten',
        'beetle', 'property', 'push', 'back', 'rake', 'committee',
        'voice', 'dad', 'boat', 'sofa', 'rhaaheem', 'care', 'DonVon',
        'Lexi', 'Alexus', 'Taylor', 'argument', 'cake', 'pot', 
        'friend', 'silver', 'button', 'list', 'screw', 'market', 'ray',
        'debt', 'ice', 'cast', 'apple', 'smile', 'advice', 'decorate',
        'upset', 'blow', 'walk', 'deal', 'yawn', 'console', 'suck',
        'vanish', 'nurse', 'marble', 'cream', 'square', 'cats', 'suit',
        'brain', 'cough', 'anus', 'vagina', 'cock', 'yo mama', 'guitar',
        'Joey', 'Deontae', 'Destini', 'monkey', 'band', 'boys', 'gender',
        'loose', 'wet', 'juice', 'dead', 'taboo', 'guess', 'coding', 
        'programming', 'javascript', 'Foss', 'Caddell', 'word', 'hey',
        'greetings', 'fish', 'lemons', 'Lindsey', 'Tyrese', 'playstation',
        'nothing', 'something', 'fucking', 'life', 'homework', 'singular',
        'random', 'young', 'first', 'kek', 'triggered', 'nigga']

def random_word(array):
    word = random.choice(array)
    return word