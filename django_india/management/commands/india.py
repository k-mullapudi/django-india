"""
Script for importing data from GeoNames.

BASE-URL: http://download.geonames.org/export/dump/

Refer http://www.geonames.org/export/codes.html for more complete information
on GeoName feature codes.

"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass

    def download(self, key):
        """
        Method for downloading file for key passed as a parameter.
        :param key: for which file is to be downloaded.
        :return:
        """
        pass

    def load_data_from_file(self, key):
        """
        Loading data for key from relevant file.
        :param key: for which file is to be loaded.
        :return:
        """
        pass

    def import_states(self):
        """
        Method for returning first-order administrative divisions, i.e., Indian states (Telangana, Gujarat etc.)
        [ADM1] GeoName feature codes.
        :return:
        """
        self.download('states')

    def import_regions(self):
        """
        Method for returning second-order, third-order and fourth-order administrative divisions, i.e., districts,
        constituencies of states etc.
        [ADM2, ADM3, ADM4] GeoName feature codes.
        :return:
        """
        self.download('regions')

    def import_cities(self):
        """
        Method for returning populated places, i.e., cities, towns and villages.
        [PPL, PPLC, PPLA, PPLA2, PPLA3, PPLA4, PPLL, PPLS] GeoName feature codes.
        * PPL - a city, town, village, or other agglomeration of buildings where people live and work
        * PPLA - seat of a first-order administrative division (PPLC takes precedence over PPLA)
        * PPLC - capital of a political entity
        * PPLS - cities, towns, villages, or other agglomerations of buildings where people live and work
        :return:
        """
        self.download('cities')
