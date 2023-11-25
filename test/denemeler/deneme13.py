from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina import curve
import random

particle_list = []

def update():
    cube.rotation_y += 1

def input(key):
    anim_time = 0
    if key == "left mouse down":
        mouse_position = mouse.world_point
        cube.animate_position(mouse_position, duration=0.5, curve=curve.in_out_quad)
        cube.color = color.random_color()
        for _ in range(100):
            anim_time += 0.5 / 110
            invoke(create_particle_effect, cube.position, mouse_position, color.yellow, delay=anim_time)

def on_mouse_enter():
    cube.color = color.lime

def on_mouse_exit():
    cube.color = color.red

def create_particle_effect(start_position, end_position, particle_color):
    particle_position = start_position
    dist = distance(start_position, end_position)
    particle_velocity = (end_position - start_position).normalized() * random.uniform(0.2, 1.0) 

    particle = Entity(
        model='sphere',
        color=particle_color,
        scale=0.5,
        position=start_position,
        always_on_top=True
    )

    dist = distance(start_position, end_position)


    particle.animate_position(
        particle.position + particle_velocity * len(particle_list) * dist / 100,  
        # Parçacığın hareket etmesi için hedef pozisyon
        curve=curve.linear
    )

    particle.animate_scale(
        particle.scale * 0.1,  # Parçacığın küçülerek kaybolması için hedef ölçek
        duration=1.0,
        curve=curve.linear,
        delay=0.5  # Parçacığın önce büyüyüp sonra küçülmesi için gecikme
    )

    particle_list.append(particle)
    invoke(remove_particle_effect, particle, delay=1.5)

def remove_particle_effect(particle):
    particle_list.remove(particle)
    destroy(particle)

def update_particles():
    for particle in particle_list:
        particle.position += particle.velocity * time.dt

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

cube = Entity(model="cube", color=color.red, scale=1.5, collider="box")
ground = Entity(model="plane", scale=200, texture="grass", collider="box")

cube.on_mouse_enter = on_mouse_enter
cube.on_mouse_exit = on_mouse_exit

editor_camera = EditorCamera()
directional_light = DirectionalLight()
directional_light.look_at((-1, -1, 1))

app.run()
