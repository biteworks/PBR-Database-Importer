import bpy


class PBRDBIMPORTER_Props(bpy.types.PropertyGroup):

    material_list: bpy.props.EnumProperty(
        name="List of base materials presets",
        description="List of base materials presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
    )

    light_source_list: bpy.props.EnumProperty(
        name="Light of light sources presets",
        description="Light of light sources presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
    )

    camera_list: bpy.props.EnumProperty(
        name="List of cameras presets",
        description="List of cameras presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
    )
