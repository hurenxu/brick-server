'''
genie.management.commands.genie_data_migrate
--------------------------------------------

command to migrate genie data

@copyright:(c) 2013 SynergyLabs
@license:UCSD License. See License file for details.
'''
from django.core.management.base import BaseCommand
from userservice.utils.bd import sensor_service
from building_depot.sensor_service import DataPoint
from core.models import Campus, Building
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, **options):
        self.init_building()
        print("building inited")

    def init_building(self):
        campus = Campus.objects.filter(name='Main').first()
        if campus is None:
            campus = Campus(name='Main', institution='UCSD')
            campus.save()
        self.campus = campus
        building = Building.objects.filter(name='EBU3B').first()
        if building is None:
            building = Building(name='EBU3B', campus=campus)
            building.save()
        self.building = building
