import random

words = ['fifth', 'reaction', 'furniture', 'experience', 'ground',
         'fang', 'sidewalk', 'discussion', 'nation', 'rhythm',
         'balls', 'stamp', 'popcorn', 'sign', 'paint', 'baseball',
         'brush', 'governor', 'income', 'fog', 'drain', 'kitten',
         'beetle', 'property', 'push', 'back', 'rake', 'committee',
         'voice', 'dad', 'boat', 'sofa', 'crouch', 'care',
         'hurting', 'maybe', 'argument', 'cake', 'pot', 'thousand',
         'friend', 'silver', 'button', 'list', 'screw', 'market', 'ray',
         'debt', 'ice', 'cast', 'apple', 'smile', 'advice', 'decorate',
         'upset', 'blow', 'walk', 'deal', 'yawn', 'console', 'suck',
         'vanish', 'nurse', 'marble', 'cream', 'square', 'cats', 'suit',
         'brain', 'cough', 'anus', 'guitar', 'height', 'virginia',
         'genitals', 'monkey', 'band', 'boys', 'gender',
         'loose', 'wet', 'juice', 'dead', 'taboo', 'guess', 'alternate',
         'programming', 'javascript', 'word', 'twist', 'onion', 'meadow',
         'greetings', 'fish', 'dominate', 'intellectual', 'control',
         'nothing', 'something', 'fucking', 'life', 'homework', 'singular',
         'random', 'young', 'first', 'triggered', 'honeycomb', 'legendary',
         'music', 'reddit', 'facebook', 'twitter', 'civilization', 'myth',
         'hope', 'death', 'marry', 'assert', 'authority', 'noodles',
         'presidents', 'Trump', 'spook', 'feet', 'fetish', 'bathtub',
         'david', 'selfie', 'stickers', 'pizza', 'lemons', 'savage', 'dollars',
         'pride', 'period', 'scramble', 'trash', 'hyper', 'extra',
         'superpower', 'interest', 'stock', 'market', 'crash',
         'trump', 'goatbot', 'peanuts', 'synonym', 'terrible', 'oranges', 'gay',
         'polygon', 'giraffe', 'corn', 'pepper', 'chimney', 'stupid',
         'veteran', 'hairy', 'lumpy', 'utensil', 'nut', 'engineer',
         'feeding', 'oreo', 'percussive', 'slaves', 'zipper', 'athlete',
         'umbrella', 'internet', 'interval', 'instances', 'recreate', 'creation',
         'animation', 'percussion', 'carnivorous', 'lean', 'applesauce', 'grits',
         'splits', 'tea', 'magazine', 'cracker', 'fluctuate', 'qwerty',
         'champions', 'ghost', 'because', 'tornado', 'engineering', 'evolution',
         'intriguing', 'jigsaw', 'crude', 'coconut', 'timeless', 'annihilate',
         'blind', 'scrub', 'massage', 'door', 'consumer', 'harmony', 'yourself',
         'me', 'them', 'lime', 'pineapple', 'anaconda', 'banana',
         'Strawberry', 'grape', 'burger', 'waterfall', 'express', 'expert',
         'apprentice', 'careless', 'guilty', 'beautiful', 'hatred', 'murder',
         'exterminate', 'scrape', 'chicken', 'nugget', 'fierce', 'rubbish',
         'flavorful', 'full', 'laugh', 'greeting', 'mate', 'gum', 'football',
         'matter', 'destructive', 'octave', 'delete', 'plasma', 'dust', 'dent',
         'square', 'teen', 'winner', 'sunrise', 'rising', 'sunshine', 'moon',
         'night', 'midnight', 'daytime', 'primitive', 'robot', 'caramel',
         'seventeen', 'spider', 'beaver', 'violin', 'damage', 'damn', 'vulture',
         'ginger', 'entry', 'mother', 'father', 'blank', 'cannibal', 'soup',
         'intern', 'teacher', 'blushing', 'carpenter', 'algebra', 'integer',
         'universe', 'legend', 'evidence', 'suspect', 'evil', 'good', 'subtract',
         'america', 'african', 'future', 'yacht', 'scratch', 'genius', 'awesome',
         'access' 'dive', 'ocean', 'library', 'variety', 'entertain', 'avenue',
         'street', 'highway', 'yahoo', 'google', 'youtube', 'porn', 'cream', 'brother',
         'sister', 'greed', 'wrath', 'sloth', 'gluttony', 'discussion', 'video',
         'camera', 'picture', 'frame', 'illness', 'spanish', 'china', 'japan',
         'obama', 'gene', 'applause', 'suffix', 'prefix', 'cookie', 'insect', 'animal',
         'theft', 'school', 'radiation', 'uranium', 'green', 'red', 'blue', 'purple',
         'black', 'white', 'orange', 'yellow', 'brown', 'pink', 'pig', 'fraction',
         'gift', 'formula', 'scream', 'exhaust', 'sprint', 'identity', 'input',
         'output', 'cousin', 'suicide', 'knife', 'defense']

gods_list = ["Agni", "Ah Muzen Cab", "Ah Puch", "Amaterasu", "Anhur", "Anubis", "Ao Kuang", "Aphrodite",
             "Apollo", "Arachne", "Ares", "Artemis", "Artio", "Athena", "Awlix", "Bacchus", "Bakasura",
             "Bastet", "Bellona", "Cabrakan", "Camazots", "Cerberus", "Cernunos", "Chaac", "Change'e", "Chiron",
             "Chronos", "Cu Chulainn", "Cupid", "Da Ji", "Discordia", "Erlang Shen", "Fafnir", "Fenrir",
             "Freya", "Ganesha", "Geb", "Guan Yu", "Hachiman", "Hades", "He Bo", "Hel", "Hercules", "Hou Yi",
             "Hun Batz", "Isis", "Izanami", "Janus", "Jing Wei", "Kali", "Khepri", "Kukulkan", "Kumba", "Kuzenbo",
             "Loki", "Medusa", "Mercury", "Ne Zha", "Neith", "Nemesis", "Nike", "Nox", "Nu Wa", "Odin", "Osiris",
             "Poseidon", "Ra", "Raijin", "Rama", "Rat boi", "Ravana", " Scylla", "Serqet", "Skadi", "Sobek", "Sol",
             "Sun Wukong", "Susanao", "Sylvanus", "Terra", "Thanatos", "The Morrigan", "Thor", "Thoth", "Tyr", "Ullr",
             "Vamana", "Vulcan", "Xbalanque", "Xing Tian", "Ymir", "Zeus", "Zhong Kui"]


def random_word(array):
    word = random.choice(array)
    return word


def scramble_words(word):
    word = list(word.lower())
    random.shuffle(word)
    return ''.join(word)
