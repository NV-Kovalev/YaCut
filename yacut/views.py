from . import app


@app.route('/')
def index_view():
    return 'Совсем скоро тут будет сервис укорачивающий ссылки.'