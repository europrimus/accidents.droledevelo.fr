# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from urllib.parse import urlparse
import os
import requests

class CommonAbstract(ABC):
    """
    Common data source function
    """
    _downloadPath="download"

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
            # save data to file
            os.makedirs(self._downloadPath, exist_ok=True)
            print(f"url : {self.url}")
            fileName = self.getFileNameFromUrl(self.url,response.headers['content-type'])
            filePath = f"{self._downloadPath}/{fileName}"
            print(f"filePath : {filePath}")
            with open(filePath, 'wb') as fd:
                for chunk in response.iter_content(chunk_size=128):
                    fd.write(chunk)
            return response.text, response.headers['content-type']
        else:
            raise IOError(response.status_code)

    @abstractmethod
    def parse(self,data):
        raise NotImplementedError("Is abstract method")

    @staticmethod
    def getFileNameFromUrl(url,contentType) :
        ext = contentType.split("/")[1]
        path = urlparse(url).path
        pathParts = path.split("/")
        fileName = ""
        if "." in path:
            fileName = pathParts[-1]
        else:
            for part in pathParts:
                if len(part) > len(fileName):
                    fileName = part
        return f"{fileName}.{ext}"
