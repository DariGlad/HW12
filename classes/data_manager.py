import json

from classes.exceptions import DataSourceBrokenException


class DataManager:
    """ Клосс для работы с данными"""

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """
        Возвращает данные json (список словарей)

        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise DataSourceBrokenException("Файл с данными повреждён")
        return data

    def save_data(self, data):
        """
        Перезаписывает данные в файле json

        """
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    # def get_all(self):
    #     """
    #     Отдаёт полный список данных
    #
    #     """
    #     return self.load_data()

    def search(self, substring):
        """
        Отдает посты(список словарей), которые содержат substring

        """
        posts = self.load_data()
        search_posts = [post for post in posts if substring.lower() in post['content'].lower()]
        return search_posts

    def add(self, post):
        """
        Добавляем в хранилище постов созданный пост

        """
        if type(post) != dict:
            raise TypeError('Требуется словарь для сохранения поста')
        posts = self.load_data()
        posts.append(post)
        self.save_data(posts)

# dm = DataManager('../data/posts.json')
# post = {"pic" : '...', "content" : '...'}
# print(dm.add(post))
