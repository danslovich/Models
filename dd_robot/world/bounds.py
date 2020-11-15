#
# Author: Daniel Slovich
# 
# Creates 50mx50m world map with perimeter
# boxes 1 meter apart
#

import subprocess

# spawns box i at location x,y,z
def spawnBox(x=0, y=0, z=5, i=0):
    subprocess.call(['sh','/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', str(x), str(y), str(z), str(i)])


# spawns out of bounds perimeter
def spawnBounds():
    i   =   0
    x   = -25
    y   = -25
    z   =   5
    box =   0
    
    for i in range(0, 25): 
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', '-25', str(y), str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', '25', str(-y), str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', str(x), '25', str(z), str(box)])
        box=box+1
        subprocess.call(['sh', '/home/user/catkin_ws/src/dd_robot/scripts/box_spawn.sh', str(-x), '-25', str(z), str(box)])
        box=box+1
        x=x+2
        y=y+2
            

if __name__=="__main__":
    spawnBounds()



