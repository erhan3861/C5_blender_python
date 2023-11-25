from ursina import *
from ursina.shaders import lit_with_shadows_shader

def parcalanma_efekti():
    cube.disable()

    for _ in range(20):
        parca = Entity(model='cube', color=color.random_color(), position=cube.position, shader=lit_with_shadows_shader)
        parca.animate_position(parca.position + Vec3(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)), duration=1)
        parca.animate_scale(Vec3(0, 0, 0), duration=1)
        destroy(parca, delay=0.5)

app = Ursina()

editor_camera = EditorCamera()
directional_light = DirectionalLight()

cube = Entity(model='cube', color=color.orange, collider='box', scale=3, shader=lit_with_shadows_shader)

def tiklama_oynat():
    parcalanma_efekti()

cube.on_click = tiklama_oynat

app.run()
