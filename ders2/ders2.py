from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve
from random import randint

Entity.default_shader = lit_with_shadows_shader 
# default -> varsayılan

items = False
b = None
b1 = None

def input(key):
    if key == "left mouse down" and distance(house, mouse.world_point)<2:
        house.clicked = not house.clicked

    if key == "left mouse down" and distance(tree1, mouse.world_point)<3:
        tree1.clicked = not tree1.clicked

    if key == "middle mouse down":
        if house.clicked:
            duplicate(house, clicked=False, unlit=True)
            text_popup("-500 $", house)

    if key == "middle mouse down":
        if tree1.clicked:
            duplicate(tree1, clicked=False, unlit=True)
            text_popup("-10 $", tree1)

    if key == "tab":
        global items,b, b1
        items = not items
       
        if items:
            b = Button("", scale=0.15, y=-.4)
            b.icon = "assets/tree_icon"
            b.icon.color=color.rgba(255,255,255,125)
            b.on_click = lambda: select_obj(tree1)

            b1 = Button("", scale=0.15, x=0.18, y=-.4)
            b1.icon = "assets/house_icon"
            b1.icon.color=color.rgba(255,255,255,125)
            b1.on_click = lambda: select_obj(house)
        else:
           destroy(b)
           destroy(b1)

def update():
    if house.clicked:
        house.position = mouse.world_point
        house.y -= .6
    if tree1.clicked:
        tree1.position = mouse.world_point
        tree1.y -= .6
        
def select_obj(obj):
    obj.clicked = True


def text_popup(txt="", obj=None) -> None:
	text = Text(text=txt, position = obj.screen_position)
	text.animate_position((text.x, (text.y + randint(5, 10)/100)), duration=.6, curve=curve.linear)
	text.animate_color(color.rgb(255, 255, 255, 0), duration=.6, curve=curve.linear)

	# We destroy it after a second
	destroy(text, delay=1)
     
app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

house = Entity(model="house", unlit=True, clicked=False)

# tree = Entity(model="tree", unlit=True, clicked=False, scale=5, y=1, z=10)
tree1 = Entity(model="tree1.obj", texture="tree1", unlit=True, clicked=False, scale=5, y=0, z=-10)

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))

Sky()

EditorCamera()

app.run()

