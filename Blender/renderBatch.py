import os

def render(path, name):
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.filepath=path+name
    bpy.ops.render.render(write_still = 1)
    print("Render done : "+path+name)

pathMain = "C:/Users/chupi/Downloads/Vostok/Images/VosMod/"
handcolors=["Gold", "Silver", "WhiteMat", "BlackMetalMat", "RedMetalMat", "OrangeMat", "YellowMat"]
glowcolors=["GlowGreen", "GlowBlue", "GlowYellow"]

hands = ["Seconds", "Minutes", "Hours"]
for h in enumerate(hands):
    #cleaning
    for n,o in enumerate(bpy.data.collections[h[1]].objects):
        bpy.data.collections[h[1]+".001"].objects.link(o)
        bpy.data.collections[h[1]].objects.unlink(o)
    pathtype = pathMain + "Hands/"+ h[1] + "/"
    bpy.data.collections[h[1]].hide_render = False
    for n,o in enumerate(bpy.data.collections[h[1]+".001"].objects):
        o.hide_render=False
        bpy.data.collections[h[1]].objects.link(o)
        bpy.data.collections[h[1]+".001"].objects.unlink(o)
        pathhand = pathtype + o.name +"/"
        namehand = o.name
        for hc in enumerate(handcolors):
            handmat = bpy.data.materials.get(hc[1])
            o.data.materials[0] = handmat
            namecolored = namehand + "_" + hc[1]
            path = pathhand + hc[1] + "/"
            if len(o.data.materials)>1:
                for gc in enumerate(glowcolors):
                    glowmat = bpy.data.materials.get(gc[1])
                    o.data.materials[1] = glowmat
                    name = namecolored + "_" + gc[1] + ".png"
                    render(path, name)
            else:
                name = namecolored + ".png"
                render(path, name)
        o.hide_render=True
    bpy.data.collections[h[1]].hide_render = True
    #cleaning
    for n,o in enumerate(bpy.data.collections[h[1]].objects):
        bpy.data.collections[h[1]+".001"].objects.link(o)
        bpy.data.collections[h[1]].objects.unlink(o)

#Bezel Rendering
pathBezelImages = "C:/Users/chupi/Downloads/Vostok/_Parts/Bezels/"
dir = os.listdir(pathBezelImages)
#cleaning
for n,o in enumerate(bpy.data.collections["Bezels"].objects):
    bpy.data.collections["Bezels.001"].objects.link(o)
    bpy.data.collections["Bezels"].objects.unlink(o)

pathtype = pathMain + "Bezels/"
bpy.data.collections["Bezels"].hide_render = False
for n,o in enumerate(bpy.data.collections["Bezels.001"].objects):
    bpy.data.collections["Bezels"].objects.link(o)
    bpy.data.collections["Bezels.001"].objects.unlink(o)
    o.hide_render=False
    path = pathtype + o.name +"/"
    namebezel = o.name
    if len(o.data.materials)>1:
        if o.material_slots[1].name=="BezelImage":
            for file in dir:
                if file.lower().endswith('.png'):
                    bezel_img = bpy.data.images.load(filepath = pathBezelImages + file)
                    o.material_slots[1].material.node_tree.nodes[3].image = bezel_img
                    name = namebezel + "_" + file
                    render(path, name)
        else:
            name = namebezel + ".png"
            render(path, name)
    else:
        name = namebezel + ".png"
        render(path, name)
    o.hide_render = True

bpy.data.collections["Bezels"].hide_render = True
#cleaning
for n,o in enumerate(bpy.data.collections["Bezels"].objects):
    bpy.data.collections["Bezels.001"].objects.link(o)
    bpy.data.collections["Bezels"].objects.unlink(o)


