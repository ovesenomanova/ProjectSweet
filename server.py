from waitress import serve
from _sweetsaratov_.wsgi import application


if __name__ == '__main__':
    serve(application, port='8000')

