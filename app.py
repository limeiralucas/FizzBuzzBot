from fizzbuzz_core import create_app, celery, init_celery

if __name__ == '__main__':
    app = create_app()
    init_celery(app, celery)
    app.run(host='0.0.0.0')
