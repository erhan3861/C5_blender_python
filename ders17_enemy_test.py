from ursina import *
from ursina import curve
from ders16_tower import *

class Enemy(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            color=color.red,
            scale=0.5,
            visible=False,
            health=100
        )

        # Create a health bar for the enemy
        self.health_bar = Entity(
            model='quad',
            scale=(2, 0.2),
            color=color.green,
            parent=self,
            billboard=True # her zaman kullanıcıya bakıyor
        )
        self.health_bar.y = 1

    def move(self, path):
        self.position = path[0]
        invoke(setattr, self, "visible", True, delay=2.5)
        print("move çalıştı")
        counter = 0
        # to move all the points in the path
        for point in path:
            counter += 3 # in 3 seconds enemy goes next position
            invoke(self.go, point, delay=counter)

    def go(self, pos):
        self.animate('position', (pos[0], 0.1, pos[2]), duration=3, curve=curve.linear)

    def change_health_bar(self):
        # Decrease health
        self.health -= 1  # For example, reduce 0.1 units of health in each update loop

        # Update the health bar
        health_percentage = self.health / 100.0
        if health_percentage < 0.002:
            health_percentage = 0.01

        self.health_bar.scale_x = health_percentage * 2  # Ensure the health bar does not take negative values

        # End the game when health is depleted
        if self.health <= 0.01:
            self.visible = False



if __name__ == "__main__":

    def input(key):
        if key == "e":
            for e in enemies:
                e.health = 100
                e.change_health_bar()
                invoke(e.move, targets, delay=enemies.index(e)*2)

    def update():
        t.show_range()
        t.find_target(t.target_list)
        if t.target:
            t.fire()

        # Check if there is hitting
        if t.target_list:
            Tower.check_hitting(t)
        
    app = Ursina(borderless = False)

    
    enemies = [Enemy() for i in range(10)]

    targets = [Vec3(5,0,7), Vec3(5,0,10), Vec3(9,0,10), Vec3(15,0,10), Vec3(5,0,5)]

    t = Tower(model = "tower_v2.glb", position=Vec3(0), range=5, damage=100)
    t.enemy = enemies[0]
    [t.target_list.append(e) for e in enemies]

    
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
