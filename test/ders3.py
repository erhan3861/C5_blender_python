from ursina import *
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader
from ursina import curve
from random import randint

Entity.default_shader = basic_lighting_shader 
# default -> varsayılan

items = False
b = None
b1 = None

def input(key):
   
    try:
        print("dist =",distance(building1, mouse.world_point))
        if key == "left mouse down" and distance(building1, mouse.world_point)<2:
            building1.clicked = not building1.clicked

        print("dist2 =",distance(building2, mouse.world_point))
        if key == "left mouse down" and distance(building2, mouse.world_point)<3:
            building2.clicked = not building2.clicked
    except: pass

    if key == "middle mouse down":
        if building1.clicked:
            duplicate(building1, clicked=False, unlit=True)
        if building2.clicked:
            duplicate(building2, clicked=False, unlit=True)
            

    if key == "tab":
        global items,b, b1
        items = not items
       
        if items:
            b = Button("", scale=0.15, y=-.4,color=color.cyan)
            b.icon = "assets/tree_icon1"
            b.icon.color=color.rgba(255,255,255,125)
            b.on_click = lambda: select_obj(building1)

            b1 = Button("", scale=0.15, x=0.18, y=-.4,color=color.cyan)
            b1.icon = "assets/house_icon1"
            b1.icon.color=color.rgba(255,255,255,125)
            b1.on_click = lambda: select_obj(building2)
        else:
           destroy(b)
           destroy(b1)

def update():
    if building1.clicked:
        building1.position = mouse.world_point
        building1.y -= .6
    elif building2.clicked:
        building2.position = mouse.world_point
        building2.y -= .6
        
def select_obj(obj):
    obj.clicked = True

app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="Area", scale=1, collider="box")

building1 = Entity(model="Building_1", unlit=True, clicked=False)
building2 = Entity(model="Building_2", unlit=True, clicked=False)

# tree = Entity(model="tree", unlit=True, clicked=False, scale=5, y=1, z=10)
tree1 = Entity(model="tree1.obj", texture="tree1", unlit=True, clicked=False, scale=5, y=0, z=-10)

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))

Sky()

EditorCamera()

app.run()

