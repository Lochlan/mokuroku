from django.contrib import admin

from products.models import Group
from products.models import GroupMembership
from products.models import Image
from products.models import BaseObject
from products.models import Product
from products.models import TurbografxCanadianCdRom2
from products.models import TurbografxCanadianHucard
from products.models import TurbografxCanadianSuperCdRom2
from products.models import TurbografxCdRom2
from products.models import TurbografxHucard
from products.models import TurbografxSuperCdRom2
from products.models import Component

admin.site.register(Group)
admin.site.register(GroupMembership)

admin.site.register(Image)

admin.site.register(Component)

admin.site.register(TurbografxCanadianCdRom2)
admin.site.register(TurbografxCanadianHucard)
admin.site.register(TurbografxCanadianSuperCdRom2)
admin.site.register(TurbografxCdRom2)
admin.site.register(TurbografxHucard)
admin.site.register(TurbografxSuperCdRom2)
