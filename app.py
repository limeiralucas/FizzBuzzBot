from fizzbuzz_core import create_app

config = {
    'development': 'config.Development',
    'prod': 'config.Production',
}

if __name__ == '__main__':
    app = create_app(config)
    app.run(port=app.config['PORT'])
