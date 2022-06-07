import logging

from flask import Blueprint, request, render_template, current_app

from classes.data_manager import DataManager
from classes.exceptions import DataSourceBrokenException

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logger = logging.getLogger("logger")


@main_blueprint.route('/')  # главная страница
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')  # страница поиска
def search_page():
    path = current_app.config.get('POST_PATH')
    data_manager = DataManager(path)

    # получаем данные
    s = request.values.get('s', None)
    posts = data_manager.search(s)

    # записываем лог поиска
    logger.info(f"Выполняется поиск: {s}")

    return render_template('post_list.html', posts=posts, s=s)


@main_blueprint.errorhandler(DataSourceBrokenException)  # Ошибка чтения файла json
def error_read_data(e):
    logger.error(e)  # Записываем ошибку в лог
    return "Ошибка данных на сервере, обратитесь к администратору"
