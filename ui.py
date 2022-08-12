import bpy


class PBRDBIMPORTER_PT_Panel(bpy.types.Panel):
    bl_label = "PBR-DB-Importer"
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

        layout.prop(pbrdbimporter, "materialList", text="")
        layout.prop(pbrdbimporter, "assignMaterialToObject")
        layout.prop(pbrdbimporter, "addFakeUserToMaterial")
        layout.operator("pbrdbimporter.create_material",
                        text="Create material", icon="MATERIAL_DATA")


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

        layout.prop(pbrdbimporter, "lightSourceList", text="")
        layout.operator("pbrdbimporter.create_light_source",
                        text="Create light source", icon="LIGHT_DATA")


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

        layout.prop(pbrdbimporter, "cameraList", text="")
        layout.operator("pbrdbimporter.create_camera", text="Create camera",
                        icon="CAMERA_DATA")


class PBRDBIMPORTER_PT_AboutPanel(bpy.types.Panel):
    bl_label = "About"
    bl_idname = "PBRDBIMPORTER_PT_AboutPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PBR-DB-Importer"
    bl_parent_id = "PBRDBIMPORTER_PT_Panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        layout.label(text="Link to github repo")
        op1 = self.layout.operator(
            'wm.url_open',
            text='GitHub Repo',
            icon='URL'
        )
        op1.url = 'https://github.com/biteworks/PBR-Database-Importer'

        layout.label(text="Link to database")
        op2 = self.layout.operator(
            'wm.url_open',
            text='physicallybased.info',
            icon='URL'
        )
        op2.url = 'https://physicallybased.info'
