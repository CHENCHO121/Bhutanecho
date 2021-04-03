from django.contrib import admin

from .models import Contact, Volunteer, Director, Producer, Adviser, Blog_CommuniteeStory, BhutanPage, BreathingBook, \
    Initiative,StoryTelling, News_Update, Sponsor_Partner, DrukyulSalon,LockdownRead

# from suit.apps import DjangoSuitConfig
#
# class SuitConfig(DjangoSuitConfig):
#     layout = 'horizontal'

admin.site.site_header = 'BHUTAN ECHOES'



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    list_filter = ['name', 'email', 'phone' ]
    search_fields = ['name', 'email', 'phone',]


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'occupation', 'address', 'message']
    list_filter = ['name','email', 'phone', 'occupation', 'address',]
    search_fields = ['name','email', 'phone', 'occupation', 'address',]


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'introduction', 'profile_img']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'introduction', 'profile_img']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Adviser)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'introduction', 'profile_img']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Initiative)
class InitiativeAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','published_date']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Blog_CommuniteeStory)
class Blog_CommuniteeStoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title', 'date_published']
    search_fields = ['title', 'date_published']

@admin.register(News_Update)
class News_UpdateAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title', 'date_published']
    search_fields = ['title', 'date_published']

@admin.register(LockdownRead)
class LockdownReadAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(BreathingBook)
class BreathingBookAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(DrukyulSalon)
class DrukyulSalonAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title']
    search_fields = ['title']

@admin.register(BhutanPage)
class BhutanPageAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','image','date_published']
    list_filter = ['title']
    search_fields = ['title']




@admin.register(Sponsor_Partner)
class Sponsor_PartnerAdmin(admin.ModelAdmin):
    list_display = ['id','sponsor_type','name','image','website_link']
    list_filter = ['name','sponsor_type']
    search_fields = ['name', 'website_link','sponsor_type']


@admin.register(StoryTelling)
class StoryTellingAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','date_published']
    list_filter = ['title']
    search_fields = ['title']


