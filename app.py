from flask import Flask
from Course import create_course_app
from Users import create_user_app
from UI import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

ui = create_app()
course = create_course_app()
user = create_user_app

application = Flask(__name__)
application.wsgi_app = DispatcherMiddleware(
    ui, {'/apicourses': course, '/apiusers': user}
)

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5000)