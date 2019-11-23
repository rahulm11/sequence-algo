import argparse

CARDS_PER_HAND_PER_PLAYER_COUNT = {
  2 : 7, 3 : 6, 4 : 6, 6 : 5, 8 : 4, 9 : 4, 10 : 3, 12 : 3
}

SEQUENCES_PER_TEAM_COUNT = {
  2 : 2, 3 : 1
}

def main(args):
  print("Sequence Algorithm")
  print("- Blind 'n Greedy (BNG) Version -\n")
  print(args)
  
  numPlayers = args.players
  numTeams = args.teams
  numCardsPerHand = CARDS_PER_HAND_PER_PLAYER_COUNT[numPlayers]
  numSequencesToWin = SEQUENCES_PER_TEAM_COUNT[numTeams]
  
  print("Number of cards per hand: {}".format(numCardsPerHand))
  print("Number of sequences to win: {}".format(numSequencesToWin))
  
  


def parseArgs():
  parser = argparse.ArgumentParser(description = "Taking a shot at solving Sequence.")
  parser.add_argument(
    "--players", type = int, required = True,
    choices = {2, 3, 4, 6, 8, 9, 10, 12},
    help = "Total number of players."
  )
  parser.add_argument(
    "--teams", type = int, required = True,
    choices = {2, 3},
    help = "Number of teams. If the number of teams equals the number of players, each player is individual. Players must be divisible by teams."
  )
  
  args = parser.parse_args()
  if ((args.players % args.teams) != 0):
    parser.error("--players ({}) is not divisble by --teams ({}).".format(args.players, args.teams))
  
  return args

if __name__ == "__main__":
  main(parseArgs())
