from mcpi.minecraft import Minecraft
from mcpi import*

mc = Minecraft.create()
air = 0
stone = 1
iron = 42
dirt = 3
gold = 41
wood = 5
leaf = 18
door = 64
stonebrick = 98

x, y, z = mc.player.getTilePos()                                                  
x, y, z = mc.player.getPos()  


def makenose():
	#mc.setBlocks(x,y-13,z,x,y,z, wood)
	mc.setBlocks(x+13,y,z+25,x,y,z+26, wood)
	mc.setBlocks(x-13,y,z+25,x,y,z+26, wood)#circle cross
	#mc.setBlocks(x+3,y+13,z,x-3,y+13,z, stonebrick) #up
	mc.setBlocks(x+3,y-13,z+25,x-3,y-13,z+26, wood) #down
	mc.setBlocks(x+13,y+3,z+25,x+13,y-3,z+26, wood) #right
	mc.setBlocks(x-13,y+3,z+25,x-13,y-3,z+26, wood) #left

	mc.setBlocks(x+12,y-6,z+25,x+12,y-3,z+26, wood) #6 #lower left
	mc.setBlocks(x+11,y-8,z+25,x+11,y-6,z+26, wood) #8
	mc.setBlocks(x+10,y-9,z+25,x+10,y-7,z+26, wood) #9 
	mc.setBlocks(x+9,y-10,z+25,x+9,y-8,z+26, wood) #10
	mc.setBlocks(x+8,y-11,z+25,x+8,y-10,z+26, wood) #11
	mc.setBlocks(x+7,y-12,z+25,x+7,y-11,z+26, wood) #12
	mc.setBlocks(x+6,y-13,z+25,x+6,y-11,z+26, wood) #13
	mc.setBlocks(x+5,y-13,z+25,x+5,y-12,z+26, wood) #13


	mc.setBlocks(x-12,y-6,z+25,x-12,y-3,z+26, wood) #6 #lower right
	mc.setBlocks(x-11,y-8,z+25,x-11,y-6,z+26, wood) #8
	mc.setBlocks(x-10,y-9,z+25,x-10,y-7,z+26, wood) #9
	mc.setBlocks(x-9,y-10,z+25,x-9,y-8,z+26, wood) #10
	mc.setBlocks(x-8,y-11,z+25,x-8,y-10,z+26, wood) #11
	mc.setBlocks(x-7,y-12,z+25,x-7,y-11,z+26, wood) #12
	mc.setBlocks(x-6,y-13,z+25,x-6,y-11,z+26, wood) #13
	mc.setBlocks(x-5,y-13,z+25,x-5,y-12,z+26, wood) #13
	
def small():	
	m = 0	
	while m < 14:
		if x-12+m<=x: 
			mc.setBlocks(x-12+m,y-6+m,z+25+m,x-12+m,y-3+m,z+26+m, wood) #6 #lower right
		if x-11+m<=x: 
			mc.setBlocks(x-11+m,y-8+m,z+25+m,x-11+m,y-6+m,z+26+m, wood) #8
		if x-10+m<=x: 
			mc.setBlocks(x-10+m,y-9+m,z+25+m,x-10+m,y-7+m,z+26+m, wood) #9
		if x-9+m<=x:
			mc.setBlocks(x-9+m,y-10+m,z+25+m,x-9+m,y-8+m,z+26+m, wood) #10
		if x-8+m<=x:
			mc.setBlocks(x-8+m,y-11+m,z+25+m,x-8+m,y-10+m,z+26+m, wood) #11
		if x-7+m<=x:
			mc.setBlocks(x-7+m,y-12+m,z+25+m,x-7+m,y-11+m,z+26+m, wood) #12
		if x-6+m<=x:
			mc.setBlocks(x-6+m,y-13+m,z+25+m,x-6+m,y-11+m,z+26+m, wood) #13
		if x-5+m<=x:
			mc.setBlocks(x-5+m,y-13+m,z+25+m,x-5+m,y-12+m,z+26+m, wood) #13
		
		if x+13-m>=x: 
			mc.setBlocks(x+13-m,y+m,z+25+m,x,y+m,z+26+m, wood)
		if x-13+m<=x:
			mc.setBlocks(x-13+m,y+m,z+25+m,x,y+m,z+26+m, wood)#circle cross
		#if x+13-m>=x: 
			#mc.setBlocks(x+4-m,y-13+m,z+m,x-4+m,y-13+m,z+1+m, wood) #down
		if x+13-m>=x: 
			mc.setBlocks(x+13-m,y+3+m,z+25+m,x+13-m,y-3+m,z+26+m, wood) #right
		if x-13+m<=x:
			mc.setBlocks(x-13+m,y+3+m,z+25+m,x-13+m,y-3+m,z+26+m, wood) #left
			#fix the if statements. Add the M's
		if x+12-m>=x: 
			mc.setBlocks(x+12-m,y-6+m,z+25+m,x+12-m,y-3+m,z+26+m, wood) #6 #lower left
		if x+11-m>=x:
			mc.setBlocks(x+11-m,y-8+m,z+25+m,x+11-m,y-6+m,z+26+m, wood) #8
		if x+10-m>=x:
			mc.setBlocks(x+10-m,y-9+m,z+25+m,x+10-m,y-7+m,z+26+m, wood) #9 
		if x+9-m>=x:
			mc.setBlocks(x+9-m,y-10+m,z+25+m,x+9-m,y-8+m,z+26+m, wood) #10
		if x+8-m>=x:
			mc.setBlocks(x+8-m,y-11+m,z+25+m,x+8-m,y-10+m,z+26+m, wood) #11
		if x+7-m>=x:
			mc.setBlocks(x+7-m,y-12+m,z+25+m,x+7-m,y-11+m,z+26+m, wood) #12
		if x+6-m>=x:
			mc.setBlocks(x+6-m,y-13+m,z+25+m,x+6-m,y-11+m,z+26+m, wood) #13
		if x+5-m>=x:
			mc.setBlocks(x+5-m,y-13+m,z+25+m,x+5-m,y-12+m,z+26+m, wood) #13
		m = m + 1
		
def low():
	j = 0
	while j < 6:
		if x+5-j>=x: 
			mc.setBlocks(x+4-j,y-13+j,z+25+j,x-4+j,y-13+j,z+26+j, wood) #down
		j = j + 1	
		
makenose()
small()
low()
