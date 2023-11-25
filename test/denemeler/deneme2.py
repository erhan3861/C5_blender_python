from ursina import *
from ursina import curve


def update():
    cube.rotation_y += 1

def input(key):
    if key == "left mouse down":
        cube.animate_scale((2, 2, 2), duration=0.5, curve=curve.in_out_quad)
        cube.color = color.random_color()

def on_mouse_enter():
    cube.animate_color(color.lime, duration=0.2)

def on_mouse_exit():
    cube.animate_color(color.red, duration=0.2)

app = Ursina()

cube = Entity(model="cube", color=color.red, scale=1.5,collider="box")
ground = Entity(model="plane", scale=10, texture="grass", collider="box")

app.run()
