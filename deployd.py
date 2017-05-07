import daemon
import web
import os
import random

app = web.application()

class FileReceiver:
    def POST(self, path):
        web_input = web.input(data={}, cmd='')
        f = web_input.data
        cmd = web_input.cmd

        if not f:
            return 'data not given'
        if not cmd:
            return 'cmd not given'

        conf_name = os.path.join(path, '.deployd.conf')
        if not os.access(conf_name, os.F_OK):
            return '.deployd.conf not found'

        try:
            http_token = web.ctx.env.get('HTTP_TOKEN')
            for line in open(conf_name):
                if not line.strip() or line.startswith('#'): continue
                ip, token = line.split()
                if ip == web.ctx.ip and token == http_token:
                    break
            else:
                return 'access denied'
        except Exception as e:
            return 'invalid .deployd.conf: ' + str(e)

        os.chdir(path)
        open(f.filename, 'wb').write(f.value)
        os.system(cmd)
        return 'ok'

    def GET(self):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        chars += chars.upper() + '0123456789'
        return ''.join([random.choice(chars) for i in range(64)])


app.add_mapping('(.+)', FileReceiver)


with daemon.DaemonContext():
    open('/var/lock/subsys/deploytool', 'w').write(str(os.getpid()))
    app.run()
