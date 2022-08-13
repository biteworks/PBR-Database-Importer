import bpy
from . PBR_DB_Connect import *


class PBRDBIMPORTER_Props(bpy.types.PropertyGroup):

    materialConnection = PBR_DB_Connect("materials")
    lightSourcesConnection = PBR_DB_Connect("lightsources")
    camerasConnection = PBR_DB_Connect("cameras")

    materialList: bpy.props.EnumProperty(
        name="List of base material presets",
        description="List of base material presets",
        items=materialConnection.getListOfNames()
    )

    lightSourceList: bpy.props.EnumProperty(
        name="List of light source presets",
        description="List of light source presets",
        items=lightSourcesConnection.getListOfNames()
    )

    cameraList: bpy.props.EnumProperty(
        name="List of camera presets",
        description="List of camera presets",
        items=camerasConnection.getListOfNames()
    )

    assignMaterialToObject: bpy.props.BoolProperty(
        name="Add material to selected objects",
        description="If checked, the new created material will be assign to selected objects",
        default=False
    )

    addFakeUserToMaterial: bpy.props.BoolProperty(
        name="Add Fake User to material",
        description="If checked, the new created material will get a fake user attribute",
        default=True
    )
