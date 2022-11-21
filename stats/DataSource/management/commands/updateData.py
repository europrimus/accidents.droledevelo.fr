# -*- coding: utf-8 -*-

import sys
from django.core.management.base import BaseCommand, CommandError
from importlib import import_module

class Command(BaseCommand):
    help = 'Update data from specified source'
    missing_args_message = """
    Missing argument sourceName.
    For the list of avaible sources, run :
        ./manage.py updateData sourcesList
    """
    _dataSources={
        'data.gouv.fr':'DataGouvFr',
    }

    def add_arguments(self, parser):
        parser.add_argument('sourceName', nargs=1, type=str)

    def handle(self, *args, **options):
        self._options = options
        if "sourcesList" == options['sourceName'][0]:
            self.sourcesList()
            return
        self.updateData(options['sourceName'][0])


    def updateData(self,source):
        if source not in set(self._dataSources.keys()):
            self.stderr.write("Unknow data source")
            return
        dataSource = self.getDataSource(source)
        print(f"dataSource : {dataSource}")
        self.updateUrlList(dataSource)

    def updateUrlList(self,dataSource):
        if None == dataSource:
            raise ValueError("Need a data source object")
        self.stdout.write("update data")
        data, mimeType = dataSource.download()
        insertedLine = dataSource.parse(data,mimeType)
        self.stdout.write(f"inserted line: {insertedLine}")

    def getDataSource(self,source):
        moduleName = self._dataSources[source]
        try :
            module = import_module(f"DataSource.{moduleName}")
            DataSource = getattr(module, moduleName)
            return DataSource()
        except Exception as e:
            self.stderr.write("Error when importing data source")
            raise e


    def sourcesList(self):
        """
        Print the list of avaible data source.
        """
        self.stdout.write("Data source availble:")
        for dataSource in set(self._dataSources.keys()):
            self.stdout.write(f"  {dataSource}")

