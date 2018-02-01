#Random Walk
import matplotlib.pyplot as plt
from random import choice
class RandomWalk():
    
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while(len(self.x_values) < self.num_points):
            
            #Decide the direction and distance in x and y
            x_direction = choice([1,-1])
            x_distance  = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance  = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            #pass if it do not move
            if x_step == 0 and y_step == 0:
                continue
                
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)

#Start a new random walk
rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))

#hide the axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    
#highlight the start and end point
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

#set the size
plt.figure(figsize=(10,6))
plt.show()
