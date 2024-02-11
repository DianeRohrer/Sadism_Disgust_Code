# Run this code at the command line each time you run a participant
# before doing anything else with psychopy.
#
# For Windows (Thanos):
# > cd C:\User\rohre\Local\Sadism_Disgust_code
# > dir
# > python run_first.py
#
# For MacOS (The Morrigan):
# > cd Desktop/Sadism_Disgust_Code
# > ls
# > python3 run_first.py
#
# These will prompt you for the subject ID.
# This will create and save the randomized conditions and offers
# for this participant in a repeatable way.

# The `json` library has tools in it for converting data to and from
# the JSON format--a useful way to store and read data.
import json

# The `os` library is useful for doing operating system-specific things,
# like adding backslashes in Windows file paths, but forward slashes for Mac.
import os

# The `random` library has all our randomization tools in it.
import random

# Total number of tastant blocks to be run in the gustatory condition
N_TASTANT_BLOCKS = 5

# Total number of games to be played by a participant
N_GAMES = 20

VISUAL_DIRNAME = "Images_Visual_Disgust"

# Create a directory called `data` if it doesn't already exist
os.makedirs("data", exist_ok=True)

# Get the subject ID from the experimenter
print("Enter the subject ID")
print("and then hit Enter")
subject_id_input = input()

# Check to make sure that the ID is an integer
# (or at least can be converted to an integer)
try:
    subject_id = int(subject_id_input)
except ValueError:
    print("Subject ID should be a number.")
    print("Maybe give it another go.")
    quit()

# Use the `subject_id` as a random seed.
# This means that the random sequences generated for this subject will
# be the same every time. It looks like running this on Mac and Windows
# gives the same results too.
random.seed(subject_id)

# There are three main conditions:
# Gustatory Disgust ("gustatory")
# Moral Disgust ("moral")
# Visual Disgust ("visual")
conditions = ["gustatory", "moral", "visual"]

# Put the conditions in a random order.
# There are six possible sequences.
# One of them is "gustatory", "moral", "visual"--it still counts as random :)
random.shuffle(conditions)
print("Run conditions in this order:")
print(conditions)

# Save text file showing the order in which the conditions are run.
# Open up a text file for writing called `data/conditions_{subject_id}.txt`.
with open(os.path.join("data", f"conditions_{subject_id}.txt"), "wt") as f:
    f.write(str(conditions))

# Randomize the sequence of disgust images
######################################
# Read in the full set of disgust images.
# Start an empty list to keep them in.
disgust_image_paths = []
# Get a list of all the filenames in the directory where visual disgust photos
# are being stored.
filenames = os.listdir(VISUAL_DIRNAME)
# Work on each file one at a time.
for filename in filenames:
    # Check whether it ends in `jpg`. This ignores any other
    # extra files that might be present.
    if filename[-3:] == "jpg":
        # Put together the fill path name for the image--
        # directory + filename.
        # This is so that we can tell psychopy exactly where to look for it.
        disgust_image_path = os.path.join(VISUAL_DIRNAME, filename)
        # Add the path to the list of disgust image paths.
        disgust_image_paths.append(disgust_image_path)

# Shuffle visual disgust images sp that they end up in a random order.
random.shuffle(disgust_image_paths)

# Save two copies of the list of disgust images.
# One copy has the subject ID in the name and the other doesn't.
# The copy with the subject ID gets kept, so we can refer back to it during
# analysis.
# The other copy gets over-written each time you run this `run_first.py`
# This is where psychopy looks to get its randomizations. It always
# contains the results of the most recent run.

# Open up a text file for writing called `data/disgust_images.txt`.
'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "disgust_images.txt"), "wt") as f:
    f.write(json.dumps(disgust_image_paths))
'''

with open(os.path.join("data", f"disgust_images_{subject_id}.txt"), "wt") as f:
    # Convert the list of images to a JSON and write it to the file.
    f.write(json.dumps(disgust_image_paths))

# Randomize the sequence of tastants
####################################


def has_back_to_back_quinine(tastant_list):
    """
    In a list of five tastants, check whether the two quinine conditions
    are next to each other.
    """
    i_q_lo = tastant_list.index("low_quinine")
    i_q_hi = tastant_list.index("high_quinine")
    dist = abs(i_q_lo - i_q_hi)
    # Only returns True if the two quinine conditions are
    # one positions apart on the list.
    return dist == 1


tastants = []
print()
print("Tastant sequence for the Gustatory Condition")
for i_block in range(N_TASTANT_BLOCKS):
    block_tastants = [
        "low_quinine",
        "high_quinine",
        "low_sucrose",
        "high_sucrose",
        "water",
    ]
    while has_back_to_back_quinine(block_tastants):
        random.shuffle(block_tastants)
    tastants.append(block_tastants)
    print(f"  For block {i_block + 1}")
    print(block_tastants)

'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "tastants.txt"), "wt") as f:
    f.write(json.dumps(tastants))
'''
with open(os.path.join("data", f"tastants_{subject_id}.txt"), "wt") as f:
    f.write(json.dumps(tastants))

# Where to find the images we'll need
OPPONENT_DIRNAME = "Virtual_Participant"
EMOTION_DIRNAME = "Emotion_Faces"

# Randomize the sequence of opponents.
######################################
# Read in the full set of opponents.
# Start an empty list to keep them in.
all_opponents = []
# Get a list of all the filenames in the directory where opponent photos
# are being stored.
filenames = os.listdir(OPPONENT_DIRNAME)

# Work on each file one at a time.
for filename in filenames:
    # Check whether it ends in `jpg`. This ignores any other
    # extra files that might be present.
    if filename[-3:] == "jpg":
        # Pull out the opponent's name--everything that comes before the "."
        # in the filename.
        opponent_name = filename.split(".")[0]
        # Put together the fill path name for the image--
        # directory + filename.
        # This is so that we can tell psychopy exactly where to look for it.
        opponent_path = os.path.join(OPPONENT_DIRNAME, filename)
        # Put the name and path together in the same data element
        # (called a tuple) and add that tuple to the list of opponents.
        all_opponents.append((opponent_name, opponent_path))

# At this point, there is a list with one element per opponent,
# and each element is tuple containing (name, path).

# Make an empty list to fill for all games.
opponents = []

# Once for each game that will be played,
# randomly choose one of the opponents and add it to the list.
# The same opponent may occur twice in a row. The might not occur
# at all. But their occurrences will all be random.
# It's like rolling dice.
for _ in range(N_GAMES):
    opponents.append(random.choice(all_opponents))

# Save two copies of the list of opponents.
# One copy has the subject ID in the name and the other doesn't.
# The copy with the subject ID gets kept, so we can refer back to it during
# analysis.
# The other copy gets over-written each time you run this `run_first.py`
# This is where psychopy looks to get its randomizations. It always
# contains the results of the most recent run.

# Open up a text file for writing called `data/opponents_A.txt`.
'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "opponents.txt"), "wt") as f:
    f.write(json.dumps(opponents))
'''
with open(os.path.join("data", f"opponents_{subject_id}.txt"), "wt") as f:
    # Convert the list of opponents to a JSON and write it to the file.
    f.write(json.dumps(opponents))

# Randomize the sequence of emotions.
#####################################

# `ordered_emotions` is a list with one element for each of 7 emotions.
ordered_emotions = [
    "E2_anger_m.jpg",
    "E9_contempt_m.jpg",
    "E18_disgust_m.jpg",
    "E26_fear_m.jpg",
    "E34_happy_m.jpg",
    "E42_sad_m.jpg",
    "E50_surprise_m.jpg",
]

# Create an empty list to hold the entire sequence of emotion images.
emotions = []

# Repeat this whole process once for each game
for _ in range(N_GAMES):
    # Take the top-level list of emotions and shuffle it.
    # This is like shuffling a deck of cards--each card is still there,
    # and it's only there once, but they could come in any order.
    # This is good for our purposes because we want the participant to see
    # every emotion once after each game.
    random.shuffle(ordered_emotions)

    # Go through the shuffled list of emotions
    for emotion_filename in ordered_emotions:
        # Pull the emotion name out of the filename by grabbing
        # the portion that comes between the two underscores.
        emotion_name = emotion_filename.split("_")[1]
        # Create the full file path to the image.
        emotion_path = os.path.join(EMOTION_DIRNAME, emotion_filename)
        # Add to the list of emotions a tuple of (name, path).
        emotions.append((emotion_name, emotion_path))

# As with the opponents, save two versions of each list,
# one with the subject ID and one without.
'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "emotions.txt"), "wt") as f:
    f.write(json.dumps(emotions))
'''
with open(os.path.join("data", f"emotions_{subject_id}.txt"), "wt") as f:
    f.write(json.dumps(emotions))


# Generate randome bets
#######################
# Choose the wording how how each bet will be phrased
bet_phrase = {
    "55": "Proposer gets 5 dollars\n\nYou get 5 dollars",
    "73": "Proposer gets 7 dollars\n\nYou get 3 dollars",
    "82": "Proposer gets 8 dollars\n\nYou get 2 dollars",
    "91": "Proposer gets 9 dollars\n\nYou get 1 dollar",
}

'''
def generate_quinine_bets():
    """
    This function makes a pair of bets for when quinine is used.
    It's set up so that there will always be two bets,
    one more fair, one more unfair.
    """
    # Choose 5:5 and 7:3 as "fair" bets
    fair_bets = ["55", "73"]
    # Specify that 80% of the time the fair bet will be 5:5.
    # The other 20% of the time it will be 7:3.
    # This is like flipping a weighted coin that comes up heads
    # 8 times out of 10.
    fair_bet_weights = [0.8, 0.2]
    # Use the weights to pick a fair bet.
    fair_bet = random.choices(fair_bets, weights=fair_bet_weights)

    # Choose 8:2 and 9:1 as "unfair" bets.
    unfair_bets = ["82", "91"]
    # Specify that 50% of the time the fair bet will be 8:2.
    # The other 50% of the time it will be 9:1.
    # This is like flipping a fair coin.
    fair_bet_weights = [0.8, 0.2]
    unfair_bet_weights = [0.5, 0.5]
    unfair_bet = random.choices(unfair_bets, weights=unfair_bet_weights)

    # Combine the fair and unfair bets into a single list of two bets.
    bets = fair_bet + unfair_bet
    # Shuffle the (tiny) list so that either could come first.
    random.shuffle(bets)

    return bets
'''


def generate_sucrose_water_bets():
    """
    This function randomly picks a bet to use
    with sucrose or water each time.
    Unlike quinine, it doesn't ensure a fixed pattern of
    one fair, one unfair pairings. It just randomly pulls one of the
    four each time using a weighted selection process.
    """
    # Lay out the complete set of 5:5, 7:3, 8:2, and 9:1 bets
    bets = ["55", "73", "82", "91"]
    # Assign weights to each bet
    # 50%   5:5
    # 10%   7:3
    # 20%   8:2
    # 20%   9:1
    weights = [0.5, 0.1, 0.2, 0.2]

    # Randomly pick two offers to use with the sucrose or water.
    # Order doesn't matter here, since both of these are randomly chosen.
    # It might be the same offer twice in a row.
    first_offer = random.choices(bets, weights=weights)
    second_offer = random.choices(bets, weights=weights)
    offer_pair = first_offer + second_offer
    return offer_pair


def generate_bets():
    # Start with an empty list to add it.
    bets = []
    for _ in range(N_GAMES):
        bets = bets + generate_sucrose_water_bets()
    return bets


# Generate a randomized list offers.
bets = generate_bets()

# Now bets is a lists of offers.

# For each offer in the game find the phrase to express it,
# and create a new list that has all these phrases in it.
bet_phrases = [bet_phrase[bet] for bet in bets]

# Now bet_phrases is a list of English sentences,
# each describing the offer for the game it corresponds to.

# Same trick. Save copies of bets and bet_phrases for all conditions
# in two versions, one with subject ID and one without.
'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "bets.txt"), "wt") as f:
    f.write(json.dumps(bets))
'''
with open(os.path.join("data", f"bets_{subject_id}.txt"), "wt") as f:
    f.write(json.dumps(bets))
'''
# Commented out to avoid saving data with ambiguous subject id.
with open(os.path.join("data", "bet_phrases.txt"), "wt") as f:
    f.write(json.dumps(bet_phrases))
'''
with open(os.path.join("data", f"bet_phrases_{subject_id}.txt"), "wt") as f:
    f.write(json.dumps(bet_phrases))
