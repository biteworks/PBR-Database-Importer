from operator import ior
import bpy


class PBRDBIMPORTER_OT_CreateMaterial(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_material"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected material preset:", pbrdbimporter.materialList)
        materialName = "PBR_" + pbrdbimporter.materialList

        ior = 1.2

        if bpy.data.materials.get(materialName) is None:

            # Create material and assign Principled BSDF
            material = bpy.data.materials.new(name=materialName)
            material.use_nodes = True
            material.use_fake_user = True
            principled_node = material.node_tree.nodes.get('Principled BSDF')

            # Base color
            principled_node.inputs[0].default_value = (
                0.8, 0.0669999, 0.0974493, 1)
            # Metalness
            principled_node.inputs[6].default_value = 0.5
            # Specular
            principled_node.inputs[7].default_value = (
                (ior - 1)/(ior + 1)) ** 2 / 0.08
            # Roughness
            principled_node.inputs[9].default_value = 0.5
            # IOR
            principled_node.inputs[16].default_value = 0.5

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
