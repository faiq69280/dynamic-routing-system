from tkinter import *
from imps import astar_path 
import math 
import time

root = Tk()
frame = Frame(root)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
frame.grid(row=0, column=0, sticky="news")
grid = Frame(frame)
grid.grid(sticky="news", column=0, row=7, columnspan=2)
frame.rowconfigure(7, weight=1)
frame.columnconfigure(0, weight=1)





SOURCE_INIT = 1 
GOAL_INIT = 2 
OBSTACLES_PLACE = 3
START_ANIMATION = False
CURR_STATE = SOURCE_INIT 
start_coords = (-1,-1)
goal_coords = (-1,-1)


cell_types=[]

for i in range(0,40):
    cell_types.append(['None' for x in range(0,40)])


def transition(event,button,row,col):
    global CURR_STATE 
    global START_ANIMATION
    global cell_types
    global start_coords 
    global goal_coords   
    if CURR_STATE == SOURCE_INIT: 
      if cell_types[row][col] == 'None': 
         button.configure(bg = 'yellow')
         CURR_STATE = GOAL_INIT
         cell_types[row][col] = 'S' 
         start_coords = (row,col)
    if CURR_STATE == GOAL_INIT: 
       if cell_types[row][col] == 'None':
          button.configure(bg = 'green')
          CURR_STATE = OBSTACLES_PLACE
          START_ANIMATION = True
          cell_types[row][col] = 'G'
          goal_coords = (row,col) 
    if CURR_STATE == OBSTACLES_PLACE: 
       if cell_types[row][col] == 'None':  
          button.configure(bg = 'red')
          cell_types[row][col] = 'O'
       elif cell_types[row][col] == 'O': 
            button.configure(bg = 'white')
            cell_types[row][col] = 'None'
          








       

button_matrix = [] 
#example values
for x in range(40):
    button_list = [] 
    for y in range(40):
        btn = Button(frame)
        btn.grid(column=y, row=x, sticky="news")
        btn.bind('<Button-1>',lambda event,btn_arg = btn,row_arg = x, col_arg = y : transition(event,btn_arg,row_arg,col_arg))
        button_list.append(btn)
    button_matrix.append(button_list)
    


prev_path = [] 


def highlight_path(path_returned,button_matrix): 
    for i in range(1,len(path_returned)-1):
          cord = path_returned[i]
          button_matrix[cord[0]][cord[1]].configure(bg = 'blue')
     

def clear_path(path_returned,button_matrix,cell_types):
    for i in range(1,len(path_returned)-1):
          cord = path_returned[i]
          if cell_types[cord[0]][cord[1]] == 'None':
             button_matrix[cord[0]][cord[1]].configure(bg = 'white')
    


def animation_start_func(event):
     global start_coords
     global goal_coords 
     global cell_types
     global button_matrix
     global START_ANIMATION
     global prev_path 
     global CURR_STATE
     global root 

     if START_ANIMATION: 
       if len(prev_path) > 0: 
           clear_path(prev_path,button_matrix,cell_types)

        
       path_returned = astar_path(start_coords,goal_coords,40,cell_types)
       prev_path = path_returned
       highlight_path(path_returned,button_matrix)
       
       if len(path_returned) > 0:
          START_ANIMATION = False 
          pos = 1 
          (rs,cs) = path_returned[0]
          prev_coord = (rs,cs)
          while pos < len(path_returned): 
                (r,c) =  path_returned[pos]
                if cell_types[r][c] != 'O':
                   button_matrix[prev_coord[0]][prev_coord[1]].configure(bg = 'white')
                   cell_types[prev_coord[0]][prev_coord[1]] = 'None'
                   time.sleep(0.3)
                   button_matrix[r][c].configure(bg = 'yellow')
                   root.update() 
               
                   start_coords = (r,c)
                   cell_types[r][c] = 'S'            
                   prev_coord = (r,c) 
                   pos = pos + 1
                else:
                    clear_path(path_returned[pos-1:],button_matrix,cell_types)
                    path_returned = astar_path(prev_coord,goal_coords,40,cell_types)
                    highlight_path(path_returned,button_matrix)
                    pos = 1 
          START_ANIMATION = True
          if start_coords == goal_coords: 
              CURR_STATE = GOAL_INIT
              START_ANIMATION = False          
       
                  

        
           



       
   


frame.columnconfigure(tuple(range(40)), weight=1)
frame.rowconfigure(tuple(range(40)), weight=1)

root.bind('<Return>',animation_start_func)


root.mainloop()



#state 