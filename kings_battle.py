#! /usr/bin/python3

import sys
import random

"""
	Kings Battle is game about war between men and machines.
"""

def chech_correct_value(choise_of_option):
	while True:
		if not choise_of_option.isdigit() or not int(choise_of_option) in (1, 2, 3):
			print('Please, enter the correct value')
			return True
		else:
			return False

class Settings():
	"""Set base messages"""
	def hello():
		print("Welcome to Battle!!!")

	def win():
		print("You win!")

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

	def set_warrior(self):
		if self.option == 1:
			self.name = 'strong'
			self.power = int(self.power * 1.5)
		elif self.option == 2:
			self.name = 'healthy'
			self.health = int(self.health * 1.5)
		elif self.option == 3:
			self.name = 'skill'
			self.skill = self.skill * 1.5


class Fight(Warrior):
	"""Game function"""
	def __init__(self, option = None, name = '', power = 10, skill = 1.0, health = 100):
		super().__init__(option, name, power, skill, health)

	def set_damage(self):
		return (self.power * self.skill)

	def set_protagonist_kick(self):
		while  True:
			kick = input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = ')
			if not chech_correct_value(kick):
				return kick

	def set_protagonist_block(self):
		while True:
			block = input('Please select block: 1 - to head, 2 - to body, 3 - to foot = ')
			if not chech_correct_value(block):
				print("your block " + str(block))
				return block

	def set_antagonist_kick(self):
		kick = random.randint(1, 3)
		print('Enimal kick ' + str(kick))
		return kick

	def set_antagonist_block(self):
		return random.randint(1, 3)


def main():
	Settings.hello()
	win = False

	protagonist = Fight()
	while True:
		choise_of_option = input("Please select your warrior: 1 - strong, 2 - healthy, 3 - skill: ")
		if not chech_correct_value(choise_of_option):
			protagonist.option = int(choise_of_option)
			protagonist.set_warrior()
			break
	print('Your warrior:', protagonist.name)

	antagonist = Fight()
	antagonist.option = random.randint(1, 3)
	antagonist.set_warrior()
	print('Your antagonist: ', antagonist.name)
	
	while True:
		print('Your warrior HP: ' + str(protagonist.health))
		print('Your antagonist HP: ' + str(antagonist.health))
		print('\n')

		if int(protagonist.set_protagonist_kick()) != int(antagonist.set_antagonist_block()):
			print('You hit an opponent!')
			antagonist.health = antagonist.health - protagonist.set_damage()
		else:
			print('Opponent blocked you!')

		if int(protagonist.set_protagonist_block()) != int(antagonist.set_antagonist_kick()):
			print('Opponent hit you :( ')
			protagonist.health = protagonist.health - antagonist.set_damage()
		else:
			print('You blocked an opponent!')

		if protagonist.health <= 0:
			break

		if antagonist.health <= 0:
			win = True
			break

	if win:
		Settings.win()
	else:
		Settings.lose()


if __name__ == '__main__':
	main()