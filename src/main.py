from infra.routes.apigs import createApp
from config.conf import BaseConf

application = createApp()

if __name__ == '__main__':
    if BaseConf.ENV_DEV:
        application.run(host=BaseConf.HOST, port=BaseConf.PORT_API)
    application.run()