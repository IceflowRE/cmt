from cmt.blender.v2_80 import import_menu, viewport_add_menu, scene_panel, object_panel

bl_info = {
    "name": "Celaria Map Importer/Exporter",
    "description": "Import or export an Celaria Map.",
    "author": "Iceflower S",
    "version": (0, 3, 0),
    "blender": (2, 80, 0),
    "location": "File > Import/Export > Celaria Map",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/iceflowre/cmt/issues",
    "support": "TESTING",
    "category": "Import-Export"
}


def register():
    # import menu
    import_menu.register()
    # 3D view add menu
    viewport_add_menu.register()
    # scene property panel
    scene_panel.register()
    # object panel
    object_panel.register()


def unregister():
    # import menu
    import_menu.unregister()
    # 3D view add menu
    viewport_add_menu.unregister()
    # scene property panel
    scene_panel.unregister()
    # object panel
    object_panel.unregister()
