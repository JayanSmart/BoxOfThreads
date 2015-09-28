"""
Multi-threaded balls bouncing in a box
Jayan Smart
26 Sept 2015
"""
from visual import *
import threading
import random


#This is a ball object
class OneBall:
    dt = 0.1
    t = 0
    rad = 0
    colr = (0, 0, 0)

    # this
    def __init__(self, rad, colr):
        self.rad = rad
        self.colr = colr

    def run(self):
        dt = 0.1
        t = 0
        col = self.colr
        radi = self.rad

        ball = sphere(pos=vector(0, 0, 0), radius=radi, color=col)
        ball.M = 10
        ball.p = ball.M * vector(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10,10))

        while t < 1000:  # This influences how long the simulation will run for
            rate(100)  # This influences how fast the simulation runs

            #fnet = vector(random.uniform(-3, 3), random.uniform(-3, 3), random.uniform(-3, 3))
            fnet = vector(0, 0, 0) # either this, or the line above must be commented out.
            ball.p += fnet

            dr = (ball.p / ball.M) * dt
            ball.pos += dr
            if ball.pos.x > 50 - radi:
                ball.pos -= dr
                dr.x = -dr.x
                ball.p.x = -ball.p.x
                ball.pos += dr
            if ball.pos.x < radi - 50:
                ball.pos -= dr
                dr.x = -dr.x
                ball.p.x = -ball.p.x
                ball.pos += dr

            if ball.pos.y > 50 - radi:
                ball.pos -= dr
                dr.y = -dr.y
                ball.p.y = -ball.p.y
                ball.pos += dr
            if ball.pos.y < radi - 50:
                ball.pos -= dr
                dr.y = -dr.y
                ball.p.y = -ball.p.y
                ball.pos += dr

            if ball.pos.z > 50 - radi:
                ball.pos -= dr
                dr.z = -dr.z
                ball.p.z = -ball.p.z
                ball.pos += dr
            if ball.pos.z < radi - 50:
                ball.pos -= dr
                dr.z = -dr.z
                ball.p.z = -ball.p.z
                ball.pos += dr

            t += dt


def get_force(ball1, ball2):
    G = 6.67e-11
    force = -G * ball1.M * ball2.M / ((ball2.pos - ball1.pos) ** 3 / mag(ball2.pos - ball1.pos))
    return force


def main():
    # Constants
    t = 0
    dt = 0.1

    # Walls
    wallLeft = box(pos=(-51, 0, 0), length=2, height=104, width=100, material=materials.wood)
    wallRight = box(pos=(51, 0, 0), length=2, height=104, width=100, material=materials.wood)
    wallTop = box(pos=(0, 51, 0), length=100, height=2, width=100, material=materials.wood)
    wallBottom = box(pos=(0, -51, 0), length=100, height=2, width=100, material=materials.wood)
    wallBack = box(pos=(0, 0, -51), length=104, height=104, width=2, material=materials.wood)

    threads = []
    for i in range(10):
        print("newThread")
        b1 = OneBall(random.randint(1, 5), (random.random(), random.random(), random.random()))
        t1 = threading.Thread(target=b1.run, args=())
        threads.append(t1)
        t1.start()
        # time.sleep(0.5)
    print("Main is done")


if __name__ == "__main__":
    main()
