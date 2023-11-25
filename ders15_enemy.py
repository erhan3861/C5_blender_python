from ursina import *
from ursina import curve

class Enemy(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            color=color.red,
            scale=0.5,
            visible=False,
            health=100, 
            
        )

        # Create a health bar for the enemy
        self.health_bar = Entity(
            model='quad',
            scale=(2, 0.2),
            color=color.green,
            parent=self,
            billboard=True
        )
        self.health_bar.y = 1

    def move(self, path):
        self.position = path[0].position
        invoke(setattr, self, "visible", True, delay=2.5)
        print("move çalıştı")
        counter = 0
        for cube in path:
            counter += 3
            invoke(self.go, cube.position, delay=counter)

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
            
