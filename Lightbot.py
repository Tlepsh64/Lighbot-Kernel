# level 1 terrain: write column by column, ex: [ [0,1,0], [2,1,0] ] is a 2x3 terrain
height = [ [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0] ]

isBlue = [ [True,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,True] ]

isOn = [ [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,False], [False,False,False,True] ]

# start by intializing the lightbot status variables
x = 0 # position x coordinate
y = 0 # position y coordinate
yon = 0 # which way our lbot is facing
direction = { 0:"north", 1:"east", 2:"south", 3:"west" }

maxX = len(height) - 1 # max possible value of the x coordinate
maxY = len(height[0]) - 1 # max possible value of the y coordinate

def heightDifferenceForward():
    """ A function to compute the difference between the current box that the lightbot is occupying, and the box it is facing. """
    
    if yon == 0 and y < maxY:
        return height[x][y+1] - height[x][y]
    
    elif yon == 2 and y > 0:
        return height[x][y-1] - height[x][y]
    
    elif yon == 1 and x < maxX:
        return height[x+1][y] - height[x][y]
    
    elif yon == 3 and x > 0:
        return height[x-1][y] - height[x][y]
    
     # return 0 # Why do we return zero? Doesn't this mean that the above codes are all gonna be useless?

komut = ""

while komut != "q": # repeat as long as we don't get the quit command
    
    print("Enter a command for lbot")
    komut = raw_input()
    
    if komut == ">" :
        print("I am turning right")
        yon = (yon + 1) % 4
    
    elif komut == "<" :
        print("I am turning left")
        yon = (yon-1) % 4
    
    elif komut == "^" :
        
        if yon == 0: # if we are facing north
            if y < maxY: # check we are not at the top row
                y = y + 1
            elif y == maxY: # This code snippet(s.look below) may not be needed, but I thought it would be smart to remind us that we are at the borders of the game's terrain.
                y = y
                
        if yon == 2: # if we are facing south
            if y > 0: # check we are not at the bottom row
                y = y - 1  
            elif y == 0:
                y = y
            
        if yon == 1: # if we are facing east
            if x < maxX: # check we are not at the rightmost column
                x = x + 1
            elif x == maxX:
                x = x
        
        if yon == 3: # if we are facing west
            if x > 0: # check we are not at the leftmost column
                x = x - 1
            elif x == 0:
                x = x
                
    elif komut == "@" :
        
        if ( isBlue[x][y] == True ):
            print("I am switching on or off")
            
            if ( isOn[x][y] == True ):
                isOn[x][y] = False
            
            else:
                isOn[x][y] = True
        
        else:
            print("Y'all are a-tryin' ta laheet up ayy gray box. I can't do it")
            
    elif komut != "q":
        print("This command is not known")
        
print("As I exit now, my orientation is ", direction[yon])
