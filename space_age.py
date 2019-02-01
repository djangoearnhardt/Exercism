print('How many years old are you?')
years = int(input())
e_seconds = years * 31557600
print('That means you are', e_seconds, 'seconds old on the planet Earth')
print("What other planet in our Solar System that you'd like to convert your age to?")
planet_result = str(input())
class SpaceAge():
	def __init__(self, seconds):
		self.seconds = seconds
	def mercury(self):
		return self.seconds * .2408467
	def venus(self):
		return self.seconds * .61519726
	def mars(self):	
		return self.seconds * 1.8808158
	def jupiter(self):
		return self.seconds * 11.862615
	def saturn(self):	
		return self.seconds * 29.447498
	def uranus(self):
		return self.seconds * 84.016846
	def neptune(self):
		return self.seconds * 164.79132
s = SpaceAge(e_seconds)

if planet_result.lower() == 'mercury':
	print('Your age on', planet_result, 'is',  s.mercury())
elif planet_result.lower() == 'venus':
	print('Your age on', planet_result, 'is', s.venus())
elif planet_result.lower() == 'mars':
	print('Your age on', planet_result, 'is', s.mars())
elif planet_result.lower() == 'jupiter':
	print('Your age on', planet_result, 'is', s.jupiter())
elif planet_result.lower() == 'saturn':
	print('Your age on', planet_result, 'is', s.saturn())
elif planet_result.lower() == 'uranus':
	print('Your age on', planet_result, 'is', s.uranus())
elif planet_result.lower() == 'neptune':
	print('Your age on', planet_result, 'is', s.neptune())
elif planet_result.lower() == 'pluto':
	print('Pluto may or may not be a planet. Sorry :(')
elif planet_result.lower() == 'earth':
	print('You already know your age in seconds on Earth')
else:
	print("That isn't a planet in our Solar System")
print('Thank you so much. Goodbye')
