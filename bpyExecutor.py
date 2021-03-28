import bpy
bl_info = {
    "name": "bpyExecutor",
    "blender": (1, 0, 0),
    "blender": (2, 90, 0),
    "description": "Execute python code for macros.",
    "author": "Abrasic",
    "category": "System",
}

class bep(bpy.types.Operator):
    bl_idname = "screen.dialog"
    bl_label = ""

    type : bpy.props.StringProperty(name="Run")
        
    @classmethod
    def poll(cls, context):
        return True

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=500)
        
    def execute(self, context):
        exec(self.type)
        return {'FINISHED'}   

    def draw(self, context):
        row = self.layout
        row.prop(self, "type", text="Run")
        row.separator()

class be(bpy.types.Operator):
    bl_idname = "screen.run"
    bl_label = "Run Python Code"
    bl_options = {"INTERNAL", "UNDO"}
    bl_description = bl_label

    def draw(self, context):
        layout = self.layout
        layout.operator(be.bl_idname)
        
    def execute(self, context):
        bpy.ops.screen.dialog('INVOKE_DEFAULT')
        return {'FINISHED'}
        
def menu_func(self, context):
    self.layout.operator(be.bl_idname, icon="SCRIPT")

addon_keymaps = []

def register():
    bpy.utils.register_class(bep)
    bpy.utils.register_class(be)
    bpy.types.TOPBAR_MT_edit.append(menu_func)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='Edit', space_type='TOPBAR')
        kmi = km.keymap_items.new(be.bl_idname, 'Y', 'PRESS', alt=True, ctrl=False, shift=False)
        addon_keymaps.append((km, kmi))

def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(be)
    bpy.utils.unregister_class(bep)
    bpy.types.TOPBAR_MT_edit.remove(menu_func)

if __name__ == "__main__":
    register()
