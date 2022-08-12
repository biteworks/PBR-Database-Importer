import bpy


class PBRDBIMPORTER_OT_CreateMaterial(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_material"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected material preset:", pbrdbimporter.material_list)

        return {'FINISHED'}


class PBRDBIMPORTER_OT_CreateLightSource(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_light_source"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected light source preset:", pbrdbimporter.light_source_list)

        return {'FINISHED'}


class PBRDBIMPORTER_OT_CreateCamera(bpy.types.Operator):
    bl_label = "Create material"
    bl_idname = "pbrdbimporter.create_camera"

    def execute(self, context):
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        print("Selected camera preset:", pbrdbimporter.camera_list)

        return {'FINISHED'}
