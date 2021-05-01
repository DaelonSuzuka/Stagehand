from .obs_extension import ObsExtension


obs = ObsExtension()


api = {
    'set scene': {
        'method': obs.set_scene,
        'fields': ['scene'],
    },
    'toggle mute': {
        'method': obs.toggle_mute,
        'fields': ['source'],
    },
    'mute': {
        'method': obs.mute,
        'fields': ['source'],
    },
    'unmute': {
        'method': obs.unmute,
        'fields': ['source'],
    },
    'enable filter': {
        'method': obs.enable_filter,
        'fields': ['source', 'filter'],
    },
    'disable filter': {
        'method': obs.disable_filter,
        'fields': ['source', 'filter'],
    },
}