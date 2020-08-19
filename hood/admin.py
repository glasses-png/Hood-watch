from django.contrib import admin
from .models import Post,NeighbourHood,Users,Business
# Register your models here.
admin.site.register(Post)
admin.site.register(NeighbourHood)
admin.site.register(Users)
admin.site.register(Business)
