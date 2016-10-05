bl_info = {
	"name": "Grid UV",
	"author": "Nexus Studio",
	"version": (0, 1),
	"blender": (2, 78),
	"location": ""T" menu > Nexus tools",
	"description": "Generate image grid uv given increments of pixel",
	"warning": "",
	"wiki_url": "none",
	"category": "User",
}

import bpy
from bpy.props import *


class UV_generate_grid(bpy.types.Operator):
	"""Calculate explode meshes"""
	bl_label = "Calculate explode meshes"
	bl_idname = "scene.grid_uv"
	bl_options = {'REGISTER', 'UNDO'}

	@classmethod
	def poll(cls, context):
		return context.mode == "OBJECT"

	def execute(self, context):
		w = bpy.context.scene.width_grid_uv
		h = bpy.context.scene.height_grid_uv
		sw = bpy.context.scene.step_w
		sh = bpy.context.scene.step_h

		image = bpy.data.images.new("GridUV", width=w, height=h)
		pixels = [None] * w * h
		for x in range(w):
			for y in range(h):
				if ((x % sw) == 0) and ((y % sh) == 0):
					r = 1.0
					g = 1.0
					b = 1.0
				elif (x % sw) == 0:
					r = 1.0
					g = 1.0
					b = 1.0
				elif (y % sh) == 0:
					r = 1.0
					g = 1.0
					b = 1.0
				else:
					r = 0.0
					g = 0.0
					b = 0.0

				a = 1.0

				pixels[(y * w) + x] = [r, g, b, a]

		# flatten list
		pixels = [chan for px in pixels for chan in px]

		# assign pixels
		image.pixels = pixels

		# write image
		# image.filepath_raw = "E:/Download/temp.png"
		# image.file_format = 'PNG'
		# image.save()
		return {'FINISHED'}


class GridUVPanel(bpy.types.Panel):
	"""Creates a Panel in the view3d context of the tools panel (key "T")"""
	bl_label = "Grid UV"
	bl_idname = "griduvid"
	bl_space_type = 'IMAGE_EDITOR'
	bl_region_type = 'TOOLS'
	bl_category = "Nexus Tools"

	bpy.types.Scene.width_grid_uv = IntProperty(
		name = "Width",
		min = 0,
		default = 512,
		description = "Width image"
	)
	bpy.types.Scene.height_grid_uv = IntProperty(
		name = "Height",
		min = 0,
		default = 512,
		description = "Height image"
	)

	bpy.types.Scene.step_w = IntProperty(
		name = "Step width",
		min = 0,
		default = 1,
		description = "Width step"
	)
	bpy.types.Scene.step_h = IntProperty(
		name = "Step height",
		min = 0,
		default = 1,
		description = "Height step"
	)

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		box = layout.box()
		box.label(text="Grid UV:")

		box.operator("scene.grid_uv", text="Generate grid")

		col = box.column()
		col.label(text="Size image")
		col.prop(scene, "width_grid_uv", text="Width")
		col.prop(scene, "height_grid_uv", text="Height")

		col = box.column()
		col.label(text="Step")
		col.prop(scene, "step_w", text="Width")
		col.prop(scene, "step_h", text="Height")




def register():
	bpy.utils.register_class(UV_generate_grid)
	bpy.utils.register_class(GridUVPanel)

def unregister():
	bpy.utils.unregister_class(UV_generate_grid)
	bpy.utils.unregister_class(GridUVPanel)

if __name__ == "__main__":
	register()