import logging
from flask import Flask, send_from_directory

from main.views import main_blueprint
from upload.views import upload_blueprint
import loggers

app = Flask(__name__)

app.register_blueprint(main_blueprint)  # регистрация блупринта main
app.register_blueprint(upload_blueprint)  # регистрация блупринта upload

# Записываем конфигурации в app
app.config['POST_PATH'] = "data/posts.json"
app.config['UPLOAD_FOLDER'] = "uploads/images"

# Создаём логгер
loggers.create_logger()
logger = logging.getLogger("logger")


@app.route("/uploads/<path:path>/")  # Роут для пути загрузки файла
def static_dir(path):
    return send_from_directory("uploads", path)


logger.info("Приложение запускается")
if __name__ == "__main__":
    app.run(debug=True)
