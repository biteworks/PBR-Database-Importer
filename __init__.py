from . ui import *
from . operators import *
from . props import *
import bpy

bl_info = {
    "name": "PBR-Database-Importer",
    "description": "",
    "author": "biteworks (Add-on), Anton Palmqvist (Database)",
    "version": (0, 0, 1),
    "blender": (2, 83, 0),
    "location": "3D View > Tools",
    "warning": "",
    "wiki_url": "https://github.com/biteworks/PBR-Database-Importer/wiki",
    "tracker_url": "",
    "category": "Generic"
}

classes = (
    PBRDBIMPORTER_Props,
    PBRDBIMPORTER_OT_CreateMaterial,
    PBRDBIMPORTER_OT_CreateLightSource,
    PBRDBIMPORTER_OT_CreateCamera,
    PBRDBIMPORTER_PT_Panel,
    PBRDBIMPORTER_PT_MaterialPanel,
    PBRDBIMPORTER_PT_LightSourcesPanel,
    PBRDBIMPORTER_PT_CamerasPanel
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.pbrdbimporterprops = bpy.props.PointerProperty(
        type=PBRDBIMPORTER_Props)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.pbrdbimporterprops


if __name__ == "__main__":
    register()