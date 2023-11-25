from ursina import *


def input(key):
    if key == "1":
        print_on_screen(f"Delta Drag : {Vec3(player.delta_drag)}")
    elif key == "2":
        print_on_screen(f"Start Position : {Vec3(player.start_pos)}")

def update():
    if player.stop_dragging:
        for g in grounds:
            if distance_xz(player, g)<.5:
                player.position = g.position

    if player.dragging:
        for g in grounds:
            if distance_xz(player, g) < .5:
                g.color = color.lime
            else:
                g.color = color.white


app = Ursina(borderless=False)


# ground = Entity(model='plane', scale=8, texture='white_cube', texture_scale=(8,8))
grounds = []
for i in range(10):
    for j in range(10):
        ground = Entity(model='plane', position=(-5+i,0,5-j),texture='white_cube')
        grounds.append(ground)

player = Draggable(parent=scene, model='cube', color=color.azure, plane_direction=(0,1,0), lock=(0,1,0), scale=.5)

Sky()

EditorCamera()

app.run()