#This code had led me to the Gold league
#This is probably as far as you can go with a "simple" algorithm
#Next step is to recreate the game and go for a genetic algorithm

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
x = 0
y = 0
# game loop
while True:
    
    prevX = x
    prevY = y
    turn=0
    x = 0
    y = 0
    
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
    if prevX == 0:
        prevX = x
        prevY = y
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if next_checkpoint_dist < 1500: 
            thrust =30
    if next_checkpoint_dist < 650: 
        thrust =19
    else:
        thrust = 100
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    if abs(next_checkpoint_angle) < 50 and next_checkpoint_dist<2600 and ((next_checkpoint_x-8000)**2+(next_checkpoint_y-4500)**2)**0.5>3000:
            next_checkpoint_x = 9000
            next_checkpoint_y = 4500
            thrust = 30
    
    
    #boost when checkpoint distance is 7000 and angle is 0
    if next_checkpoint_dist > 7000 and next_checkpoint_angle == 0: #( -5 < next_checkpoint_angle < 5):
        thrust = "BOOST"
       
    print(str(next_checkpoint_x -(x-prevX)*3)+ " " + str(next_checkpoint_y -(y-prevY)*3) + " " + str(thrust))
