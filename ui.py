import bpy


class PBRDBIMPORTER_PT_Panel(bpy.types.Panel):
    bl_label = "PhysicallyBased-Database-Importer"
    bl_idname = "PBRDBIMPORTER_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PBR-DB-Importer"

    def draw(self, context):
        return


class PBRDBIMPORTER_PT_MaterialPanel(bpy.types.Panel):
    bl_label = "Materials"
    bl_idname = "PBRDBIMPORTER_PT_MaterialPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PBR-DB-Importer"
    bl_parent_id = "PBRDBIMPORTER_PT_Panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        layout.prop(pbrdbimporter, "material_list", text="")
        layout.operator("pbrdbimporter.create_material",
                        text="Create material", icon="MATERIAL_DATA")
        layout.separator()


class PBRDBIMPORTER_PT_LightSourcesPanel(bpy.types.Panel):
    bl_label = "Light Sources"
    bl_idname = "PBRDBIMPORTER_PT_LightSourcesPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PBR-DB-Importer"
    bl_parent_id = "PBRDBIMPORTER_PT_Panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        layout.prop(pbrdbimporter, "light_source_list", text="")
        layout.operator("pbrdbimporter.create_light_source",
                        text="Create light source", icon="LIGHT_DATA")
        layout.separator()


class PBRDBIMPORTER_PT_CamerasPanel(bpy.types.Panel):
    bl_label = "Cameras"
    bl_idname = "PBRDBIMPORTER_PT_CamerasPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PBR-DB-Importer"
    bl_parent_id = "PBRDBIMPORTER_PT_Panel"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        pbrdbimporter = scene.pbrdbimporterprops

        layout.prop(pbrdbimporter, "camera_list", text="")
        layout.operator("pbrdbimporter.create_camera", text="Create camera",
                        icon="CAMERA_DATA")
        layout.separator()
