class DataSourceBrokenException(Exception):
    """ Ошибка при чтении файла json """
    pass


class PictureFormatNotSupportedError(Exception):
    """ Ошибка, если неподдерживаемый формат """
    pass


class OutOfFreeNamesError(Exception):
    """ Ошибка, превышен лимит имён """
    pass


class PictureNotUploadedError(Exception):
    """ Ошибка при неудачной загрузке файла """
    pass
