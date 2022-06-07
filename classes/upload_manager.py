import os
import random

from classes.exceptions import PictureFormatNotSupportedError, PictureNotUploadedError, \
    OutOfFreeNamesError


class UploadManager:
    """ Класс обработки загружаемого файла """

    def get_free_file_name(self, folder, file_type):
        """ Метод генерации имени для загружаемого файла """
        attemps = 0
        LIMIT_OF_ATTEMPS = 10000

        while True:
            pic_name = str(random.randint(0, 10000))
            filename_to_save = f"{pic_name}.{file_type}"
            os_path = os.path.join(folder, filename_to_save)
            is_filename_occupied = os.path.exists(os_path)
            if not is_filename_occupied:
                return filename_to_save
            attemps += 1
            if attemps > LIMIT_OF_ATTEMPS:
                raise OutOfFreeNamesError("Нет свободных имён для сохранения")

    def file_type_valid(self, file_type):
        """ Метод проверки поддерживаемого файла """
        if file_type.lower() in {"png", "jpg", "jpeg"}:
            return True
        return False

    def save_with_random_name(self, picture):
        """ Метод создания имени загружаемого файла """
        filename = picture.filename
        type_file = filename.lower().split(".")[-1]
        if not self.file_type_valid(type_file):
            raise PictureFormatNotSupportedError(f"Формат {type_file} не поддерживается")
        folder = os.path.join(".", "uploads", "images")
        filename_to_save = self.get_free_file_name(folder, type_file)
        try:
            picture.save(os.path.join(folder, filename_to_save))
        except FileNotFoundError:
            raise PictureNotUploadedError(f"{folder, filename_to_save}")
        return filename_to_save
