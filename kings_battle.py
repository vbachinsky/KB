#! /usr/bin/python3

import sys
import random
import csv

"""
	Kings Battle is game about war between men and machines.
"""

def check_correct_value(choise_of_option):
	while True:
		if not choise_of_option.isdigit() or not int(choise_of_option) in (1, 2, 3):
			print('Please, enter the correct value')
			return True
		else:
			return False

class Settings():
	"""Basic messages"""
	@staticmethod
	def hello():
		print("Welcome to Battle!!!")
	@staticmethod
	def win():
		print("You win!")
	@staticmethod
	def lose():
		print("You lose!")


class Warrior():
	"""Basic class Warrior"""
	def __init__(self, option, name, power, skill, health):
		self.name = name
		self.power = power
		self.skill = skill
		self.health = health
		self.option = option
		self._some_hidden_parametr = "some hidden parametr"
		filename = 'warriors.csv'
		with open(filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)
			self.list_warriors, self.list_power, self.list_health, self.list_skill = [], [], [], []
			for row in reader:
				self.list_warriors.append(row[0])
				self.list_power.append(int(row[1]))
				self.list_health.append(int(row[2]))
				self.list_skill.append(float(row[3]))
	
	# getter method
	def get_some_hidden_parametr(self):
		return self._some_hidden_parametr

	# setter method
	def set_some_hidden_parametr(self, x):
		self._some_hidden_parametr = x

	# magic method
	def __gt__(self, other):
		return self.power > other.power

	# magic method
	def __lt__(self, other):
		return self.power < other.power

	def set_warrior(self):
		self.name = self.list_warriors[self.option - 1]
		self.power = int(self.list_power[self.option - 1])
		self.health = int(self.list_health[self.option - 1])
		self.skill = float(self.list_skill[self.option - 1])


class Fight(Warrior):
	"""Game function"""
	def __init__(self, option = None, name = '', power = 10, skill = 1.0, health = 100):
		super().__init__(option, name, power, skill, health)

	def get_damage(self):
		return (self.power * self.skill)

	def set_protagonist_kick(self):
		while  True:
			kick = input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
			if not check_correct_value(kick):
				return int(kick)

	def set_protagonist_block(self):
		while True:
			block = input('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')
			if not check_correct_value(block):
				print("Your block " + str(block))
				return int(block)

	def set_antagonist_kick(self):
		kick = random.randint(1, 3)
		print('Enemy kick ' + str(kick))
		return kick

	def set_antagonist_block(self):
		return random.randint(1, 3)


def main():
	Settings.hello()
	win = False

	protagonist = Fight()
	while True:
		choise_of_option = input("Please select your warrior: 1 - strong, 2 - healthy, 3 - skill: ")
		if not check_correct_value(choise_of_option):
			protagonist.option = int(choise_of_option)
			protagonist.set_warrior()
			break
	print('Your warrior:', protagonist.name)

	antagonist = Fight()
	antagonist.option = random.randint(1, 3)
	antagonist.set_warrior()
	print('Your antagonist: ', antagonist.name)
	if protagonist > antagonist:
		print('You are stronger than your opponent \n')
	elif protagonist < antagonist:
		print('You are weaker than your opponent \n')
	else:
		print('You are equally strong \n')
	
	while True:
		print('Your warrior HP: ' + str(protagonist.health))
		print('Your antagonist HP: ' + str(antagonist.health))
		print('\n')		

		if protagonist.set_protagonist_kick() != antagonist.set_antagonist_block():
			print('You hit an opponent!')
			antagonist.health = antagonist.health - protagonist.get_damage()
		else:
			print('Opponent blocked you!')

		if protagonist.set_protagonist_block() != antagonist.set_antagonist_kick():
			print('Opponent hit you :( ')
			protagonist.health = protagonist.health - antagonist.get_damage()
		else:
			print('You blocked an opponent!')

		if protagonist.health <= 0:
			break

		if antagonist.health <= 0:
			win = True
			break

	Settings.win() if win else Settings.lose()


if __name__ == '__main__':
	main()