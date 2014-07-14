import datetime
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

# TODO put into its own file
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, default=timezone.now())
    modified = models.DateTimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True

class Group(Base):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField('GroupMembership', blank=True, null=True)

    def __str__(self):
        return self.name

class GroupMembership(Base):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content_object.name

class GroupMembershipInterface(models.Model):
    groups = generic.GenericRelation(GroupMembership, blank=True, null=True)

    class Meta:
        abstract = True

# TODO put into its own file
class Image(Base, GroupMembershipInterface):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, unique=True) # TODO replace with ImageField
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BaseObject(Base, GroupMembershipInterface):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('Image', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Component(BaseObject):
    pass

class ComponentInterface(models.Model):
    components = models.ManyToManyField('Component', blank=True, null=True)

    class Meta:
        abstract = True

class Product(BaseObject):
    isbn = models.DecimalField(max_digits=13, decimal_places=0, blank=True, null=True)
    product_number = models.CharField(max_length=200, blank=True, null=True)
    date_released = models.DateField(blank=True, null=True)
    # publisher
    # author
    # locale

    class Meta:
        abstract = True

class PcEngineSoftware(Product, ComponentInterface):
    msrp = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True

class PcEngineArcadeRom2(PcEngineSoftware):
    pass

class PcEngineCdRom2(PcEngineSoftware):
    pass

class PcEngineHucard(PcEngineSoftware):
    pass

class PcEngineHucardPlus(PcEngineSoftware):
    pass

class PcEngineSuperCdRom2(PcEngineSoftware):
    pass

class PcEngineSuperHucard(PcEngineSoftware):
    pass

class TurbografxSoftware(Product, ComponentInterface):
    msrp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        abstract = True

class TurbografxCanadianCdRom2(TurbografxSoftware):
    pass

class TurbografxCanadianHucard(TurbografxSoftware):
    pass

class TurbografxCanadianSuperCdRom2(TurbografxSoftware):
    pass

class TurbografxCdRom2(TurbografxSoftware):
    pass

class TurbografxHucard(TurbografxSoftware):
    pass

class TurbografxSuperCdRom2(TurbografxSoftware):
    pass
