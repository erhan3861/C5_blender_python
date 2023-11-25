from ursina import *
from random import uniform


# Define the Tower class
class Tower(Draggable):
    def __init__(self, position, range, damage, attack_speed = 20):
        super().__init__(parent = scene)
        self.model='cube'
        self.scale_y = 2
        self.y = 1
        self.position=position
        self.plane_direction=(0,1,0)
        self.lock=(0,1,0)

        self.color=color.azure  # Customize the tower's appearance
        self.range = range
        self.damage = damage
        self.attack_speed = attack_speed
        self.target = None  # Initialize the target as None
        self.target_list = [] # hedefler listesi
        self.target_alive = True
       
        self.bullets = [] # kulenin mermileri

        self.range_circle = Entity(parent=self, model=Circle(64, mode='line', radius=3, thickness=4), color=color.red, rotation_x=90)

    @classmethod
    def check_hitting(cls, self):
        for bullet in self.bullets:
            if bullet and distance(bullet, self.target) < .5:
                self.target.color = color.random_color()
                

    def fire(self):
        # Check if the target is visible
        if not self.target.visible : return
        
        if not self.target_list: return # eğer düşman yoksa

        # Check if the target is within range
        distance_to_target = distance(self, self.target)
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
        for enemy in enemies:
            if distance_2d(self, enemy) <= 1:
                return enemy
        return enemies[0]


            
if __name__ == "__main__":


    def update():
        t.show_range()
        t.fire()

    app = Ursina(borderless = False)

    ground = Entity(model="plane", scale=200, texture="grass")

    t = Tower(position=Vec3(0), range=2, damage=100)

    enemy = Entity(model="cube", color=color.red)

    t.target = enemy
    t.target_list.append(enemy)

    EditorCamera()

    Sky()

    app.run()

    # ÖDEVİMİZ en az 3 tane düşman eklemek
    # 2 tane kule yapmak


    



