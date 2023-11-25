from ursina import *
from ursina.shaders import basic_lighting_shader as bls
import json

Entity.default_shader = bls

stop = False

def input(key):
    global stop
    if key == "space":
        stop = not stop
        if stop :
            anim.pause()
        else:
            anim.resume()

def update():
    pass    

app = Ursina(borderless=False)

anim = FrameAnimation3d(name="anim_copter\\anim_", fps=60, texture="copter_baked", autoplay=False, rotation_y = 180)
anim.start()

print("anim.frames", anim.frames.__str__)

ground = Entity(model="plane", scale=300, texture="shore")

Sky()

cam = EditorCamera()

with open("D:\pythonDerslerim\C5_blender_python\helicopter_position.json", "r") as file:
    loc_dict = json.load(file)

point = Entity(model="sphere", scale=3, color=color.red)

point.sequence = Sequence(loop=True, auto_destroy=False)
for i in loc_dict:
    point.sequence.append(Func(setattr, point, 'position', tuple(loc_dict[i])))
    point.sequence.append(Wait(1/30))
point.sequence.start()

sf = cam.add_script(SmoothFollow(target=point, offset=(0,0.5,-4)))

app.run()