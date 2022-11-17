from django.test import TestCase
from DataSource.DataGouvFr import DataGouvFr

class DataGouvFrTest(TestCase):
    def setUp(self):
        pass

# __init__(self,url=None)
    def test_init_noError(self):
        dataSource = DataGouvFr()

    def test_init_hasUrl(self):
        dataSource = DataGouvFr()
        self.assertIsNotNone(dataSource.url)

    def test_init_urlEqual(self):
        dataSource = DataGouvFr()
        self.assertEqual(dataSource.url, DataGouvFr._dataGouvUrl)

# _set_url(self,url)
    def test_setValidUrl_noError(self):
        dataSource = DataGouvFr()
        dataSource.url="https://new.domain.tld/"

    def test_setNotValidUrl_raiseException(self):
        dataSource = DataGouvFr()
        self.assertRaises(ValueError, dataSource._set_url, "not valid url")

    def test_setValidUrl_changeUrl(self):
        dataSource = DataGouvFr()
        oldUrl = dataSource.url
        dataSource.url="https://new.domain.tld/"
        self.assertNotEqual(oldUrl, dataSource.url)

# def _get_url(self):
    def test_getUrl_noError(self):
        dataSource = DataGouvFr()
        dataSource.url

    def test_getUrl_isString(self):
        dataSource = DataGouvFr()
        self.assertIsInstance(dataSource.url, str)

# download(self)
    def test_download_returnData(self):
        dataSource = DataGouvFr()
        data, contentType = dataSource.download()
        self.assertIsNotNone(data)

    def test_download_dataLen(self):
        dataSource = DataGouvFr()
        data, contentType = dataSource.download()
        length = len(data)
        self.assertGreater(length, 100)

    def test_downloadError404_raiseException(self):
        dataSource = DataGouvFr()
        dataSource.url = "https://droledevelo.fr/404"
        self.assertRaises(IOError, dataSource.download)

# parse(self,data)
    def test_parseNoneData_raiseException(self):
        dataSource = DataGouvFr()
        self.assertRaises(ValueError, dataSource.parse, None)

    def test_parseEmptyData_raiseException(self):
        dataSource = DataGouvFr()
        self.assertRaises(ValueError, dataSource.parse, "")
