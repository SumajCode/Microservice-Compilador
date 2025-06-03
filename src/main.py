from infra.routes.apigs import createApp

application = createApp()

if __name__ == '__main__':
    application.run()