from ursina import *
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader
from ursina import curve
from random import randint

Entity.default_shader = basic_lighting_shader 
# default -> varsayılan

items = False
b = None
b1 = None
b2 = None # parking area resmi
money = 1000
parkingAreaList = [] # otopark listesi

def input(key):
    global money
    try:
        print("dist =",distance(building1, mouse.world_point))
        if key == "left mouse down" and distance(building1, mouse.world_point)<2:
            building1.clicked = not building1.clicked

        print("dist2 =",distance(building2, mouse.world_point))
        if key == "left mouse down" and distance(building2, mouse.world_point)<3:
            building2.clicked = not building2.clicked

        if key == "left mouse down" and distance(parkingArea, mouse.world_point)<2:
            parkingArea.clicked = not parkingArea.clicked

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

    if key == "tab":
        global items, b, b1, b2
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
            

        else:
           destroy(b)
           destroy(b1)
           destroy(b2)

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

    if parkingAreaList : # eğer liste dolu ise çalıştır
        for pA in parkingAreaList:
            pA.sayac += 1
            invoke(text_popup, "+10 $", pA, delay=pA.sayac) 
            # invoke -> tetiklemek, başlatmak
            # delay 
    
        
def select_obj(obj):
    obj.clicked = True # mouse takip edebiliyor
    obj.visible = True # oyun başladığında parkımız invisible 

app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="Area", scale=2, collider="box")

building1 = Entity(model="Building_1", unlit=True, clicked=False, x=10)
building2 = Entity(model="Building_2", unlit=True, clicked=False)

parkingArea = Entity(model="ParkingArea", clicked=False, scale=0.3, visible=False)

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

yol_duz = Entity(model="duz_yol", unlit=True, clicked=False, scale=1)


    
Sky()

EditorCamera()

app.run()

