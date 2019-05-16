# -*- coding: utf-8 -*-
import  time


from config.base_setting import UPLOAD, APP


class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s"%( 22222222 )
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildImageUrl(path):
        app_config = APP
        url = app_config['domain'] + UPLOAD['prefix_url'] + path
        return url


