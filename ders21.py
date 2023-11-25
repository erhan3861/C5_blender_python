from ursina import *
from ursina.shaders import basic_lighting_shader as bls

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

app = Ursina(borderless=False)

anim = FrameAnimation3d(name="anim_copter\\anim_", fps=60, texture="copter_baked", autoplay=False, rotation_y = 180)
anim.start()

ground = Entity(model="plane", scale=300, texture="shore")

Sky()

cam = EditorCamera()

app.run()