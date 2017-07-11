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
        'greetings', 'fish', 'dominate', 'Lindsey', 'Tyrese', 'playstation',
        'nothing', 'something', 'fucking', 'life', 'homework', 'singular',
        'random', 'young', 'first', 'kek', 'triggered', 'nigga', 'branscomb',
        'Neil', 'music', 'reddit', 'facebook', 'twitter', 'tom', 
        'hope', 'death', 'marry', 'assert', 'authority', 'reliance',
        'presidents', 'Trump', 'spook', 'snapchat', 'feet', 'fetish',
        'david', 'selfie', 'stickers', 'pizza', 'lemons', 'savage', 'dollars',
        'pride', 'period', 'Quora', 'scramble', 'trash', 'hyper', 'extra',
        'superpower', 'interest', 'stock', 'market', 'crash', 'donald',
        'trump', 'goatbot', 'peanuts', 'synonym', 'terrible', 'oranges', 'gay',
        'Branflakes', 'branscomb', 'polygon', 'giraffe', 'ferrari', 'chevrolet',
        'toyota', 'ford', 'nissan', 'veteran', 'hairy', 'lumpy', 'utensil', 'nut', 
        'feeding', 'oreo', 'Joseph', 'Alexia', 'percussive', 'slaves', 'zipper', 
        'umbrella', 'internet', 'interval', 'instances', 'recreate', 'creation', 
        'animation', 'percussion', 'carnivorous', 'lean', 'applesauce', 'grits', 
        'splits', 'tea', 'playboy', 'magazine', 'ritz', 'fluctuate', 'qwerty', 
        'champions', 'facebook', 'twitter', 'ghost', 'because', 'tornado', 
        'intriguing', 'jigsaw', 'crude', 'coconut', 'timeless', 'annihilate',
        'blind', 'scrub', 'massage', 'door', 'consumer', 'harmony', 'yourself',
        'me', 'them', 'mints', 'lime', 'pineapple', 'anaconda', 'banana', 
        'Strawberry', 'grape', 'burger', 'waterfall', 'express', 'expert', 
        'apprentice', 'careless', 'guilty', 'beautiful', 'hatred', 'murder', 
        'exterminate', 'scrape', 'chicken', 'nugget', 'fierce', 'rubbish', 
        'tentacles', 'flavorful', 'full', 'laugh', 'greeting', 'mate',
        'matter', 'destructive', 'octave', 'delete', 'plasma', 'dust', 'dent',
        'square', 'teen', 'winner', 'sunrise', 'rising', 'sunshine', 'moon', 
        'night', 'midnight', 'daytime', 'primitive', 'robot', 'caramel', 
        'seventeen', 'school', 'beaver', 'violin', 'damage', 'damn', 'vulture',
        'ginger', 'entry', 'mother', 'father', 'blank', 'cannibal', 'soup', 
        'intern', 'teacher', 'blushing', 'carpenter', 'algebra', 'integer',]

def random_word(array):
    word = random.choice(array)
    return word

def scramble_words(word):
    word = list(word.lower())
    random.shuffle(word)
    return ''.join(word)
