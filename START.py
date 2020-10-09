from concat import *
import os


seed = 1
world_size = 100000000
x = world_size/2
y = world_size/2

terrain_p = 0.7
features_p = 0.3
vegetation_p = 0.75
constructions_p = 0.3
reg_p = 0.1

time_step = 30
time = 870
day_prev = 1
day = 1

reg_prev = random.choice(names_reg)
reg_type_prev = random.choice(types_reg)
constr_visited = False
random.seed(seed)
	
os.system("clear")
print_intro(reg_prev, reg_type_prev)
print_day(day)

while True:
	while True : 
		inp = input("│ » ").strip()
		
		if (inp == "n" or inp == "north"):
			x = x+1
		elif (inp == "s" or inp == "south"):
			x = x-1
		elif (inp == "e" or inp == "east"):
			y = y+1
		elif (inp == "w" or inp == "west"):
			y = y-1
		elif (inp == "ne" or inp == "north east"):
			x = x+1
			y = y+1
		elif (inp == "se" or inp == "south east"):
			x = x-1
			y = y+1
		elif (inp == "nw" or inp == "north west"):
			x = x+1
			y = y-1
		elif (inp == "sw" or inp == "south west"):
			y = y-1
			x = x-1
		elif inp == "info":
			print_prompt()
		elif inp == "quit":
			quit()
		else :
			break
			
		seed = x+world_size*y
		
		#date
		result = date_time(
			day_prev, day, 
			time, time_step)
		day = result["day"]
		day_prev = result["day_prev"]
		time = result["time"]
		
		#regions
		result = print_reg(
			seed,
			reg_p, 
			time,
			reg_prev,
			reg_type_prev)
			
		reg_p = result["reg_p"]
		reg_prev = result["reg_prev"]
		reg_type_prev = result["reg_type_prev"]
		
		#scenery
		if random.random() < 0.5 :
			#constructions
			result = print_constructions(
				seed,
				time,
				constructions_p,
				constr_visited)
				
			constr_visited = result["constr_visited"]
			
		else: 
			#terrain
			result = print_terrain(
				seed,
				time,
				terrain_p,
				constr_visited,)
			
			constr_visited = result
		
		#features
		print_features(
			seed,
			features_p,
			time
			)
	
