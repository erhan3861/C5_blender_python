from ursina import *
import random
from ursina.shaders import basic_lighting_shader as bls
from ursina import curve

# Entity.default_shader = bls


def select():
    helicopter.selected = not helicopter.selected
    if helicopter.selected: helicopter.color = color.lime
    else: helicopter.color = color.white

def update():
    pervane.rotation_y += held_keys["r"] * time.dt * 50

def input(key):
    if key == "+":
        helicopter.x += 1

app = Ursina(borderless=False)

helicopter = Entity(model="govde.glb", collider="box", selected=False, area=Entity(mode=""))
helicopter.on_click = select

pervane = Entity(model="pervane.glb", parent=helicopter, collider="box", y=3)
# parent=helicopter , position = (-2.69147, 282.882, 26.5073)

EditorCamera()

Sky(texture="sky_sunset")

app.run()