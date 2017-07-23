#-*- coding: utf-8 -*-

from backend.common.file_utils import FileUtils

class WebContentStorage():
    def __init__(self):
        self.file_utils = FileUtils()
        self.base_path = './stockbaby/backend/data/'

    def set(self, key, url):
        filepath = self.__build_filepath(key)
        self.file_utils.copy_url_to_file(url, filepath)

    def contains(self, key):
        filepath = self.__build_filepath(key)
        return self.file_utils.is_file(filepath)
        
    def get(self, key):
        filepath = self.__build_filepath(key)
        return self.file_utils.read_file(filepath)

    def __build_filepath(self, key):
        relative_path = '''{key}.html'''.format(key=key)
        return self.file_utils.join_paths(self.base_path, relative_path)

