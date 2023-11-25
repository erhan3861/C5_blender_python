from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

class Water(Entity):
    def __init__(self, pos):
        super().__init__()
        self.model = "water.gltf"
        self.scale = 5
        self.y += .025
        self.z += pos*3
        self.color = color.random_color()
        self.shader = bls
    
    def update(self):
        self.z -= 5 * time.dt
        if self.z <-13:
            self.z = 5
            self.y = uniform(0.025, 0.090)

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

    if abs(player.x - water.x) < 2:
        if not water_sound.playing:
            water_sound.play()
    else:
        water_sound.stop()

    
            
app = Ursina(borderless=False)

water_sound = Audio("river_sound1.wav", autoplay=False)


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

water = Entity(model="water.gltf", color=color.clear)

for i in range(13):
    Water(pos = i) 


app.run()