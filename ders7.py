from ursina import *
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from ursina import curve
from random import randint
from car7 import *

Entity.default_shader = lit_with_shadows_shader 
# default -> varsayılan

items = False
b = None
b1 = None
b2 = None # parking area resmi
b_yol = None

money = 1000
parkingAreaList = [] # otopark listesi

def input(key):
    global money
    try:
        if key == "left mouse down" and distance(building1, mouse.world_point)<2:
            building1.clicked = not building1.clicked

        if key == "left mouse down" and distance(building2, mouse.world_point)<3:
            building2.clicked = not building2.clicked

        if key == "left mouse down" and distance(parkingArea, mouse.world_point)<2:
            parkingArea.clicked = not parkingArea.clicked

        if key == "left mouse down" and distance(duz_yol, mouse.world_point)<2:
            duz_yol.clicked = not duz_yol.clicked
    except: pass

    if key == "middle mouse down":
        if int(btn_m.text[:-2]) <= 0:
            return
        if building1.clicked:
            duplicate(building1, clicked=False, unlit=True)
            text_popup("-100 $", building1)
            money -= 100
            btn_m.text = str(money) + " $"
            
        
        if building2.clicked:
            duplicate(building2, clicked=False, unlit=True)
            text_popup("-100 $", building2)
            money -= 100
            btn_m.text = str(money) + " $"

        if parkingArea.clicked: # parkingArea tıkladıysak
            p = duplicate(parkingArea, clicked=False, unlit=True, visible=True, sayac=0)
            parkingAreaList.append(p)
            text_popup("+10 $", p)
            money += 10
            btn_m.text = str(money) + " $"

        if duz_yol.clicked: # parkingArea tıkladıysak
            d = duplicate(duz_yol, clicked=False, unlit=True, visible=True, sayac=0)
            text_popup("-5 $", d)
            money -= 5
            btn_m.text = str(money) + " $"

    if key == "tab":
        global items, b, b1, b2, b_yol
        items = not items
       
        if items:
            b = Button("", scale=0.15, y=-.4,color=color.cyan)
            b.icon = "assets/icon1"
            b.icon.color=color.rgba(255,255,255,125)
            b.on_click = lambda: select_obj(building1)

            b1 = Button("", scale=0.15, x=0.18, y=-.4,color=color.cyan)
            b1.icon = "assets/icon2"
            b1.icon.color=color.rgba(255,255,255,125)
            b1.on_click = lambda: select_obj(building2)

            b2 = Entity(model="quad", parent=camera.ui, scale=0.30, x=0.40, y=-.4, texture="assets/parkingArea.png", collider="box")
            b2.color = color.white # orjinal renk
            b2.on_click = lambda: select_obj(parkingArea) # üzerine tıkla

            b_yol = Entity(model="quad", parent=camera.ui, scale=0.30, x= -0.20, y=-.4, texture="duz_yol.png", collider="box")
            b_yol.color = color.white # orjinal renk
            b_yol.on_click = lambda: select_obj(duz_yol) # üzerine tıkla

            
        else:
           destroy(b)
           destroy(b1)
           destroy(b2)
           destroy(b_yol)     
    
    # araba ekleme
    if key == "left shift":
        car = Car(model="car1.glb", position=mouse.world_point, unlit=False)
    if key == "right shift":
        car = Car(model="car2.glb", position=mouse.world_point, unlit=False)
    

def update():
    if not mouse.world_point:
        return
    if building1.clicked:
        building1.position = mouse.world_point
        building1.y -= .6
    elif building2.clicked:
        building2.position = mouse.world_point
        building2.y -= .6
    elif parkingArea.clicked: # mouse takp et
        parkingArea.position = mouse.world_point
        parkingArea.y += .1
    elif duz_yol.clicked: # mouse takp et
        duz_yol.position = mouse.world_point
        duz_yol.y -= .2

    if parkingAreaList : # eğer liste dolu ise çalıştır
        for pA in parkingAreaList:
            pA.sayac += 1
            invoke(text_popup, "+10 $", pA, delay=pA.sayac) 
            # invoke -> tetiklemek, başlatmak
            # delay 

            
def select_obj(obj):
    obj.clicked = True # mouse takip edebiliyor
    obj.visible = True # nesneyi görünür yap 

    # ders7 de bu kısım eklendi
    for e in scene.entities:
        if hasattr(e, "lines"): # yani bu nesne bir araba mıdır?
            e.clicked = False # arabanın seçimini iptal et
            e.color = color.white # orjinal rengine çevir


app = Ursina(borderless = False) # pencere ekle

Sky()


building1 = Entity(model="Building_1", unlit=True, clicked=False, x=10)
building2 = Entity(model="Building_2", unlit=True, clicked=False)

parkingArea = Entity(model="ParkingArea2", clicked=False, scale=10, visible=False)

# tree = Entity(model="tree", unlit=True, clicked=False, scale=5, y=1, z=10)
tree1 = Entity(model="tree1.obj", texture="tree1", unlit=True, clicked=False, scale=5, y=0, z=-10)

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))

coin_icon = Entity(model="Coin1", scale= 0.025, color=color.white,parent=camera.ui, z=0, x=.74, y=.45)
btn_m = Button(text="1000", scale=(0.1, 0.05), x=.82, y=.45, color=color.black90) # scale= 0.08

def text_popup(txt="", obj=None) -> None:
        text = Text(text=txt, position = obj.screen_position)
        text.animate_position((text.x, (text.y + randint(5, 10)/100)), duration=1.5, curve=curve.linear)
        text.animate_color(color.rgb(255, 255, 255, 0), duration=1.5, curve=curve.linear)

        # We destroy it after a second
        destroy(text, delay=1)

duz_yol = Entity(model="duzYol.obj", texture="bakedDuzYol.png",unlit=True, clicked=False, scale=1, visible=False)

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

EditorCamera(z=-20, y=20, rotation_x = 45) 

app.run()
