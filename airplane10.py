from ursina import *
import random
from ursina.shaders import basic_lighting_shader as bls, lit_with_shadows_shader as lit
from ursina import curve

Entity.default_shader = lit

def update():
    global fuel, current_target_index

    if not plane : return

    # Hedef noktaya doğru uçağı hareket ettirin
    target_point = target_points[current_target_index]
    
    plane.look_at_2d(Vec3(target_point), axis="y")
    
    if plane.fly : plane.position += plane.forward * 0.05  # Uçak hızı ayarlayın

    # Hedef noktaya ulaşıldığında bir sonraki hedefe geçin
    if distance(plane.position, target_point) < 0.1:
        current_target_index = (current_target_index + 1) % len(target_points)

    # Yakıtı azaltın
    fuel -= 0.1  # Örneğin, her güncelleme döngüsünde 0.1 birim yakıt azalıyor

    # Yakıt çubuğunu güncelleyin
    health_percentage = fuel / 100.0  # Sağlık çubuğunu yakıt miktarına göre güncelleyin
    if health_percentage < 0.002:
        health_percentage = 0.01

    health_bar.scale_x = health_percentage * 7  # Sağlık çubuğu negatif değer almasın

    # Yakıt tükendiğinde oyunu sonlandırın
    if fuel <= 0 and plane.fly:
        plane.animate('y', 0, duration=3, curve = curve.linear)
        invoke(destroy, plane, delay=5) # tetikle, ateşle, başlat
        plane.fly = False

    for airplane in airplanes:
        if airplane.y == 15 and airplane.fly:
            fly_on_air(airplane)


def on_mouse_click(airplane):
    for airplane in airplanes:
        if mouse.hovered_entity == plane and plane.fly:
            plane.look_at_2d(airport, axis="y")
            plane.animate('position', airport.position+Vec3(2,0.5,0), duration=3, curve=curve.linear)
            plane.fly = False

        elif mouse.hovered_entity == airport and not airplane.fly:
            airplane.animate('y', 15, duration=3, curve=curve.linear)
            airplane.animate('z', airplane.z + 30, duration=3, curve=curve.linear)
            airplane.fly = True

def fly_on_air(plane):
    if plane.fly : plane.position += plane.forward * 0.1  # Uçak hızı ayarlayın


def toggle_fly(air_plane):
    air_plane.fly = not air_plane.fly

app = Ursina()

# Uçağınızı oluşturun veya içe aktarın
plane = Entity(model="Airplane.obj", texture="AirplaneBaked", y=15, fly=True, shader=bls, collider="box")
plane.on_click = lambda : on_mouse_click(plane)

# Sağlık çubuğunu oluşturun
health_bar = Entity(model='quad', scale=(7, .5), color=color.green, parent=plane, billboard = True)
health_bar.y = 1.5  # Sağlık çubuğunu uçağın üstüne yerleştirin

# Uçağın başlangıç yakıt miktarını ayarlayın
fuel = 100.0  # Örneğin, başlangıçta 100 birim yakıt

# Uçağın uçacağı 5 farklı hedef nokta belirleyin
target_points = [(3, 15, 3), (-3, 15, 3), (25, 15, -20), (-15, 15, -3), (0, 15, 0)]
# hedefin şu anki indeksi (sırası)
current_target_index = 0

ground = Entity(model="plane", texture="grass", scale=200)

# Havaalanı oluşturun
airport = Entity(model='Airport_Lowpoly', y=0.05, collider="box", scale=3)
airport.on_click = lambda : on_mouse_click(airplane)

# Uçakları oluşturun ve havaalanına yerleştirin
airplanes = []
for i in range(3):
    # GÖREV-1 3 tane uçak yapınız ve farklı noktalarda olsunlar
    airplane = Entity(model="Airplane.obj", texture="AirplaneBaked", position=airport.position+Vec3(0, 0.5, i*12), shader=bls, collider="box", fly=False)
    
    airplane.on_click = lambda x = airplane: toggle_fly(x) # Görev-2 fonksiyonun uçağın fly özelliğini True veya False

    airplanes.append(airplane)


Sky()

EditorCamera(y=30)

sun = DirectionalLight() # yönlendirilmiş ışık 
sun.look_at((-1, -1, 1))

app.run()

# ödevimiz 




