from ursina import *

def parcalanma_efekti():
    # Küpü kaldırmak için işlev
    cube.disable()

    # Parçaları oluşturmak için döngü
    for _ in range(20):
        parca = Entity(model='cube', color=color.random_color(), position=cube.position)
        parca.animate_position(parca.position + Vec3(random.uniform(-2, 2), random.uniform(-2, 2), random.uniform(-2, 2)), duration=0.5)
        parca.animate_scale(Vec3(0, 0, 0), duration=0.5)
        destroy(parca, delay=0.5)

# Oyunu başlatma
app = Ursina()

# Küpü oluşturma
cube = Entity(model='cube', color=color.orange, collider='box', scale=3)

# Tıklama olayını tanımlama
def tiklama_oynat():
    parcalanma_efekti()

cube.on_click = tiklama_oynat

# Oyunu başlatma
app.run()
