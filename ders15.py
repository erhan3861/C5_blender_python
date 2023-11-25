from ursina import *
from ursina.shaders import basic_lighting_shader as bls, lit_with_shadows_shader
from ders15_move import *
from ders15_tower import *

Entity.default_shader = bls

cubes = []
highlighted_cubes = []
targets = []
towers = []

def input(key):
    global highlighted_cubes
    if key == "right mouse down":
    
        if mouse.world_point == None:
            return
        
        for cube in grounds:
            if distance_xz(cube, mouse.world_point) < .5:
                cube.color = color.light_gray
                if cube in highlighted_cubes:
                    highlighted_cubes.remove(cube)
                    break

    if key == "space":
        print(cam.position)
        print(cam.rotation)

    if key == "x":
        move(targets)

    elif key == "t":
        tower = Tower(position = (1,0,2), range=3, damage=10)
        tower.target = enemy
        tower.target_list.append(tower.target)
        towers.append(tower)

        # shaders for entities of other classes
        tower.range_circle.shader = lit_with_shadows_shader
        if enemy:
            enemy.shader = bls

def update():
    for tower in towers:
        # Fire at the target
        tower.fire(tower.target)
        
        # Check if there is hitting
        print("tower target", tower.target_list)
        if tower.target_list:
            Tower.check_hitting(tower)

        tower.show_range()
    

                
def on_click_cube(cube):
    global cubes

    if len(cubes) == 1:
        cube.color = color.orange
        cubes.append(cube)

        start_cube, end_cube = tuple(cubes)
        
        find_path(start_cube, end_cube)
        mark_path(highlighted_cubes)

        
        cubes[0].texture = "white_cube" 
        cubes.clear() # ilk seçimi çıkar
    else:
        cube.color = color.orange
        cube.texture = "one.jpg" 
        cubes.append(cube)

def find_path(start, end):
    global highlighted_cubes
    
    if check_width(start, end):
        print_on_screen("Lütfen aynı x veya z düzlemi seçiniz.", scale=2, position=(-.5,0))
        return 
    
    if highlighted_cubes and start not in highlighted_cubes:
        print_on_screen("Start position must be in green path", scale=2, position=(-.5,0))
        return
    
    for cube in grounds:
        if is_between(start, end, cube) or is_between(end, start, cube):                    
            highlighted_cubes.append(cube)
        else:
            cube.color = color.light_gray

    # put first cube in targets list
    if not targets:
        targets.append(start)

    # put end cubes in targets list
    if end not in targets:
        targets.append(end)
    

def check_width(start, end):
    if abs(start.x - end.x) > 0 and abs(start.z - end.z) > 0:
        return True
        

def is_between(a, b, c):
    # Check if point 'c' is between points 'a' and 'b' along both axes
    x_between = min(a.x, b.x) <= c.x <= max(a.x, b.x)
    z_between = min(a.z, b.z) <= c.z <= max(a.z, b.z)
    return x_between and z_between

def mark_path(path):
    for cube in path:
        cube.color = color.lime


app = Ursina()

Sky(texture = "sky_sunset")

grounds = []

# Create ground cubes
for x in range(20):
    for z in range(20):
        cube = Entity(model='cube', position=(x, -0.5, z), color=color.light_gray, texture="white_cube")
        cube.collider = 'box'
        cube.on_click = lambda x=cube: on_click_cube(x)
        grounds.append(cube)

# Yukarıdan oyun alanına doğru bakacak bir kamera ekleyin
cam = EditorCamera()
cam.position = Vec3(10.4199, 13.6906, -4)
cam.rotation = Vec3(50.9669, -1.30302, 0)

app.run()
