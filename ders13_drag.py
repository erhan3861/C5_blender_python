from ursina import *
from ursina.shaders import basic_lighting_shader as bls, lit_with_shadows_shader as lit
from ursina import curve

Entity.default_shader = bls


def input(key):
    if key == "1":
        print_on_screen(f"Delta Drag : {round(Vec3(player.delta_drag).x/5)}", scale=2, duration=5,position=(-.5,0)) # f-string
        # ÖDEV #1 z hareketini siz yapınız
    elif key == "2":
        print_on_screen(f"Start Position : {player.start_pos}", scale=2, duration=5, position=(-.5,0)) 
        # ÖDEV # 2 İz yapma
        # kırmızı küre oluşturun sphere 
        # eski konumuna gitsin
        # duplicate(position = player.start_pos)
    if key == "y":
        player.plane_direction=(0,0,1)
        player.lock = (1,0,1)
        

app = Ursina(borderless=False)

grid = Entity(model = Grid(width=20, height=20, mode="line", thickness=2, colors=color.white), rotation_x=90, scale=100)

ground = Entity(model="plane", scale=100, texture="white_cube", texture_scale=(5,5),color=color.light_gray)

player = Draggable(parent=scene, model='cube', color=color.lime, plane_direction=(0,1,0), lock=(0,1,0), scale=5) # x y z

# Sky(texture="sky_sunset")

EditorCamera()

app.run()
