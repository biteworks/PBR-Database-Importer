import bpy


class PBRDBIMPORTER_Props(bpy.types.PropertyGroup):

    materialList: bpy.props.EnumProperty(
        name="List of base materials presets",
        description="List of base materials presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
    )

    lightSourceList: bpy.props.EnumProperty(
        name="Light of light sources presets",
        description="Light of light sources presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
    )

    cameraList: bpy.props.EnumProperty(
        name="List of cameras presets",
        description="List of cameras presets",
        items=[('OP1', "Option 1", ""),
               ('OP2', "Option 2", ""),
               ('OP3', "Option 3", ""),
               ]
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
