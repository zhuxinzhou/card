# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
import time
from config.base_setting import APP, UPLOAD


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        """
        构建静态文件的获取地址
        :param path:
        :return:
        """
        return UrlManager.buildUrl("/static" + path)

    @staticmethod
    def buildImageUrl(path):
        config2 = UPLOAD
        config1 = APP
        url = config1['domain'] + config2['prefix_url'] + path
        return url
