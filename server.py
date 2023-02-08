from waitress import serve
from mood_tracker.wsgi import application

if __name__ == "__main__":
    serve(application, port="8000")
