import sublime, sublime_plugin, os, sys
sys.path.append('lib')
import source_tools

class Actionscript3Run(sublime_plugin.TextCommand):
	"""
	Open project
	"""
	def run(self, edit):
		st = source_tools.SourceTools(self.view.file_name())
		os.system("open %s" % os.path.join(st.project_path, st.config['default'][0]['open']).replace(' ','\ '))
