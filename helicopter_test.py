from ursina import *
import random
from ursina.shaders import basic_lighting_shader as bls
from ursina import curve
from ursina.prefabs.first_person_controller import FirstPersonController

Entity.default_shader = bls


def update():
    pervane.rotation_y += time.dt * 10
    
    if helicopter.selected and helicopter.area.mode=="y":
        try:
            helicopter.y = mouse.world_point.y
        except:
            pass
    elif helicopter.selected and helicopter.area.mode=="x":
        try:
            helicopter.x = mouse.world_point.x
        except:
            pass
    # GÖREV #1 area.mode == z konumunu ayarla

line = None
def input(key):
    global line
    if key == "+":
        helicopter.x += 1

    elif key == "y":
        destroy(helicopter.area)
        destroy(line)
        if helicopter.selected:
            helicopter.area = Entity(model="cube", scale=(200,200,1), y=100, color=color.rgba(30, 1, 1, 120), collider="box", mode="y")
            line = Entity(model=Mesh(vertices = [Vec3(helicopter.x,0,0), Vec3(helicopter.x,200,0)], mode="line"))

    elif key == "x":
        destroy(helicopter.area)
        destroy(line)
        if helicopter.selected:
            helicopter.area = Entity(model="cube", scale=(400,1,400), y=helicopter.y, color=color.rgba(30, 1, 1, 120), collider="box", mode="x")
            line = Entity(model=Mesh(vertices = [Vec3(-200,helicopter.y,0), Vec3(200,helicopter.y,0)], mode="line"))

        # Görev #2 AREA Z

    elif key == "space":
        destroy(helicopter.area)
        destroy(line)
        helicopter.selected = False

def select():
    helicopter.selected = not helicopter.selected
    if helicopter.selected: helicopter.color = color.lime
    else: helicopter.color = color.white
    

app = Ursina(borderless=False)

helicopter = Entity(model="govde.glb", collider="box", selected=False, y=5, area=Entity(mode=""), scale=10)
helicopter.on_click = select

pervane = Entity(model="pervane.glb", parent=helicopter, position=(0, 3, 0.02)) # position=(3.083, 4.7, 0.02)

ground = Entity(model="plane", texture="grass", scale=300)

EditorCamera()

Sky()

app.run()