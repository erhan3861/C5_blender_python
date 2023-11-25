from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve
Entity.default_shader = lit_with_shadows_shader 
# default -> varsayılan

def input(key):
    if key == "left mouse down":
        try:
            # cube.position = mouse.world_point
            for c in cube_listesi:
                c.animate_position(mouse.world_point, duration=3, curve=curve.sin)
        except:
            pass

app = Ursina(borderless = False) # pencere ekle

ground = Entity(model="plane", scale=400, texture="grass", collider="box")

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))


cube_listesi = []
for i in range(100):
    cube = Entity(model="C5Cube", unlit = True, y = 3, z=-100+i*3)
    cube_listesi.append(cube)


Sky()
EditorCamera()

app.run()