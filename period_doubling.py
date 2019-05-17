import numpy as np
import sys
import copy
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

r = 2.4
samples = 10
y_inits = []
for next_y in range(samples):
    y_inits.append([random.uniform(0.00001, .999999)])
y_copy = copy.deepcopy(y_inits)


def refresh_y():
    global y_inits
    #print(y_inits)
    #print(y_copy)
    y_inits = []
    y_inits = copy.deepcopy(y_copy)

def log_map(prev):
    next = r*prev*(1-prev)
    return next

fig, ax = plt.subplots(figsize = (15,15))
ax.set_xlim([0, 20])
ax.set_ylim([-.5, 1])

lines = []
for new_line in range(len(y_inits)):
    line, = ax.plot([],[], lw=2)
    lines.append(line)
text_r = plt.text(10, -.2, "r parameter: " + str(r))

def init():
    for line in lines:
        line.set_data([],[])
    text_r.set_text("r parameter: " + str(r) + " step: 0")
    return (text_r,) + tuple(lines)

def animate(i):
    global r
    global y_inits
    if i == 0:
        r = 2.4
    #chaos occurs at 3.56995
    #this is set up to slowly approach that in a pretty way
    r = r+(.1*(3.56995-r))
    if i > 95:
        r = 3.56995
    counter = 0
    for y in y_inits:
        for next_val in range(99): 
            y.append(log_map(y[len(y)-1]))
            if np.isinf(y[len(y)-1]):
                if y[len(y)-1] < 0:
                    y[len(y)-1] = sys.float_info.max*-1.0
                else:
                    y[len(y)-1] = sys.float_info.max*1.0
        #print(len(y_copy[0]))
        #print(len(y))
        lines[counter].set_data(np.linspace(0.0, 100.0, num = 100), y)
        refresh_y()
        counter += 1

    text_r.set_text("r parameter: " + str(r) + " step: " + str(i))
    return (text_r,) + tuple(lines)

# instantiate the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=500, blit=True)

anim.save('test2.mp4', fps=10)

plt.show()
