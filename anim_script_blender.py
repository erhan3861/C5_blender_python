import bpy
import json

loc_dict = {}

def save_helicopter_position(frame):
    # Helikopter objesini seç
    helicopter_obj = bpy.data.objects.get("Helicopter.007")

    if helicopter_obj:
        # Belirli çerçevedeki sahne konumunu ayarla
        bpy.context.scene.frame_set(frame)

        # Helikopterin sahne konumunu al
        location = helicopter_obj.location

        # Konumu JSON formatına dönüştür
        loc_dict[frame] = (location.x,  location.z, location.y)
        
        print("Helikopter konumu çerçeve {} için başarıyla kaydedildi.".format(frame))
        
        

    else:
        print("Helikopter objesi bulunamadı.")

# Örneğin, 250. çerçevedeki konumu kaydetmek için:
for i in range(250):
    save_helicopter_position(i)

# JSON dosyasına yaz
with open("D:\pythonDerslerim\C5_blender_python\helicopter_position.json", "w") as file:
    json.dump(loc_dict, file)

