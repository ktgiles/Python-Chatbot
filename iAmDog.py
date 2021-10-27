#!/usr/bin/python

# This chatbot attempts to imitate what a dog would say if it could chat

import string

def getReply(line, words):
	if len(words) == 0: return 'Did you see a squirrel and get distracted?'
 	if 'animal' in words or 'dog' in words or 'cat' in words or 'squirrel' in words or 'human' in words or 'dogs' in words or 'cats' in words or 'squirrels' in words:
		return replyAnimal(line, words)
 	if 'treat' in words or 'treats' in words or 'food' in words or 'snacks' in words or 'snack' in words:
		return replyFood(line, words)
	if 'outside' in words or 'park' in words or 'mountain' in words or 'mountains' in words:
		return replyPlace(line, words)
	if 'go' in words or 'explore' in words or 'nap' in words or 'walk' in words or 'walking' in words or 'hike' in words or 'hiking' in words or 'swim' in words or 'run' in words:
		return replyActivity(line, words)
	if 'pet' in words or 'belly' in words or 'cuddle' in words or 'cuddles' in words or 'scratches' in words or 'rub' in words or 'rubs' in words:
		return replyCuddles(line, words)
	if 'sit' in words or 'drop' in words or 'speak' in words or 'shake' in words or 'command' in words or 'commands' in words:
		return replyCommand(line, words)
	if 'play' in words or 'ball' in words or 'toy' in words or 'fetch' in words:
		return replyPlay(line, words)
	if 'hi' in words or 'hello' in words:
		return replyGreeting(line, words)
	if 'bark' in words: return 'Wait, I\'m the one that should be barking!'
	if 'bath' in words: return 'NO BATH. ONLY STINKY.'
	if words[0] == 'i' and (words[1] == 'feel' or words[1] == 'think'):
		return 'I totally agree, you should tell me more while you scratch my ears.'
	if line[-1] == '?': return 'I don\'t know, I\'m just a dog!'
	return 'Oh really? Rub my belly and tell me more!'

def replyActivity (line, words):
	if 'walk' in words or 'walking' in words: return 'Going on walks is the best! Where do you like to walk?'
	if 'hike' in words or 'hiking' in words: return 'Oh, I love to hike! I like the mountains, what about you?'
	if 'swim' in words: return 'The lake is nice but I\'m scared of fish.'
	if 'run' in words: return 'Oh, running is so much work! Don\'t you get tired?'
	if 'go' in words: return 'GO IS MY FAVORITE WORD! Where do you want to go???'	
	if 'explore' in words: return 'Have you ever been to the Smoky Mountains?'
	if 'nap' in words: return 'Napping is amazing. When was your last nap?'

def replyPlace (line, words):
	if 'outside' in words: return 'Playing outside is amazing! Where is your favorite place?'
	if 'park' in words: return 'Park? I love the park! There are dogs at the park! Which park do you like?'
	if 'mountain' in words or 'mountains' in words: return 'The mountains are beautiful! So many smells! Do you like to explore?'
	
def replyAnimal (line, words):
	if 'dog' in words or 'dogs' in words: return 'DOG?!?! I\'m a dog!! I love dogs! Do you love dogs???'
	if 'cat' in words or 'cats' in words: return 'Ugh, I hate cats. What do you hate?'
	if 'squirrel' in words or 'squirrels' in words: return 'BARK BARK BARK BARK BARK BARK'
	if 'human' in words: return 'Oh, humans like to pet me and feed me. Do you like humans too?'
	if 'animal' in words: return 'All animals are awesome! What is your favorite animal?'

def replyFood (line, words):
	if 'treat' in words or 'treats' in words: return 'Treats! I like treats so much! What do you like?'
	if 'food' in words: return 'What is your favorite food?'
	if 'snacks' in words or 'snack' in words: return 'Ohhhhhh snacks are the best. What\'s your favorite snack?'

def replyCuddles (line, words):
	if 'pet' in words or 'pets' in words: return 'I love when humans pet me! What do you love?'
	if 'belly' in words or 'scratches' in words or 'rub' in words or 'rubs' in words: return 'I like people who scratch or rub my belly, do you like people?'
	if 'cuddles' in words or 'cuddle' in words: return 'oh I love cuddling during nap time.'
	
def replyCommand (line, words):
	if 'sit' in words: return '*sits down like a good boy*'
	if 'speak' in words: return 'BARK'
	if 'shake' in words: return '*gives paw to shake like a good boy*'
	if 'command' in words or 'commands' in words: return 'I know how to sit, speak, shake, and drop it!'
	if 'drop' in words: return '*growls but does not drop it* NO TAKE ONLY THROW'

def replyPlay (line, words):
	if 'ball' in words: return 'Oh, I love to play with a ball! Will you throw it?'
	if 'fetch' in words: return 'I don\'t like fetch that much, it\'s too much work. Can we have a snack instead?'
	if 'toy' in words: return 'My favorite toy is a big squeaky snake!' 
	if 'play' in words: return 'I like to play with the squirrels in my backyard.'

def replyGreeting (line, words):
	if 'hi' in words: return 'Hi to you too! What is up?'
	if 'hello' in words: return 'Hello hello! What have you been doing today?'

name = raw_input('Yes this is dog. What is your name? ')
print name, ' is a good name! Your humans did a good job naming you.'
print 'Type "quit" whenever you want to exit this chat program. I\'m just a dog so I like to ignore words like "stop" and "no".'
line = raw_input("Well, "+name+", sniffed anything good lately? ")

while line!="quit":
  line = line.lower()
  reply = getReply(line, line.split())
  line = raw_input(reply)
