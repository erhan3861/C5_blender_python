from ursina.prefabs.health_bar import HealthBar
from ursina import *
from ursina import curve


path = []

enemy = Entity(model="sphere", color=color.red, scale=.5, visible = False, health=100)

# Sağlık çubuğunu oluşturun
health_bar = Entity(model='quad', scale=(2, .2), color=color.green, parent=enemy, billboard = True)
health_bar.y = 1  # Sağlık çubuğunu uçağın üstüne yerleştirin


def go(enemy, pos, delay):
    enemy.animate('position', (pos[0], .1, pos[2]), duration = 2, curve = curve.linear)

def move(path):
    enemy.position = path[0].position
    invoke(setattr, enemy, "visible", True, delay=2.5)
    counter = 0
    for cube in path:
        counter += 2
        invoke(go, enemy, cube.position, counter, delay = counter)

def change_health_bar():
    global enemy
    # Decrease health (fuel)
    enemy.health -= 0.1  # For example, reduce 0.1 units of health in each update loop

    # Update the health bar
    health_percentage = enemy.health / 100.0  
    if health_percentage < 0.002:
        health_percentage = 0.01

    health_bar.scale_x = health_percentage * 2  # Ensure the health bar does not take negative values

    # End the game when health is depleted
    if enemy.health <= 0:
        destroy(enemy, delay=1)
        return False
        
