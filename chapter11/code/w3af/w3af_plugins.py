from w3af.core.controlles.w3afCore import w3afCore

w3af = w3afCore()

#list of plugins in audit category
pluginType = w3af.plugins.get_plugin_list('audit')
for plugin in pluginType:
	print('Plugin:'+plugin)
	
#list of available plugin categories
plugins_types = w3af.plugins.get_plugin_types()
for plugin in plugins_types:
	print('Plugin type:'+plugin)
	
#list of enabled plugins
plugins_enabled = w3af.plugins.get_enabled_plugin('audit')
for plugin in plugins_enabled:
	print('Plugin enabled:'+plugin)
	
