from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key == "g": # göster -> show
        for e in city.children:
            e.shader = bls
            e.color = color.clear
            if "col" in e.name:
                e.color = color.azure
    elif key == "h": # hide -> gizle
        for e in city.children:
            e.shader = bls
            e.color = color.clear

def update():
    if distance_xz(player, city_model) < 7:
        city.shader = bls # sis efektini kaldırırız
    else:
        city.shader = Entity.default_shader # öntanımlı shader

    for w in waters:
        w.z -= time.dt * 0.4
        if w.z < -15:
            w.z = 3

            
app = Ursina(borderless=False)


city = load_blender_scene("AncientRuin", reload=False) # .blend uzantısını yazmıyoruz
# load_blender_scene kısmında hata alanlar reload=False yapmalılar

city.scale = 5

for e in city.children:
    e.color = color.clear
    if "col" in e.name:
        e.color = color.azure
        e.collider = "box"

ground = Entity(model="plane", scale=200, texture="grass", collider="box", y=1.5)

city_model = Entity(model="AncientRuin.obj", scale=5, texture="Ancient_Bake.png", rotation_y= 180)

Sky(texture="sky_sunset")

# EditorCamera()
player = FirstPersonController(x=25, y=2)

# walls for showing fog
wall1 = Entity(model = 'cube', scale = (100, 20,2), z=50, color=color.clear)
wall2 = duplicate(wall1, x=50, rotation_y=90)
wall3 = duplicate(wall1, z=-50, rotation_y=180)
wall4 = duplicate(wall1, x=-50, rotation_y=270)

scene.fog_density = 0.1 # sisin yoğunluğu
scene.fog_color = color.gray # sisin rengi

water = Entity(model="water.gltf",color = color.blue, scale=5, scale_z = 2) 


waters = [water]
for i in range(50):
    w = duplicate(water, z = water.z - i*3)
    waters.append(w)

app.run()