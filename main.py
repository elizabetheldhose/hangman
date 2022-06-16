import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['abruptly',
             'absurd',
             'abyss',
             'affix',
             'askew',
             'avenue',
             'awkward',
             'axiom',
             'azure',
             'bagpipes',
             'bandwagon',
             'banjo',
             'bayou',
             'beekeeper',
             'bikini',
             'blitz',
             'blizzard',
             'boggle',
             'bookworm',
             'boxcar',
             'boxful',
             'buckaroo',
             'buffalo',
             'buffoon',
             'buxom',
             'buzzard',
             'buzzing',
             'buzzwords',
             'caliph',
             'cobweb',
             'cockiness',
             'croquet',
             'crypt',
             'curacao',
             'cycle',
             'daiquiri',
             'dirndl',
             'disavow',
             'dizzying',
             'duplex',
             'dwarves',
             'embezzle',
             'equip',
             'espionage',
             'euouae',
             'exodus',
             'faking',
             'fishhook',
             'fixable',
             'fjord',
             'flapjack',
             'flopping',
             'fluffiness',
             'flyby',
             'foxglove',
             'frazzled',
             'frizzled',
             'fuchsia',
             'funny',
             'gabby',
             'galaxy',
             'galvanize',
             'gazebo',
             'giaour',
             'gizmo',
             'glowworm',
             'glyph',
             'gnarly',
             'gnostic',
             'gossip',
             'grogginess',
             'haiku',
             'haphazard',
             'hyphen',
             'iatrogenic',
             'icebox',
             'injury',
             'ivory',
             'ivy',
             'jackpot',
             'jaundice',
             'jawbreaker',
             'jaywalk',
             'jazziest',
             'jazzy',
             'jelly',
             'jigsaw',
             'jinx',
             'jiujitsu',
             'jockey',
             'jogging',
             'joking',
             'jovial',
             'joyful',
             'juicy',
             'jukebox',
             'jumbo',
             'kayak',
             'kazoo',
             'keyhole',
             'khaki',
             'kilobyte',
             'kiosk',
             'kitsch',
             'kiwifruit',
             'klutz',
             'knapsack',
             'larynx',
             'lengths',
             'lucky',
             'luxury',
             'lymph',
             'marquis',
             'matrix',
             'megahertz',
             'microwave',
             'mnemonic',
             'mystify',
             'naphtha',
             'nightclub',
             'nowadays',
             'numbskull',
             'nymph',
             'onyx',
             'ovary',
             'oxidize',
             'oxygen',
             'pajama',
             'peekaboo',
             'phlegm',
             'pixel',
             'pizazz',
             'pneumonia',
             'polka',
             'pshaw',
             'psyche',
             'puppy',
             'puzzling',
             'quartz',
             'queue',
             'quips',
             'quixotic',
             'quiz',
             'quizzes',
             'quorum',
             'razzmatazz',
             'rhubarb',
             'rhythm',
             'rickshaw',
             'schnapps',
             'scratch',
             'shiv',
             'snazzy',
             'sphinx',
             'spritz',
             'squawk',
             'staff',
             'strength',
             'strengths',
             'stretch',
             'stronghold',
             'stymied',
             'subway',
             'swivel',
             'syndrome',
             'thriftless',
             'thumbscrew',
             'topaz',
             'transcript',
             'transgress',
             'transplant',
             'triphthong',
             'twelfth',
             'twelfths',
             'unknown',
             'unworthy',
             'unzip',
             'uptown',
             'vaporize',
             'vixen',
             'vodka',
             'voodoo',
             'vortex',
             'voyeurism',
             'walkway',
             'waltz',
             'wave',
             'wavy',
             'waxy',
             'wellspring',
             'wheezy',
             'whiskey',
             'whizzing',
             'whomever',
             'wimpy',
             'witchcraft',
             'wizard',
             'woozy',
             'wristwatch',
             'wyvern',
             'xylophone',
             'yachtsman',
             'yippee',
             'yoked',
             'youthful',
             'yummy',
             'zephyr',
             'zigzag',
             'zigzagging',
             'zilch',
             'zipper',
             'zodiac',
             'zombie',
             ]
chosen_word = random.choice(word_list)


lives = 6
display = []
for n in chosen_word:
    display += "_"

n = len(chosen_word)
end_of_game = False

while not end_of_game and lives > -1:
    guess = input("guess the letter: ")
    for position in range(n):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("you lose")
            end_of_game = True

    if "_" not in display:
        print("you win")
        end_of_game = True

