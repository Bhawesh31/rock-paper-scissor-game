import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # Start with random until enough data
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Frequency analysis
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1

    most_common = max(freq, key=freq.get)

    # Counter most common
    counters = {"R": "P", "P": "S", "S": "R"}
    prediction = most_common
    return counters[prediction]
