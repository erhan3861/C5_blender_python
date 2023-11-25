from ursina import *
import random
from ursina.shaders import basic_lighting_shader as bls
from ursina import curve



def update():
    pervane.rotation_y += time.dt * 10


app = Ursina(borderless = False)


helicopter = Entity(model="Helicopter")
pervane = Entity(model="Pervane1", parent=helicopter, z = 0.34)

EditorCamera()

app.run()