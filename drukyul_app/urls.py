from django.urls import path,include

from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('initiatives/',views.initiative,name='initiatives'),
    path('initiatives_detail/<int:pk>', views.initiative_detail, name='initiatives_detail'),
    path('sponsors/',views.sponsor,name='sponsors'),
    path('royal-patron/',views.royal_patron,name='royal-patron'),
    path('our-story/',views.our_story,name='our-story'),
    path('festival-committee/',views.festival_committee,name='festival-committee'),
    path('bhutan/',views.bhutan,name='bhutan'),
    path('breathing_book/',views.breathing_book,name='breathing_book'),
    path('community_story',views.community_story,name='community_story'),
    path('community_story_detail/<int:pk>', views.community_story_detail, name='community_story_detail'),
    path('contact/',views.contact,name='contact'),
    path('digital_saloon/',views.digital_saloon,name='digital_saloon'),
    path('digital_saloon_detail/<int:pk>',views.digital_saloon_detail,name='digital_saloon_detail'),
    path('literature_arts/',views.literature_arts,name='literature_arts'),
    path('lockdown_read/',views.lockdown_read,name='lockdown_read'),
    path('lockdown_read_detail/<int:pk>', views.lockdown_read_detail, name='lockdown_read_detail'),
    path('news_update/',views.news_update,name='news_update'),
    path('news_update_detail/<int:pk>',views.news_update_detail,name='news_update_detail'),
    path('story_telling/',views.story_telling,name='story_telling'),
    path('volunteer/',views.volunteer,name='volunteer'),
    

]