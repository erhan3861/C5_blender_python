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

ground = Entity(model="plane", scale=300, texture="shore", y=-0.3)

anim = FrameAnimation3d(name="helicopter_anim\\helicopter_animation_", fps=60, texture="BAKE_Helicopter", autoplay=False, rotation_y = 180)
anim.start()

platform = Entity(model="platform.gltf")

Sky()

cam = EditorCamera()

app.run()