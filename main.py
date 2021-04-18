from flask import Flask, request, send_file
from mcstatus import MinecraftServer

__author__ = 'Xiao_Jin'

app = Flask(__name__)


class icons(object):
    '''Response icons'''
    offline: str = 'icons/offline.svg'
    online: str = 'icons/online.svg'
    warning: str = 'icons/warning.svg'


# https://example.com/status-icon?addr=mc.hypixel.net
@app.route('/status-icon', methods=['GET'])
def route_status():
    _httpGetArgs = request.args
    if 'addr' in _httpGetArgs:
        serverAddr: str = _httpGetArgs.get('addr')
        resIcon = icons.online if isServerOnline(serverAddr) else icons.offline
        return send_file(resIcon)
    else:
        return send_file(icons.warning)


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Cache-Control'] = 'no-store'
    return response


def isServerOnline(_serverAddr: str) -> bool:
    '''Check whether `_serverAddr` is online.

    Args:
        _serverAddr: Minecraft Server address'''
    server = MinecraftServer.lookup(_serverAddr)
    try:
        server.status()
        return True
    except Exception:
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
