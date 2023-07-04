#This code has led me to the gold league
#It is probably the highest level you can reach with a "simple" algorithm
#Next step would be to simulate the game and select moves based on a simulated genetic algorithm solution

import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

def distance(x,y):
    return (x**2+y**2)
    
def postion_future(x,y,x_ent,y_ent,my_team_id):
    a = (y-y_ent)/(x-x_ent)
    b = y-a*x
    if my_team_id == 0 and (16000*a + b)> 2200 and (16000*a + b) < 5300:
        return True
    elif my_team_id == 1 and b > 2200 and b < 5300:
        return True
    else:
        return False
    
def get_valeur(liste,i):
    for j in range(len(liste)):
        id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent = liste[j]
        if id_ent == i:
            return(id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent)
            
my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

# game loop
while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    
    my_wizards = []
    his_wizards = []
    
    snaffles = []
    bludgers = []
    
    for i in range(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise
        entity_id, entity_type, x, y, vx, vy, state = input().split()
        entity_id = int(entity_id)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        state = int(state)
        
        if entity_type == "WIZARD":
            my_wizards.append([entity_id,x,y,vx,vy,state])
        elif entity_type == "OPPONENT_WIZARD":
            his_wizards.append([entity_id,x,y,vx,vy,state])
        elif entity_type == "SNAFFLE":
            snaffles.append([entity_id,x,y,vx,vy,state])
        else:
            bludgers.append([entity_id,x,y,vx,vy,state])
        
        if my_magic >= 20:
            sort = True
        else:
            sort = False
            
    snaffles_libres = []
    
    for j in range(len(snaffles)):
        id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent = snaffles[j]
        if state_ent == 0:
            snaffles_libres.append([id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent])
    
    if my_magic >= 20:
        magie = True 
    else:
        magie = False
    
    x_min = 16001
    petrificus = False
    id_a_petrifier = -1
    
    for j in range(len(snaffles_libres)):
        id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent = snaffles_libres[j]
        if my_team_id == 0 and x_ent+2*vx_ent <0 and x > 0:
            petrificus = True
            id_a_petrifier = id_ent
        elif my_team_id == 1 and x_ent + 2*vx > 16000 and x < 16000:
            petrificus = True 
            id_a_petrifier = id_ent
        
    
    for i in range(2):
        
        entity_id,x,y,vx,vy,state = my_wizards[i]
        
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)
        if state == 0:
            if len(snaffles_libres) >= 1:
                distance_minimale = 999999999999999999999
                for j in range(len(snaffles_libres)):
                    id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent = snaffles_libres[j]
                    if (distance(x-x_ent,y-y_ent) < distance_minimale):
                        distance_minimale = distance(x-x_ent,y-y_ent)
                        aller_vers = id_ent
                id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent = get_valeur(snaffles_libres,aller_vers)
                snaffles_libres.remove([id_ent,x_ent,y_ent,vx_ent,vy_ent,state_ent])
                dx = x - x_ent
                if petrificus and my_magic >= 10:
                    print("PETRIFICUS "+str(id_a_petrifier))
                    petrificus = False
                    my_magic += -10
                elif my_team_id == 0 and dx <0 and magie and postion_future(x,y,x_ent,y_ent,my_team_id):
                    print("FLIPENDO "+str(id_ent))
                    my_magic += -20
                elif my_team_id == 1 and dx >0 and magie and postion_future(x,y,x_ent,y_ent,my_team_id):
                    print("FLIPENDO "+str(id_ent))
                    my_magic += -20
                elif my_team_id == 0 and dx >0 and magie:
                    print("ACCIO "+str(id_ent))
                    my_magic += -20
                elif my_team_id == 1 and dx < 0 and magie:
                    print("ACCIO "+str(id_ent))
                    my_magic += -20
                else:
                    print("MOVE "+ str(x_ent)+ " "+str(y_ent)+" 150")
            else:
                if my_team_id == 1:
                    print("MOVE 16000 3750 150")
                else:
                    print("MOVE 0 3750 150")
        else:
            if len(snaffles_libres) == 0:
                if x > 14000 and y > 2000 and y < 5000:
                    if my_team_id == 0:
                        print("THROW 16000 3750 500")
                    else:
                        print("THROW 0 3750 500")
                else:
                    if my_team_id == 0:
                        print("THROW 16000 3750 400")
                    else:
                        print("THROW 0 3750 400")
            else:
                if my_team_id == 0:
                    print("THROW 16000 3750 500")
                else:
                    print("THROW 0 3750 500")
        # Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500)
        # i.e.: "MOVE x y thrust" or "THROW x y power"
        
