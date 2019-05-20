# -*- coding: utf-8 -*-
import time

from config.base_setting import UPLOAD, APP


class UrlManager(object):
    def __init__(self):
        pass

    # @staticmethod
    # def buildUrl( path ):
    #     return path
    #
    # @staticmethod
    # def buildStaticUrl(path):
    #     # ver = "%s"%( 22222222 )
    #     # path =  "/static" + path + "?ver=" + ver
    #     return UrlManager.buildUrl( path )

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
        # release_version = app.config.get( "release_version" )
        # ver = "%s" % ("first")
        # path = "/static" + path + "?ver=" + ver
        # return UrlManager.buildUrl(path)
        return UrlManager.buildUrl("/static" + path)

    @staticmethod
    def buildImageUrl(path):
        app_config = APP
        url = app_config['domain'] + UPLOAD['prefix_url'] + path
        return url
