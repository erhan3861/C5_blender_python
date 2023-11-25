from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve
Entity.default_shader = lit_with_shadows_shader 
# default -> varsayılan

def input(key):
    if key == 'left mouse down' and distance(house.position, mouse.world_point)<2:
        house.clicked = not house.clicked

    if key == "left mouse down" and distance(tree1, mouse.world_point)<3:
        tree1.clicked = not tree1.clicked

    if key == "middle mouse down":
        if house.clicked:
            duplicate(house, clicked=False, unlit=True)

        if tree1.clicked:
            duplicate(tree1, clicked=False, unlit=True)    

def update():
    if house.clicked:
        house.position = mouse.world_point 
        house.y -= .6 
    if tree1.clicked:
        tree1.position = mouse.world_point
        tree1.y -= .6


app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

house = Entity(model="house", unlit = True, y=0, z=5, clicked=False)

tree1 = Entity(model="tree1.obj", texture="tree1", unlit=True, clicked=False, scale=5, y=0, z=-10)

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))

Sky()

EditorCamera()

app.run()