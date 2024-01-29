# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    contactid = models.CharField(max_length=255, null=True, blank=True)
    userid = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Contact(models.Model):

    #__Contact_FIELDS__
    contactid = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Contact Names(models.Model):

    #__Contact Names_FIELDS__
    contactid = models.CharField(max_length=255, null=True, blank=True)
    nameid = models.CharField(max_length=255, null=True, blank=True)
    nametypeid = models.CharField(max_length=255, null=True, blank=True)

    #__Contact Names_FIELDS__END

    class Meta:
        verbose_name        = _("Contact Names")
        verbose_name_plural = _("Contact Names")


class Parameters(models.Model):

    #__Parameters_FIELDS__
    parameterid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    parametertypeid = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Parameters_FIELDS__END

    class Meta:
        verbose_name        = _("Parameters")
        verbose_name_plural = _("Parameters")


class Processes(models.Model):

    #__Processes_FIELDS__
    processid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Processes_FIELDS__END

    class Meta:
        verbose_name        = _("Processes")
        verbose_name_plural = _("Processes")


class Reports(models.Model):

    #__Reports_FIELDS__
    reportid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Reports_FIELDS__END

    class Meta:
        verbose_name        = _("Reports")
        verbose_name_plural = _("Reports")


class Contact Phones(models.Model):

    #__Contact Phones_FIELDS__
    contactid = models.CharField(max_length=255, null=True, blank=True)
    phonetype = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    #__Contact Phones_FIELDS__END

    class Meta:
        verbose_name        = _("Contact Phones")
        verbose_name_plural = _("Contact Phones")


class Roles(models.Model):

    #__Roles_FIELDS__
    roleid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Roles_FIELDS__END

    class Meta:
        verbose_name        = _("Roles")
        verbose_name_plural = _("Roles")


class Docs(models.Model):

    #__Docs_FIELDS__
    docid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    path = models.CharField(max_length=255, null=True, blank=True)

    #__Docs_FIELDS__END

    class Meta:
        verbose_name        = _("Docs")
        verbose_name_plural = _("Docs")



#__MODELS__END
