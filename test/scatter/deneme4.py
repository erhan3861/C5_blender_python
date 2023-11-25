from ursina import *


fire_shader = Shader(
    vertex='''
        #version 140
        uniform mat4 p3d_ModelViewProjectionMatrix;
        in vec4 p3d_Vertex;
        out vec4 position;

        void main() {
            position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
            gl_Position = position;
        }
    ''',
    fragment='''
        #version 140
        uniform float time;
        out vec4 fragColor;

        void main() {
            float strength = 1.0 - abs(sin(time * 5.0));
            vec3 color = vec3(1.0, 0.5, 0.0);  // Ateş rengi

            fragColor = vec4(color * strength, strength);
        }
    ''',
    geometry='',
    tessellation='',
    compute=''
)

class Fire(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model='quad',
            position=position,
            scale=(2, 2, 2),
            shader=fire_shader
        )

app = Ursina()
fire = Fire()

def update():
    fire.shader.set_uniform('time', time.time())

app.run()