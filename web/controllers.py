from six import StringIO
from six.moves import http_client
from dh_webconfig.base import Controller, BaseController


class Events(Controller):
    def get(self, handler, *args, **kwargs):
        response = self.render_template('events.html')

        handler.send_response(http_client.OK)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(response.encode())


class EventsUpdate(Controller):
    def get(self, handler, *args, **kwargs):
        f = StringIO()
        for timestamp, predictions in handler.server.server.events_queue:
            data = {
                'timestamp': '{:%Y-%m-%d %H:%M:%S}'.format(timestamp),
                'predictions': predictions
            }
            f.writelines(self.render_template('event.html', **data))

        response = f.getvalue()
        f.close()

        handler.send_response(http_client.OK)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(response.encode())
