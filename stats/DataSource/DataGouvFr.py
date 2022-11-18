# -*- coding: utf-8 -*-

from DataSource import CommonAbstract
from DataSource.models import URL
from datetime import datetime
from django.utils.timezone import make_aware

class DataGouvFr(CommonAbstract) :
    """
    Read and parse data from data.gouv.fr
    """
    _dataGouvUrl = "https://www.data.gouv.fr/api/2/datasets/53698f4ca3a729239d2036df/resources/?page=1&type=main&page_size=100"

    def __init__(self):
        super().__init__(self._dataGouvUrl)

    def parse(self,data,contentType=None):
        if data == None or data == "":
            raise ValueError()
        if contentType == "text/csv" :
            return self.parseCsv(data)
        elif contentType == "application/json" :
            return self.parseJson(data)
        else :
            print(data[:20])
            return data

    def parseCsv(self,data):
        import csv
        parsedData = csv.reader(data, delimiter=';', quotechar='"')
        return parsedData

    def parseJson(self,data):
        import json
        insertedLines = 0
        jsonData = json.JSONDecoder().decode(data)["data"]
        for link in jsonData:
            try:
                urls = URL.objects.filter(uid=link['id'])
                if len(urls) == 0 :
                    # if the entry exist : using it
                    url = URL(uid = link['id'])
                else :
                    # if the entry not exist : create a new one
                    url = urls[0]
                del urls
                # update or set value
                url.title = link['title']
                url.description = link['description']
                url.url = link['latest']
                url.checksum_type = None if link['checksum'] is None else link['checksum']['type']
                url.checksum_value = None if link['checksum'] is None else link['checksum']['value']
                url.filesize = link['filesize']
                url.mime_type = link['mime']
                url.created_at = make_aware(__class__.parseDate(link['created_at']))
                url.published_at = make_aware(__class__.parseDate(link['published']))
                url.last_modified_at = make_aware(__class__.parseDate(link['last_modified']))

                url.save()
                insertedLines += 1
            except Exception as e:
                print(
                    f"""{20*'-'} EXCEPTION {20*'-'}
{e}
link: {link}
{50*'-'}
"""
)
        return insertedLines

    @staticmethod
    def parseDate(str) -> datetime:
        # 2015-08-07T18:46:44.834000
        # 2015-08-07T18:46:44
        format = '%Y-%m-%dT%H:%M:%S'
        if '.' in str :
            format += '.%f'
        return datetime.strptime(str,format)