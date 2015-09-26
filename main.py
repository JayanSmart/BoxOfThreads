"""
Multi-threaded balls bouncing in a box
Jayan Smart
26 Sept 2015
"""
from visual import *
import threading, time

def oneBall(rad, colr):
    dt = 0.1
    t = 0

    ball = sphere(pos=vector(0, 0, 0), radius=rad, color=colr)
    ball.M = 10
    ball.p = ball.M*vector(0, 3, 0)
    while (t<5):
        rate(10)

        fnet = vector(1,2,3)

        ball.p += fnet

        dr = (ball.p/ball.M)*dt
        ball.pos += dr
        t += dt
        print(ball.pos)


def main():
    # Constants
    t = 0
    dt = 0.1
    G = 6.67e-11

    # Objects
    #Walls
    wallLeft = box(pos=(-51, 0, 0), length=2, height=104, width=100, material=materials.wood)
    wallRight = box(pos=(51, 0, 0), length=2, height=104, width=100, material=materials.wood)
    wallTop = box(pos=(0, 51, 0), length=100, height=2, width=100, material=materials.wood)
    wallBottom = box(pos=(0, -51, 0), length=100, height=2, width=100, material=materials.wood)
    wallBack = box(pos=(0, 0, -51), length=104, height=104, width=2, material=materials.wood)

    threads = []
    for i in range(5):
        print("newThread")
        t1 = threading.Thread(target=oneBall, args=(4, color.blue))
        t2 = threading.Thread(target=oneBall, args=(3, color.green))

        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()
        print("This is done")




if __name__ == "__main__":
    main()