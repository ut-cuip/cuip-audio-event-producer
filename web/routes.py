from .controllers import Events, EventsUpdate

routes = [
    (r'^/events/$', Events),
    (r'^/events/update/$', EventsUpdate),
]
