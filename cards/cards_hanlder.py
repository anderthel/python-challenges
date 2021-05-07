from colorama import Fore, Back, Style			# Used for coloring cards
import random			# Used for shuffle


# Unicode based cards
small = {
	"AS": "🂡", "2S": "🂢", "3S": "🂣", "4S": "🂤", "5S": "🂥", "6S": "🂦", "7S": "🂧", "8S": "🂨", "9S": "🂩", "0S": "🂪", "JS": "🂫", "QS": "🂭", "KS": "🂮",
	"AH": "🂱", "2H": "🂲", "3H": "🂳", "4H": "🂴", "5H": "🂵", "6H": "🂶", "7H": "🂷", "8H": "🂸", "9H": "🂹", "0H": "🂺", "JH": "🂻", "QH": "🂽", "KH": "🂾",
	"AC": "🃑", "2C": "🃒", "3C": "🃓", "4C": "🃔", "5C": "🃕", "6C": "🃖", "7C": "🃗", "8C": "🃘", "9C": "🃙", "0C": "🃚", "JC": "🃛", "QC": "🃝", "KC": "🃞",
	"AD": "🃁", "2D": "🃂", "3D": "🃃", "4D": "🃄", "5D": "🃅", "6D": "🃆", "7D": "🃇", "8D": "🃈", "9D": "🃉", "0D": "🃊", "JD": "🃋", "QD": "🃍", "KD": "🃎",
	"J": "🃏", "--": "🂠"}

# Set color by suit
color = {
	"-": f"{Fore.BLACK}{Back.WHITE}",
	"S": f"{Fore.BLACK}{Back.WHITE}",
	"C": f"{Fore.BLACK}{Back.WHITE}",
	"H": f"{Fore.RED}{Back.WHITE}",
	"D": f"{Fore.RED}{Back.WHITE}"}

# Values and suits (0 is 10)
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K"]
suits = ["H", "D", "S", "C"]


def get_card(card, size="S"):
	if size == "S":
		if len(card) == 0:
			return ""
		else:
			try:
				return f"{color[card[1]]}{small[card]} {Style.RESET_ALL}"
			except KeyError:
				print("Error: card not supported")
				raise
			else:
				pass
	else:
		print("Error: card not supported")
		raise


class Deck():
	def __init__(self):
		self.cards = []
		self.delt = []
		for suit in suits:
			for value in values:
				self.cards.append(f"{value}{suit}")
		self.shuffle()

	def shuffle(self):
		self.cards.extend(self.delt)
		self.delt = []
		random.shuffle(self.cards)

	def print(self):
		for self.card in self.cards:
			print(get_card(self.card), end="")
		print()

	def draw(self):
		card = self.cards.pop()
		self.delt.append(card)
		return(card)


class Shoe():
	def __init__(self, count):
		self.cards = []
		self.delt = []
		for self.i in range(count):
			deck = Deck()
			self.cards.extend(deck.cards)
		self.shuffle()

	def shuffle(self):
		self.cards.extend(self.delt)
		self.delt = []
		random.shuffle(self.cards)

	def print(self):
		for self.card in self.cards:
			print(get_card(self.card), end="")
		print()

	def draw(self):
		card = self.cards.pop()
		self.delt.append(card)
		return(card)


if __name__ == '__main__':
	pass


# Large Example
#  __________
# |₁₀        |
# |   ♥   ♥  |
# |     ♥    |
# |   ♥   ♥  |
# |   ♥   ♥  |
# |     ♥    |
# |   ♥   ♥  |
# |          |
#  ‾‾‾‾‾‾‾‾‾‾
