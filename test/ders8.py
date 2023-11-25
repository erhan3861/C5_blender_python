from ursina import *
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader
from ursina import curve
from random import randint
from car8 import *

Entity.default_shader = lit_with_shadows_shader 
# default -> varsayılan

items = False
b = None
b1 = None
b2 = None # parking area resmi
b_yol = None
b_yollar = False
b_yol_list = []

car1 = None
b_cars = None

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

        if key == "left mouse down" and distance(car1, mouse.world_point)<2:
            car1.clicked = not car1.clicked

        if key == "left mouse down" and distance(rampa, mouse.world_point)<2:
            rampa.clicked = not rampa.clicked

        if key == "right mouse down" and distance(rampa, mouse.world_point)<3:
            rampa.rotation_y += 90

        if key == "left mouse down" and distance(kopru, mouse.world_point)<2:
            kopru.clicked = not kopru.clicked

        if key == "left mouse down" and distance(e2, mouse)<2: rampa.clicked = True
        if key == "left mouse down" and distance(e3, mouse)<2: kopru.clicked = True




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

        if car1.clicked: # parkingArea tıkladıysak
            car = Car(model="car1", position=mouse.world_point, unlit=True)
            text_popup("-15 $", car)
            money -= 15
            btn_m.text = str(money) + " $"

        if distance(rampa, mouse.world_point)<3:
            rampa.clicked = False
            rampa.collider = "box"
        else:
            rampa.collider = None

        if distance(kopru, mouse.world_point)<3:
            kopru.clicked = False
            kopru.collider = "box"
        else:
            kopru.collider = None



    if key == "tab":
        global items, b, b1, b2, b_yol, b_yollar, b_yol_list, b_cars
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

            b_cars = Entity(model="quad", parent=camera.ui, scale=0.30, x= -0.40, y=-.4, texture="car1.png", collider="box")
            b_cars.color = color.white # orjinal renk
            b_cars.on_click = lambda: select_obj(car1) # üzerine tıkla


            e1 = Entity(model="quad", parent=camera.ui, scale=0.30, x= -0.60, y=-.25, texture="duz_yol.png", collider="box", visible=False)
            e2 = Entity(model="quad", parent=camera.ui, scale=0.30, x= -0.40, y=-.25, texture="rampa.png", collider="box", visible=False)
            e3 = Entity(model="quad", parent=camera.ui, scale=0.30, x= -0.20, y=-.25, texture="bridge.png", collider="box", visible=False)
            b_yol_list = [e1,e2,e3]

            e1.on_click = lambda : select_obj(duz_yol) # üzerine tıkla
            e2.on_click = lambda : select_obj(rampa) # üzerine tıkla
            e3.on_click = lambda : select_obj(kopru) # üzerine tıkla

        else:
           destroy(b)
           destroy(b1)
           destroy(b2)
           destroy(b_yol)
           [destroy(b) for b in b_yol_list] 
           b_yol_list.clear()
           destroy(b_cars)
           for e in scene.entities:
                if hasattr(e, "clicked"):
                    e.clicked = False
                
        
    if items:
        try : 
            if key =="left mouse down" and distance_2d(mouse, b_yol) < 0.03:
                b_yollar = not b_yollar
                print(distance_2d(mouse, b_yol))
        except : pass
    
    if b_yollar and b_yol_list:
        [setattr(e, "visible", True) for e in b_yol_list] 
    else:
        [setattr(e, "visible", False) for e in b_yol_list] 

    # araba ekleme
    if key == "left shift":
        car = Car(model="car1.glb", position=mouse.world_point, unlit=False)
    if key == "right shift":
        car = Car(model="car_white", position=mouse.world_point, unlit=False)
    if key == "space":
        rampa.clicked = True


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
    elif car1.clicked: # mouse takp et
        car1.position = mouse.world_point
        car1.y -= .1

    elif rampa.clicked: # mouse takp et
        rampa.position = mouse.world_point
        rampa.y += .1

    elif kopru.clicked: # mouse takp et
        kopru.position = mouse.world_point
        kopru.y += .1
    
    

    if parkingAreaList : # eğer liste dolu ise çalıştır
        for pA in parkingAreaList:
            pA.sayac += 1
            invoke(text_popup, "+10 $", pA, delay=pA.sayac) 
            # invoke -> tetiklemek, başlatmak
            # delay 

            
def select_obj(obj):
    obj.clicked = True # mouse takip edebiliyor
    obj.visible = True # nesneyi görünür yap 


app = Ursina(borderless = False) # pencere ekle

Sky()


building1 = Entity(model="Building_1", unlit=True, clicked=False, x=10, scale=5)
building2 = Entity(model="Building_2", unlit=True, clicked=False, scale=5)

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

duz_yol2 = Entity(model="duzYol2.glb", unlit=False, clicked=False, scale=5, visible=False)

car1 = Entity(model="car1.glb", unlit=False, clicked=False, scale=5, visible=False)

rampa = Entity(model="rampa.obj", texture="rampa_baked.png",clicked=False, scale=5, visible=False, shader=basic_lighting_shader, unlit=True)
kopru = Entity(model="bridge.obj", texture="bridge_baked.png", clicked=False, scale=5, visible=False, shader=basic_lighting_shader, unlit=True)

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

EditorCamera() 

app.run()
