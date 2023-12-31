from ursina import *
from ursina import curve
from random import randint


class Car(Entity):
    def __init__(self, position=Vec3(0), **kwargs):
        super().__init__()
        self.position=position
        self.lines = Entity(model=Mesh(vertices=[self.position, self.position], mode='line', thickness=1), color=color.random_color())
        self.collider = "box"
        self.on_click = self.select_obj
        self.delay = 0
        self.clicked = False
        self.go = False
        self.show_points = False
        self.scale = 5
        self.event_list = []
        
        # kullanıcı tanımlı ekstra özellikleri de nesneye ekle
        for key, value in kwargs.items():
            setattr(self, key, value)

    def input(self, key):
        # sahnede sol tıklama yaptığımız aracı aktif yap, diğer araçları pasif yap
        if key == "left mouse down" and distance(self, mouse.world_point) < 5:
            for e in scene.entities:
                if hasattr(e, "lines"):
                    e.clicked = False # arabanın seçimini iptal et
                    e.color = color.white # orjinal rengine çevir

            self.clicked = True # arabayı seç
            self.color = color.lime

        if key == "right mouse down" and distance(self, mouse.world_point) < 5:
            self.go = True # sağ tıklama ile arabayı hareket ettir

        if key == "middle mouse down" and mouse.world_point and self.clicked:
            # sahnedeki mouse konumunu al
            x=mouse.world_point[0]
            y=mouse.world_point[1] 
            z=mouse.world_point[2]
            self.lines.model.vertices.append(Vec3(x,y,z))
            
            # arabanın rotasını güncelle
            self.lines.model.generate()

        if key == "c":
            self.clicked = False
            for s in self.event_list:
                s.kill()
            self.event_list.clear()
            self.delay = 0 

        if key == "p" and self.clicked:
            self.show_points = not self.show_points 

            # eğer noktaları göster özelliği açık ise
            if self.show_points: 
                # önceki noktaları sil
                for p in Point.pointList:
                    destroy(p)

                Point.pointList.clear()

                # güncel noktaları ekle
                for coor in self.lines.model.vertices:
                    point = Point(position=coor)
                    Point.pointList.append(point)

            else:
                # eğer noktaları göster kapalı ise noktaları gizle
                for p in Point.pointList:
                    p.visible = False

    def update(self):
        if self.go:
            for pos in self.lines.model.vertices[2:]:
                self.delay += 3
                s = invoke(self.goTo, pos, delay=self.delay)
                self.event_list.append(s)
        
        if self.clicked and Point.pointList:
            try:
                self.lines.model.vertices[Point.index] = Point.pointList[Point.index].position
                self.lines.model.generate()
            except: pass

    def select_obj(self):
        self.clicked = True # mouse takip edebiliyor
        self.visible = True # nesneyi görünür yap 

    def goTo(self, pos): 
        self.look_at_2d(Vec3(pos), axis="y")

        self.rotation_y += 180

        # İki nokta arasındaki uzaklık hesaplanır
        distance_to_target = distance(self, Vec3(pos))

        # Arabanın rotation_x değeri hesaplanır
        self.rotation_x = math.degrees(math.atan2(pos[1] - self.y, distance_to_target))

        self.animate_position(pos, duration=3, curve=curve.linear)

class Point(Entity):
    pointList = []
    index = 0
    def __init__(self, position=Vec3(0), **kwargs):
        super().__init__()
        self.model = "sphere"
        self.position = position
        self.scale = .5
        self.color = color.red
        self.collider = "sphere"
        self.on_click = self.select

        # kullanıcı tanımlı ekstra özellikleri de nesneye ekle
        for key, value in kwargs.items():
            setattr(self, key, value)

    def select(self):
        for p in Point.pointList:
            p.color = color.red
        self.color = color.lime

    def input(self, key):
        if key == "left mouse down" and mouse.hovered_entity == self:
            self.select()
 

        if key == "up arrow" and self.color == color.lime:
            if self in Point.pointList:
                Point.index = Point.pointList.index(self)
                self.y += .1
            

        if key == "down arrow" and self.color ==  color.lime:
            if self in Point.pointList:
                Point.index = Point.pointList.index(self)
                self.y -= .1
            
