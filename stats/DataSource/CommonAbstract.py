# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from urllib.parse import urlparse
import requests

class CommonAbstract(ABC):
    """
    Common data source function
    """

    def __init__(self,url=None):
        self._set_url(url)

    def _set_url(self,url):
        urlObj = urlparse(url)
        # print(f"url : {urlObj}")
        if urlObj.scheme == None or urlObj.hostname == None :
            raise ValueError(f"not valid url : {url}")
        self._url = urlObj

    def _get_url(self):
        return self._url.geturl()

    url = property(_get_url,_set_url)

    def download(self):
        if not self.url :
            raise ValueError("No url provided")
        import requests
        response = requests.get(self.url, allow_redirects=True)
        if response.status_code == 200:
            return response.text, response.headers['content-type']
        else:
            raise IOError(response.status_code)

    @abstractmethod
    def parse(self,data):
        raise NotImplementedError("Is abstract method")