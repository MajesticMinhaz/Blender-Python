import bpy
import csv
import os


coll_obj_name = []
rows = []

outputFilePath = os.path.dirname(bpy.data.filepath)
file = f'{outputFilePath}/main.blend'
bpy.ops.wm.save_mainfile(filepath=file)

for object in bpy.data.objects:
    coll_obj_name.append(object.name)

with open(f'{outputFilePath}/test.csv', 'r', encoding='UTF8') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        rows.append(row)

for x in range(len(rows)):
    csvFileName = f'{rows[x][0]}'
    hideObj = [ele for ele in coll_obj_name if ele not in rows[x]]
    scene = bpy.context.scene
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.filepath = os.path.join(outputFilePath, csvFileName)
    for y in hideObj:
        # Select the object
        # bpy.data.objects[delValue].select = True    # Blender 2.7x
        bpy.data.objects[y].select_set(True)  # Blender 2.8x
        bpy.data.objects[y].hide_render = True
    bpy.ops.render.render(write_still=True)
    for z in hideObj:
        # Select the object
        # bpy.data.objects[delValue].select = True    # Blender 2.7x
        bpy.data.objects[z].select_set(True)  # Blender 2.8x
        bpy.data.objects[z].hide_render = False
    rows[x].append(f'{csvFileName}.png')    
with open(f'{outputFilePath}/test1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    f.close()
    
    
