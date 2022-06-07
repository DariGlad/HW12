import logging

from flask import Blueprint, render_template, request, current_app

from classes.data_manager import DataManager
from classes.exceptions import OutOfFreeNamesError, PictureFormatNotSupportedError, PictureNotUploadedError
from classes.upload_manager import UploadManager

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder='templates')

logger = logging.getLogger("logger")


@upload_blueprint.route("/post/")  # страница формы для создания поста
def page_post_form():
    return render_template("post_form.html")


@upload_blueprint.route("/post/", methods=["POST"])  # Страница успешного создания поста
def page_post_upload():
    path = current_app.config.get('POST_PATH')
    data_manager = DataManager(path)
    upload_manager = UploadManager()

    # Получаем данные
    pic = request.files.get("picture", None)
    content = request.values.get("content", "")

    # Сохраняем картинку с помощью менеджера загрузок
    filename_saved = upload_manager.save_with_random_name(pic)

    # Получаем путь для браузера клиента
    web_path = f"/uploads/images/{filename_saved}"

    # Создаём данные для записи в файл
    post = {"pic": web_path, "content": content}

    # Добавляем данные в файл
    data_manager.add(post)
    return render_template("post_uploaded.html", pic=web_path, content=content)


@upload_blueprint.errorhandler(OutOfFreeNamesError)  # Ошибка по превышению свободных имён
def error_out_of_free_names(e):
    logger.error(e)  # Записываем ошибку в лог
    return "Закончились имена для загрузки картинок, обратитесь в администратору сайта"


@upload_blueprint.errorhandler(PictureFormatNotSupportedError)  # Ошибка неподдерживаемого формата
def error_format_not_supported(e):
    logger.info(e)  # Записываем ошибку в лог
    return "Формат картинки не поддерживается, выберите другой"


@upload_blueprint.errorhandler(PictureNotUploadedError)  # Ошибка загрузки картинки
def error_picture_not_upload(e):
    logger.error(e)  # Записываем ошибку в лог
    return "Не удалось загрузить картинку"
