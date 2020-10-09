import random
import textwrap
from strings import *
from datetime import timedelta

width = 48 #for mobile screen
#width = 200 #for tts


tw_intro = textwrap.TextWrapper(
	width, 
	initial_indent="╭",
	subsequent_indent="│")

tw_ind = textwrap.TextWrapper(
	width, 
	initial_indent="  ",
	subsequent_indent="  ")
	
tw_ni = textwrap.TextWrapper(
	width, 
	initial_indent="",
	subsequent_indent="")

tw_mid = textwrap.TextWrapper(
	width, 
	initial_indent="│",
	subsequent_indent="│")
	
tw_init = textwrap.TextWrapper(
	width, 
	initial_indent="╭",
	subsequent_indent="│")
	
tw_cont = textwrap.TextWrapper(
	width, 
	initial_indent="│",
	subsequent_indent="│")

tw_subs = textwrap.TextWrapper(
	width, 
	initial_indent="│",
	subsequent_indent="│")

def date_time(
	day_prev, day, 
	time, time_step):
		
	if day != day_prev :
		print_day(day)
		day_prev = day
		
	time = time + time_step 
	if time >= 1440 :
		day = day+1
		time = 0
	
	if (time == 1440/8*1 or time == 1440/8*2
		or time == 1440/8*3 or time == 1440/8*4
		or time == 1440/8*5 or time == 1440/8*6
		or time == 1440/8*7 or time == 1440/8*8):
		
		print_sun_pos(time)
	
	return {
		"day_prev" : day_prev,
		"day" : day,
		"time" : time,
	}

def print_intro(
	reg_prev, 
	reg_type_prev):

	s = tw_intro.wrap(
		"Your adventure begins as you"+" "+
		"embark from your dwelling in"+" "+
		reg_prev+" "+
		reg_type_prev+" "+
		"to the Wild Randomness. Type info for help.")
	
	for el in s:
		print(el)
		
def print_prompt():

	s1 = tw_ni.wrap(
		"╰────────────────────────────╮"
	)
	s2 = tw_ind.wrap(
		"Type e, w, s, n, to move.  │"
	)
	s2_1 = tw_ind.wrap(
		"Also try se, sw, nw, ne.   │"
	)
	s2_2 = tw_ind.wrap(
		"Quit to close the game.    │"
	)
	s3 = tw_ni.wrap(
		"╭────────────────────────────╯"
	)
	
	for el in s1:
		print(el)
	for el in s2:
		print(el)
	for el in s2_1:
		print(el)
	for el in s2_2:
		print(el)
	for el in s3:
		print(el)


def print_sun_pos(
	time):
	
	if time == 1440/8*8:
		s = tw_cont.wrap(
			"It is midnight"
			)
	elif time == 1440/8*7:
		s = tw_cont.wrap(
			"The night falls"
			)
	elif time == 1440/8*6:
		s = tw_cont.wrap(
			"The sun begins to set"
			)
	elif time == 1440/8*5:
		s = tw_cont.wrap(
			"The sun is high in the western sky"
			)
	elif time == 1440/8*4:
		s = tw_cont.wrap(
			"It is noon"
			)
	elif time == 1440/8*3:
		s = tw_cont.wrap(
			"The sun is rising higher in the east"
			)
	elif time == 1440/8*2:
		s = tw_cont.wrap(
			"The sun appears on the eastern horizon"
			)
	elif time == 1440/8*1:
		s = tw_cont.wrap(
			"The night is deep and dark"
			)
	else:
		return
	
	print_time(time)
	for el in s:
		print(el)
		
		
def print_day(day):
	
	shift = len(str(day))
	offset = 1
	s1 = tw_ni.wrap(
		"╰───────"+"─"*shift+"───────╮"
	)
	s2 = tw_ind.wrap(
		"It is day "+
		str(day)+". "+
		offset*" "+
		"│"
	)
	s3 = tw_ni.wrap(
		"╭───────"+"─"*shift+"───────╯"
	)
	
	for el in s1:
		print(el)
	for el in s2:
		print(el)
	for el in s3:
		print(el)

def print_time(time):
	s = tw_init.wrap(
		"It is currently "+
		str(timedelta(minutes=time))[:-6]+" "+
		"hours"+" "+
		#"and"+" "+
		#str(timedelta(minutes=time))[3:5]+" "+
		#"minuted"+" "+
		"o'clock"+". ")
	
	print("╰")
	for el in s:
		print(el)

def print_reg(
	seed, 
	reg_p, 
	time,
	reg_prev,
	reg_type_prev):
	
	random.seed(seed+7439075)
	if random.random() < reg_p :
		print_time(time)
		
		s1 = tw_ni.wrap(
			"╰──────────────────────────────────────────────╯"
		)
		s2 = tw_ind.wrap(
			"You have left the"+" "+
			reg_prev+" "+
			reg_type_prev+". "
			)
		
		reg_prev = random.choice(names_reg)
		reg_type_prev = random.choice(types_reg)
		
		s3 = tw_ind.wrap(
			"The land before you is"+" "+
			reg_prev+" "+
			reg_type_prev+". "
			)
		
		s4 = tw_ni.wrap(
			"╭──────────────────────────────────────────────╮"
		)
		
		for el in s1:
			print(el)
		for el in s2:
			print(el)
		for el in s3:
			print(el)
		for el in s4:
			print(el)
		
	return {
		"reg_p" : reg_p,
		"reg_prev" : reg_prev,
		"reg_type_prev" : reg_type_prev,
	}
	

		
def print_constructions(
	seed, 
	time,
	constructions_p,
	constr_visited):
	
	random.seed(seed+9437906)
	if random.random() < constructions_p:
			
		print_time(time)
		constr = random.choice(constructions_type)
		s1 = tw_cont.wrap(
			"You"+" "+
			random.choice(spot_verb)+" "+
			random.choice(constructions_word)+" "+
			constr+". "+
			random.choice(explore_verb)+" "+
			"the"+" "+
			constr+" "+
			random.choice(after_word)+" "+
			random.choice(action_done)+" "+
			"and"+" "+
			random.choice(action_verb_ing)+" "+
			"you"+" "+
			random.choice(walk_verb)+". "
			)
			
		for el in s1:
			print(el)
		
		constr_visited = True
		
	else : 
		s3 = tw_cont.wrap(
			random.choice(scenery_generic)+". "
			)

		for el in s3:
			print(el)
	
	return {
		"constr_visited" : constr_visited,
	}
	
	
def print_features(
	seed, 
	features_p, 
	time
	):
	
	random.seed(seed+184348)
	if random.random() < features_p :
			
		#print_time(time)
		s1 = tw_cont.wrap(
			"There is"+" "+
			random.choice(natural_features_type)+" "+
			random.choice(prox_word)+". "
			)
		
		for el in s1:
			print(el)
		
	else :
		s4 = tw_cont.wrap(
			random.choice(features_generic)+". "
			)
			
		for el in s4:
			print(el)
	
def print_terrain(
	seed, 
	time,
	terrain_p,
	constr_visited,
	):
	
	random.seed(seed+195320)
	if (random.random() < terrain_p 
		and constr_visited == False):
		
		#print_time(time)
		s1 = tw_cont.wrap(
			"You"+" "+
			random.choice(arrival_verbs)+". "+
			"The"+" "+
			random.choice(terrain_word)+" "+
			"is"+" "+
			random.choice(terrain_type)+" "+
			"and"+" "+
			random.choice(vegetation_type)+" "+
			"are"+" "+
			random.choice(vegetation_word)+" "+
			random.choice(prox_word)+". "+
			"You are"+" "+
			random.choice(action_verb_ing)+" "+
			random.choice(after_word)+" "+
			"you"+" "+
			random.choice(walk_verb)+". "
			)
		
		for el in s1:
			print(el)
	
	else : 
		constr_visited = False
	
		s4 = tw_cont.wrap(
			random.choice(features_generic)+". "
			)
			
		for el in s4:
			print(el)
			
	return (constr_visited)
