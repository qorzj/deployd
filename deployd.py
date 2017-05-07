import daemon
import web
import os

app = web.application()

class FileReceiver:
    def POST(self):
        web_input = web.input(data={})
        f = web_input.data
        os.chdir('/mnt/grus_product')
        open('bin/' + f.filename, 'wb').write(f.value)
        os.system('docker-compose stop')
        #os.system('docker-compose up -d')
        return 'done.'

    def GET(self):
        return 'working'


app.add_mapping('/', FileReceiver)


with daemon.DaemonContext():
    open('/var/lock/subsys/deploytool', 'w').write(str(os.getpid()))
    app.run()
