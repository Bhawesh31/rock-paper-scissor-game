from RPS_game import play, quincy, kris, mr_robot, abbey
from RPS import player

# Play against each bot
print("Quincy")
play(player, quincy, 1000)

print("\nKris")
play(player, kris, 1000)

print("\nMr. Robot")
play(player, mr_robot, 1000)

print("\nAbbey")
play(player, abbey, 1000)

# Uncomment to run tests
# import test_module
