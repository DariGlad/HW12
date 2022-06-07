import logging


def create_logger():
    """ Создаём логгер """

    logger = logging.getLogger("logger")
    logger.setLevel("DEBUG")
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("logs/logger.log", encoding="utf-8")

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Добавляем формат логов
    formatter_one = logging.Formatter("%(asctime)s : %(message)s")

    console_handler.setFormatter(formatter_one)
    file_handler.setFormatter(formatter_one)
