from cards_hanlder import get_card, Shoe		# Used for card related stuff
from time import sleep							# Used for waiting
import os										# Used for screan clear

# Settings
decks = 6				# Number of decks in shoe
width = 75				# Width for play window
dealspeed = 0.25		# Deal speed in seconds (lower is faster)


def screen_clear():
	if os.name == 'posix':
		_ = os.system('clear')
	else:
		_ = os.system('cls')


def menu():
	screen_clear()
	print("Welcome\n1) Play Blackjack\n2) How to play\n3) Exit")
	choice = int(input("Please make a selection: "))
	if choice not in range(1, 4):
		print("Error: Choice must be 1 to 3")
		menu()
	elif choice == 1:
		screen_clear()
		play()
	elif choice == 2:
		screen_clear()
		instruction()
	else:
		screen_clear()
		print("Goodbye")


def play():
	def cards_value(cards):
		cardvalues = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 10, "J": 10, "Q": 10, "K": 10, "-": 0}
		value = 0
		aces = 0
		for card in cards:
			if card[0] == "A":
				aces += 1
			else:
				value += cardvalues[card[0]]
		if aces == 0:
			return value
		elif value + (aces * 11) <= 21:
			return value + (aces * 11)
		else:
			return value + aces

	def hit(cards):
		cards.append(shoe.draw())
		value = cards_value(cards)
		return cards, value

	def print_display(dealer_cards, dealer_value, player_cards, player_value):
		chars = {"0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", " ": " ", "(": "₍", ")": "₎"}
		dealer_value = "".join(chars[char] for char in str(dealer_value))
		player_value = "".join(chars[char] for char in str(player_value))
		dealer_cards_len = len(dealer_cards)
		dealer_cards = "".join(get_card(card) for card in dealer_cards)
		player_cards_len = len(player_cards)
		player_cards = "".join(get_card(card) for card in player_cards)

		# Print
		display = ""
		display = "".join([display, f" {'_'*width} \n"])
		display = "".join([display, f"|{' '.ljust(width)}|\n"])
		display = "".join([display, f"|{' Dealer:'.ljust(width)}|\n"])
		display = "".join([display, f"|{f' {dealer_value}'.ljust(width)}|\n"])
		display = "".join([display, f"|{f' {dealer_cards}'.ljust(width + dealer_cards_len*14)}|\n"])
		display = "".join([display, f"|{' '.ljust(width)}|\n"])
		display = "".join([display, f"|{' '.ljust(width)}|\n"])
		display = "".join([display, f"|{' You:'.ljust(width)}|\n"])
		display = "".join([display, f"|{f' {player_value}'.ljust(width)}|\n"])
		display = "".join([display, f"|{f' {player_cards}'.ljust(width + player_cards_len*14)}|\n"])
		display = "".join([display, f"|{' '.ljust(width)}|\n"])
		display = "".join([display, f"|{' '.ljust(width)}|\n"])
		display = "".join([display, f" {'‾'*width} \n"])
		screen_clear()
		print(display)
		sleep(dealspeed)

	def dealer(dealer_card_hidden, dealer_cards, dealer_value, player_cards, player_value):
		# Set inital values after flipping hidden
		dealer_cards = [''.join(dealer_card_hidden), ''.join(dealer_cards[1:])]
		print(dealer_cards)
		print(type(dealer_cards))
		dealer_value = cards_value(dealer_cards)
		print_display(dealer_cards, dealer_value, player_cards, player_value)

		# Basic loop
		while dealer_value <= 16:
			dealer_cards, dealer_value = hit(dealer_cards)
			print_display(dealer_cards, dealer_value, player_cards, player_value)
		if dealer_value == 21:
			print("Blackjack!\nDealer Win!")
			sleep(2)
			menu()
		elif dealer_value > 21:
			print("Dealer Bust!\nPlayer Win!")
			sleep(2)
			menu()
		elif dealer_value > player_value:
			print("Dealer Higher!\nDealer Win!")
			sleep(2)
			menu()
		elif dealer_value < player_value:
			print("Player Higher!\nPlayer Win!")
			sleep(2)
			menu()

	# Startup
	shoe = Shoe(decks)

	# Initial Values
	dealer_cards, dealer_value = [], 0
	player_cards, player_value = [], 0
	print_display(dealer_cards, dealer_value, player_cards, player_value)

	# Hide First Dealer Card
	dealer_card_hidden = [shoe.draw()]
	dealer_cards, dealer_value = ["--"], 0
	print_display(dealer_cards, dealer_value, player_cards, player_value)

	# Deal remaining
	player_cards, player_value = hit(player_cards)
	print_display(dealer_cards, dealer_value, player_cards, player_value)
	dealer_cards, dealer_value = hit(dealer_cards)
	print_display(dealer_cards, dealer_value, player_cards, player_value)
	player_cards, player_value = hit(player_cards)
	print_display(dealer_cards, dealer_value, player_cards, player_value)

	# Input
	while player_value < 21:
		print("1) Hit\n2) Stand")
		choice = int(input("Please make a selection: "))
		if choice not in range(1, 3):
			print("Error: Choice must be 1 or 2")
		elif choice == 1:
			player_cards, player_value = hit(player_cards)
			print_display(dealer_cards, dealer_value, player_cards, player_value)
		elif choice == 2:
			break
	if player_value == 21:
		print("Blackjack!\nPlayer Win!")
		sleep(2)
		menu()
	elif player_value > 21:
		print("Player Bust!\nDealer Win!")
		sleep(2)
		menu()
	else:
		dealer(dealer_card_hidden, dealer_cards, dealer_value, player_cards, player_value)


def instruction():
	print("Instructions:\n")
	input("Press enter to continue\n")
	screen_clear()
	menu()


if __name__ == '__main__':
	menu()
