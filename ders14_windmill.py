from ursina import *
from ursina.shaders import basic_lighting_shader as bls

Entity.default_shader = bls

# bu değişken oyunun başlamasını kontrol eder
game_start = False

def input(key):
    if key == "1":
        print_on_screen(f"Delta Drag: {Vec3(windmill.delta_drag)}")
    elif key == "2":
        print_on_screen(f"Start Position: {Vec3(windmill.start_pos)}")

def update():
    global game_start
    # game_start değişkenini değiştireceğimiz için global yaptık

    if windmill.stop_dragging and game_start: # sürükleme bittiğinde ve game_start True ise
        for g in grounds:
            if distance_xz(windmill, g) < .5:
                windmill.x = g.x
                windmill.z = g.z
                windmill.placed = True
                make_green() # etrafını yeşile boya

    if windmill.dragging: # sürüklendiğinde
        game_start = True
        for g in grounds:
            if distance_xz(windmill, g) < .5: # yatay mesafesi 0.5 ten az ise
                g.color = color.lime
            else:
                g.color = color.white
        
    # ÖDEV : 
    # yel değirmeninin bir yere koyulduğu zaman
    # pervanelerinin dönmesini sağlayalım

def make_green():
    # Windmill ile en yakın 6 küpün rengini zamanla beyazdan yeşile geçirin
    if windmill.placed:
        for g in grounds:
            if distance_xz(windmill, g) < 2:
                g.color = lerp(g.color, color.lime, time.dt / 10)  # 60 FPS'de 1 dakika geçişi
                # g.color = 0    0         100  = 50
                #           50   50        100  = 75
                #           75   75        100  = 90

app = Ursina(borderless=False)

grounds = [] # zemindeki küpleri saklar / tutar
for i in range(10): # dış döngü
    for j in range(10): # iç
        ground = Entity(model='plane', position=(-5 + i, 0, 5 - j), texture='white_cube')
        grounds.append(ground)

# Windmill ekleyin
windmill = Draggable(parent=scene, model='windmill', position=(0, .5, 0), plane_direction=(0, 1, 0), lock=(0, 1, 0),scale=.5, color=color.white, placed = False)

Sky()
EditorCamera()

app.run()
