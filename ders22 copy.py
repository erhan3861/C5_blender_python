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

    if key == "left mouse down" and point.hovered:
        point.color = color.random_color()


x = 0
y = 0
z = 0
def update():
    global x,y,z
    x += (held_keys["1"]-held_keys["2"]) / 10
    y += (held_keys["4"]-held_keys["5"]) / 10
    z += (held_keys["7"]-held_keys["8"]) / 10

    # player.world_position = point2.world_position + Vec3(x,y, z)

app = Ursina(borderless=False)

anim = FrameAnimation3d(name="anim_copter\\anim_", fps=30, texture="copter_baked", autoplay=False, rotation_y = 180)
anim.start()

ground = Entity(model="plane", scale=300, texture="shore", collider="box", y=-.1)
player = FirstPersonController()

with open("helicopter_position.json", "r") as file:
    loc_dict = json.load(file)

point = Entity(model="sphere", scale=1, color=color.red, collider="box")

point.sequence = Sequence(loop=True, auto_destroy=False)
for i in loc_dict:
    point.sequence.append(Func(setattr, point, 'position', tuple(loc_dict[i])))
    point.sequence.append(Wait(1/15))
point.sequence.start()

# cam = EditorCamera()
# sf = cam.add_script(SmoothFollow(target=point, offset=(0,0,0)))



# sf = player.add_script(SmoothFollow(target=point))
# point2 = Entity(model="cube", parent=point, y=-1, scale=3, color=color.lime, collider="box")

Sky()

app.run()