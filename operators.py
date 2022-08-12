import bpy
from . PBR_DB_Connect import *


class PBRDBIMPORTER_OT_CreateMaterial(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_material"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected material preset:", pbrdbimporter.materialList)
        materialName = "PBR_" + pbrdbimporter.materialList

        # Get material attributes
        materialConnection = PBR_DB_Connect("materials")
        materialAttributes = materialConnection.getMaterialAttributes(
            pbrdbimporter.materialList)

        if bpy.data.materials.get(materialName) is None:

            # Create material and assign Principled BSDF
            material = bpy.data.materials.new(name=materialName)
            material.use_nodes = True
            if (pbrdbimporter.addFakeUserToMaterial):
                material.use_fake_user = True
            principled_node = material.node_tree.nodes.get('Principled BSDF')

            # Base color
            principled_node.inputs[0].default_value = (
                materialAttributes["color"][0], materialAttributes["color"][1], materialAttributes["color"][2], 1)
            # Metalness
            principled_node.inputs[6].default_value = materialAttributes["metalness"]
            # Specular
            principled_node.inputs[7].default_value = (
                (materialAttributes["ior"] - 1)/(materialAttributes["ior"] + 1)) ** 2 / 0.08
            # Roughness
            principled_node.inputs[9].default_value = materialAttributes["roughness"]
            # IOR
            principled_node.inputs[16].default_value = materialAttributes["ior"]
            # Transmission if is used
            if "transmission" in materialAttributes:
                principled_node.inputs[17].default_value = materialAttributes["transmission"]

            # Set viewport display and alpha blending
            material.diffuse_color = (
                materialAttributes["color"][0], materialAttributes["color"][1], materialAttributes["color"][2], 1)
            material.metallic = materialAttributes["metalness"]
            material.roughness = materialAttributes["roughness"]
            if "transmission" in materialAttributes:
                material.blend_method = 'BLEND'
                material.use_screen_refraction = True

            infoMessage = materialName + ' is created'
            self.report({'INFO'}, infoMessage)

            if (pbrdbimporter.assignMaterialToObject):
                objs = bpy.context.selected_objects

                if not objs:
                    errorMessage = 'Nothing selected'
                    self.report({'ERROR'}, errorMessage)
                else:
                    for obj in objs:
                        if obj.data.materials:
                            obj.data.materials[0] = material
                        else:
                            obj.data.materials.append(material)
        else:
            errorMessage = materialName + ' already exists.'
            self.report({'ERROR'}, errorMessage)

        return {'FINISHED'}


class PBRDBIMPORTER_OT_CreateLightSource(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_light_source"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected light source preset:", pbrdbimporter.lightSourceList)

        return {'FINISHED'}


class PBRDBIMPORTER_OT_CreateCamera(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_camera"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected camera preset:", pbrdbimporter.cameraList)

        return {'FINISHED'}
