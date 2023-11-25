from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key == "g":
        for e in city.children:
            e.shader = bls
            e.color = color.clear
            if "col" in e.name:
                e.color = color.azure
    elif key == "h": # hide -> gizle
        for e in city.children:
            e.shader = bls
            e.color = color.clear
            
app = Ursina(borderless=False)


city = load_blender_scene("AncientRuin", reload=False) # .blend uzantısını yazmıyoruz
# load_blender_scene kısmında hata alanlar reload=False yapmalılar

print(city)

city.scale = 5

for e in city.children:
    e.shader = bls
    e.color = color.clear
    if "col" in e.name:
        e.color = color.azure
        e.collider = "box"

ground = Entity(model="plane", scale=200, texture="grass", collider="box", y=1.5)

e = Entity(model="AncientRuin.obj", scale=5, shader=bls, texture="Ancient_Bake.png", rotation_y= 180)

Sky()

# EditorCamera()
player = FirstPersonController(x=25, y=2)

app.run()