


import math 




def h(p1,p2): 
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def astar_path(source_coords,goal_coords,grid_size,cell_types):
   g = dict() 
   g[source_coords] = 0

   p = dict()
   p[source_coords] = None 
   p[goal_coords] = None

   open = list() 
   close  = list() 
   open.append(source_coords)
   while len(open) > 0: 
       curr = min(open,key = lambda k : g[k]+h(k,goal_coords))
       if curr == goal_coords: 
           break 
       open.remove(curr)
       close.append(curr)
       #generate neighbours of curr 
       neighbours = list() 
       moves = [1,0,-1]
       for moveRow in moves: 
           for moveCol in moves: 
               if ((moveCol != 0 and moveRow == 0) or (moveRow != 0 and moveCol == 0)) and (curr[0] + moveRow >= 0 and curr[0] + moveRow < grid_size) and (curr[1] + moveCol >= 0 and moveCol + curr[1] < grid_size) and cell_types[curr[0]+moveRow][curr[1]+moveCol] != 'O':
                   neighbours.append((curr[0]+moveRow,curr[1]+moveCol))
       for n in neighbours: 
         if not n in close: 
           if n in open: 
              if g[curr] + 1 + h(n,goal_coords) < g[n] + h(n,goal_coords): 
                 g[n] = g[curr] + 1
                 p[n] = curr
           else: 
               g[n] = g[curr] + 1 
               p[n] = curr
               open.append(n)

   path = list() 
   if p[goal_coords] != None:
    node = goal_coords
    
    path.append(node)
    node = p[node] 
    while node != None: 
         path.append(node) 
         node = p[node] 
    path.reverse()


   return path 












       





#cell_types = [['S','O','G'],
#['None','O','None'],
#['None','None','None']
#]


#print(astar_path((0,0),(0,2),3,cell_types))
