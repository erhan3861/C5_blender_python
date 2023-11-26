from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController 
import json

Entity.default_shader = bls

stop = False

def input(key):
    global stop
    if key == "space":
        stop = not stop
        if stop :
            anim.pause()
            point.sequence.pause()
        else:
            anim.resume() 
            point.sequence.resume()

    if key == "0":
        point2.world_position = point.world_position

    if key == "left mouse down" and point.hovered:
        point.color = color.random_color()


def update():

    player.world_position = point.world_position + Vec3(0,-2, 2)

app = Ursina(borderless=False)

anim = FrameAnimation3d(name="anim_copter\\anim_", fps=60, texture="copter_baked", autoplay=False, rotation_y = 180)
anim.start()

ground = Entity(model="plane", scale=300, texture="shore")

Sky()

with open("helicopter_position.json", "r") as file:
    loc_dict = json.load(file)

point = Entity(model="sphere", scale=3, color=color.red, collider="sphere")

point.sequence = Sequence(loop=True, auto_destroy=False)
for i in loc_dict:
    point.sequence.append(Func(setattr, point, 'position', tuple(loc_dict[i])))
    point.sequence.append(Wait(1/30))
point.sequence.start()

# cam = EditorCamera()
# sf = cam.add_script(SmoothFollow(target=point, offset=(0,0,0)))

player = FirstPersonController()
# sf = player.add_script(SmoothFollow(target=point))

app.run()