'''
core.models
---------------

models of core information

@copyright:(c) 2013 SynergyLabs
@license:UCSD License. See License file for details.
'''
from django.db import models
from userservice.settings import BD_SETTINGS
import logging
logger = logging.getLogger(__name__)

class Campus(models.Model):

    class Meta:
        permissions = (
            ("manage_campus", "Can manage a campus"),
        )

    name = models.CharField(max_length=64, unique=True)
    institution = models.CharField(max_length=64)

    def __str__(self):
        return "Institution: %s - Campus: %s" % (self.institution, self.name)


class Building(models.Model):

    class Meta:
        permissions = (
            ("manage_building", "Can manage a building"),
        )

    name = models.CharField(max_length=64, unique=True)
    campus = models.ForeignKey(Campus, related_name="buildings_set")

    def __str__(self):
        return "Building: %s " % self.name
