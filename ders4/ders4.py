# coin ve money kısmını yapıyoruz, text pop-up

from ursina import *
from ursina.shaders import lit_with_shadows_shader,basic_lighting_shader
from ursina import curve
from random import randint

Entity.default_shader = basic_lighting_shader 
# default -> varsayılan

items = False # nesneleri sakla
btn1 = None
btn2 = None
money = 1000 # başlangıç paramız

def input(key):
    global money # bir değişkeni fonk içinde değiştiriyorsak global yapmak zorundayız
    try:
        if key == "left mouse down" and distance(b1, mouse.world_point)<2:
            b1.clicked = not b1.clicked

        if key == "left mouse down" and distance(b2, mouse.world_point)<3:
            b2.clicked = not b2.clicked
    except: pass

    # building
    if key == "middle mouse down":
        if int(buton_coin.text) <= 0:
            return # paramız biterse fonksiyonu çalıştırma
        if b1.clicked:
            duplicate(b1, clicked=False, unlit=True)
            text_popup("-100 $", b1)
            money -= 100
            buton_coin.text = str(money)

        if b2.clicked:
            duplicate(b2, clicked=False, unlit=True)
            # ÖDEV
    
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
    if not mouse.world_point:
        return # eğer mouse zemin üzerinde değilse geri dön

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

def text_popup(txt="", obj=None) -> None:
    text = Text(text=txt, position = obj.screen_position)
    text.animate_position((text.x, text.y + 0.10), duration=2, curve=curve.linear)
    text.animate_color(color.rgba(255,255,255,0), duration=2, curve=curve.linear)

    destroy(text, delay=2) # yok etmek    delay -> gecikme

# coin ve money (ÖDEV)
coin_icon = Entity(model="quad", scale=0.08, parent=camera.ui, x=.73, y=.45, z=-.2, texture="coin")
# money_icon
buton_coin = Button(text="1000", scale=(0.1, 0.05), x=.82, y=.45, color=color.black90)
# buton_money

Sky()

EditorCamera()

app.run()

