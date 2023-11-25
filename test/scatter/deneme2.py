from ursina import *

def parcalanma_efekti():
    cube.visible = False

    for _ in range(20):
        parca = Entity(model='cube', color=color.random_color(), position=cube.position)
        parca.animate_scale(Vec3(0, 0, 0), duration=1)
        parca.animate_position(parca.position + Vec3(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)), duration=0.5)
        
        destroy(parca, delay=2)

app = Ursina()

# Editor kamera oluşturma
editor_camera = EditorCamera()

# Işık oluşturma
directional_light = DirectionalLight()

cube = Entity(model='cube', color=color.orange, collider='box', scale=3)

def tiklama_oynat():
    parcalanma_efekti()

cube.on_click = tiklama_oynat

Sky()

ground = Entity(model="plane", scale=200, texture="grass", collider="box")

app.run()