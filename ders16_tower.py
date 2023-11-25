from ursina import *
from random import uniform # rastgele ondalıklı sayı
from ursina.shaders import basic_lighting_shader as bls
from ders17_enemy_test import *


Entity.default_shader = bls

# Define the Tower class
class Tower(Draggable):
    def __init__(self, model, position, range, damage, attack_speed = 20):
        super().__init__(parent = scene)
        self.model = model
        # self.scale_y = 2
        # self.y = 1
        self.scale = .1
        self.collider = "box"
        self.position=position
        self.plane_direction=(0,1,0)
        self.lock=(0,1,0)

        self.color = color.white  # Customize the tower's appearance
        self.range = range
        self.damage = damage
        self.attack_speed = attack_speed
        self.target = None  # Initialize the target as None
        self.target_list = [] # hedefler listesi
        self.target_dict = {} # hedefler listesi
        self.target_alive = True
       
        self.bullets = [] # kulenin mermileri

        self.range_circle = Entity(parent=self, model=Circle(64, mode='line', radius=self.range*10, thickness=4), color=color.red, rotation_x=90)

    @classmethod
    def check_hitting(cls, self):
        for bullet in self.bullets:
            if bullet and distance(bullet, self.target) < .5:
                self.target.color = color.random_color()
                self.target.change_health_bar() # added in lesson 17
                

    def fire(self):
        # Check if the target is visible
        if not self.target.visible : return
        
        if not self.target_list: return # eğer düşman yoksa

        # Check if the target is within range
        distance_to_target = distance_xz(self, self.target)
        if distance_to_target >= self.range: return

        # Create a bullet entitys -> mermi oluştur
        bullet = Entity(
            world_parent = scene,
            model='sphere',
            color=color.yellow,  # Customize the projectile appearance
            scale=0.1,
            position=self.position,
            y = self.y + .7
        )

        self.bullets.append(bullet)

        bullet.look_at(self.target)

        bullet.animate_position(self.target.position + Vec3(uniform(-1,1),0,uniform(-1,1)), duration=.3)

        destroy(bullet, delay=.4)
        # invoke -> tetikliyor
        invoke(lambda x = bullet: self.bullets.remove(x), delay=.5)

    def show_range(self):
        if self.dragging:
            self.range_circle.visible = True
        else:
            self.range_circle.visible = False

    def find_target(self, enemies):
        min_dist = self.range # min uzaklık = kulenin menzilini  
        
        for enemy in enemies:
            if distance_2d(self, enemy) <= min_dist:
                min_dist = distance_2d(self, enemy)

        for enemy in enemies:
            if distance_2d(self, enemy) <= min_dist:
                self.target = enemy
                return

        # no enemy detected    
        self.target = enemies[0]
        


            
if __name__ == "__main__":

    def update():
        t.show_range()
        t.find_target(t.target_list)
        t.fire()

        # Check if there is hitting
        if t.target_list:
            Tower.check_hitting(t)
        
    app = Ursina(borderless = False)

    t = Tower(model = "tower_v2.glb", position=Vec3(0), range=5, damage=100)
    
    enemy = Entity(model="cube", color=color.red)
    enemy2 = Entity(model="cube", color=color.red, position=(3,0,5))

    t.target = enemy
    t.target_list.append(enemy)
    t.target_list.append(enemy2)

    t.target_dict[enemy] = {}



    EditorCamera()

    Sky()

    grounds = []

    # Create ground cubes
    for x in range(20):
        for z in range(20):
            cube = Entity(model='cube', position=(x, -0.5, z), color=color.light_gray, texture="white_cube")
            cube.collider = 'box'
            grounds.append(cube)

    # Yukarıdan oyun alanına doğru bakacak bir kamera ekleyin
    cam = EditorCamera()
    cam.position = Vec3(10.4199, 13.6906, -4)
    cam.rotation = Vec3(50.9669, -1.30302, 0)

    app.run()

    # ÖDEVİMİZ en az 3 tane düşman eklemek
    # 2 tane kule yapmak


    



