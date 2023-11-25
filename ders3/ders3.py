from ursina import *
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader
from ursina import curve
from random import randint

Entity.default_shader = basic_lighting_shader 
# default -> varsayılan

items = False # nesneleri sakla
btn1 = None
btn2 = None

def input(key):
    try:
        if key == "left mouse down" and distance(b1, mouse.world_point)<2:
            b1.clicked = not b1.clicked

        if key == "left mouse down" and distance(b2, mouse.world_point)<3:
            b2.clicked = not b2.clicked
    except: pass

    if key == "middle mouse down":
        if b1.clicked:
            duplicate(b1, clicked=False, unlit=True)
        if b2.clicked:
            duplicate(b2, clicked=False, unlit=True)
    
    if key == "tab":
        global items, btn1, btn2
        items = not items # False -> True  / True -> False

        if items: # eğer items -> True
            btn1 = Button("", scale=0.15, y=-.4)
            btn1.icon = "assets/icon1"
            btn1.icon.color = color.rgba(255,255,255,125)
            btn1.on_click = lambda : select_obj(b1)

            btn2 = Button("", scale=0.15, x=0.18, y=-.4)
            btn2.icon = "assets/icon2"
            btn2.icon.color = color.rgba(255,255,255,125)
            btn2.on_click = lambda : select_obj(b2)
        
        else:
            destroy(btn1)
            destroy(btn2)
    
def update():
    if b1.clicked:
        b1.position = mouse.world_point
        b1.y -= .6
    if b2.clicked:
        b2.position = mouse.world_point
        b2.y -= .6
        
def select_obj(obj):
    obj.clicked = True

app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="Area_3", scale=100, collider="box", unlit=True)

b1 = Entity(model="Building_1", unlit=True, clicked=False, x=5,scale=3)
b2 = Entity(model="Building_2", unlit=True, clicked=False,scale=3)

# sun = DirectionalLight() # yönlendirilmiş ışık 
# sun.look_at((-1, -1, 1))

Sky()

EditorCamera()

app.run()

