import random

class Card():
  def __init__(self, name, value, suit, symbol):
    self.value = value
    self.suit = suit
    self.name = name
    self.symbol = symbol
    self.showing = False

  def __repr__(self):
    if self.showing:
      return self.symbol
    else:
      return "Card"

class Deck():
  def __init__(self):
    self.cards = []
  
  def shuffle(self, times=1 ):
    random.shuffle(self.cards)
    print("Deck Shuffled")

  def deal(self):
    return self.cards.pop(0)

class StandardDeck(Deck):
  def __init__(self):
    self.cards = []
    suits = {"Hearts":"♡", "Spades":"♠", "Diamonds":"♢", "Clubs":"♣"}
    values = {"Two":2,
              "Three":3,
              "Four":4,
              "Five":5,
              "Six":6,
              "Seven":7,
              "Eight":8,
              "Nine":9,
              "Ten":10,
              "Jack":11,
              "Queen":12,
              "King":13,
              "Ace":14 }

    for name in values:
      for suit in suits:
        symbolIcon = suits[suit]
        if values[name] < 11:
          symbol = str(values[name])+symbolIcon
        else:
          symbol = name[0]+symbolIcon
        self.cards.append( Card(name, values[name], suit, symbol) )

  def __repr__(self):
    return "Standard deck of cards:{0} remaining".format(len(self.cards))

class Player():
  def __init__(self,name):
    self.cards = []
    self.name = name

  def cardCount(self):
    return len(self.cards)

  def addCard(self, card):
    self.cards.append(card)


class PokerScorer():
  def __init__(self, cardsList):
    # Number of cards
    self.cards = cardsList

  def flush(self):
    suits = [card.suit for card in self.cards]
    if len( set(suits) ) == 1:
      return True
    return False

  def straight(self):
    values = [card.value for card in self.cards]
    values.sort()

    if not len( set(values)) == 5:
      return False 

    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5

    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False

    return values[4]

  def highCard(self):
    values = [card.value for card in self.cards]
    highCard = None
    for card in self.cards:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card

    return highCard

  def highestCount(self):
    count = 0
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)

    return count

  def pairs(self):
    pairs = []
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)

    return pairs
        
  def fourKind(self):
    values = [card.value for card in self.cards]
    for value in values:
      if values.count(value) == 4:
        return True

  def fullHouse(self):
    two = False
    three = False
    
    values = [card.value for card in self.cards]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True

    if two and three:
      return True

    return False

def interpreterVideoPoker():
  player1_name = input("Please input your name: ")
  player = Player(player1_name)

  # Intial Amount
  points = 100

  # Cost per hand
  

  end = False
  while not end:

    if not points > 0:
      print('You lost all your points!')
      break 

    print( f"{player.name} have {points} points" )
    print()

    ## Hand Loop
    deck = StandardDeck()
    deck.shuffle()

    # Deal Out
    for i in range(5):
      player.addCard(deck.deal())

    # Make them visible
    for card in player.cards:
      card.showing = True

    validInput = False
    while not validInput:
      
      print(player.cards)

      handCost = int(input("Please submit your bet: "))

      points -= handCost

      print("Which cards do you want to discard? ( ie. 1, 2, 3 )")

      print("*Just hit return to hold all, type --exit to help to read the rules and --quit to exit the program")
      inputStr = input()

      if inputStr == "--exit":
        print(f"Thank you for playing {player.name}!")
        end=True
        points += handCost
        break
      
      if inputStr == "--help":
        a = True
        while a:
          print("INSERT POKER RULES HERE")
          print()
          print("Whenever you are ready to continue input --resume")
          b = input()
          if b == "--resume":
            print("Round restarted.")
            break
        points += handCost
        break
          
      try:
        inputList = [int(inp.strip()) for inp in inputStr.split(",") if inp]

        for inp in inputList:
          if inp > 6:
            continue 
          if inp < 1:
            continue 

        for inp in inputList:
          player.cards[inp-1] = deck.deal()
          player.cards[inp-1].showing = True

        validInput = True
      except:
        print("Input Error: use commas to separated the cards you want to hold")

    #Score
    score = PokerScorer(player.cards)
    straight = score.straight()
    flush = score.flush()
    highestCount = score.highestCount()
    pairs = score.pairs()

    # Royal flush
    if straight and flush and straight == 14:
      print("Royal Flush!!!")
      points += 400 * handCost
      print(f"+{points}")

    # Straight flush
    elif straight and flush:
      print("Straight Flush!")
      points += 50 * handCost
      print(f"+{points}")

    # 4 of a kind
    elif score.fourKind():
      print("Four of a kind!")
      points += 25 * handCost
      print(f"+{points}")

    # Full House
    elif score.fullHouse():
      print("Full House!")
      points += 8 * handCost
      print(f"+{points}")

    # Flush
    elif flush:
      print("Flush!")
      points += 5 * handCost
      print(f"+{points}")

    # Straight
    elif straight:
      print("Straight!")
      points += 4 * handCost
      print(f"+{points}")

    # 3 of a kind
    elif highestCount == 3:
      print("Three of a Kind!")
      points += 3 * handCost
      print(f"+{points}")
      

    # 2 pair
    elif len(pairs) == 2:
      print("Two Pairs!")
      points += 2 * handCost
      print(f"+{points}")
      

    # Jacks or better
    elif pairs and pairs[0] > 10:
      print ("Jacks or Better!")
      points += 1 * handCost
      print(f"+{points}")

    player.cards=[]

    print()


interpreterVideoPoker()