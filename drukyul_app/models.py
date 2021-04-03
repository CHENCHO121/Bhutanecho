from django.db import models
from django.utils.html import mark_safe
from embed_video.fields import EmbedVideoField


class CommonForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12)
    message = models.TextField()

    class Meta:
        abstract = True


class Contact(CommonForm):
    class Meta:
        verbose_name = "Contact Table"

    def __str__(self):
        return self.name


class Volunteer(CommonForm):
    occupation = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        verbose_name = "Volunteer Table"

    def __str__(self):
        return self.name


class CommonCommittee(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="profiles")
    introduction = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


class Director(CommonCommittee):
    class Meta:
        verbose_name = "Director Table"

    def __str__(self):
        return self.name


class Producer(CommonCommittee):
    class Meta:
        verbose_name = "Producer Table"

    def __str__(self):
        return self.name


class Adviser(CommonCommittee):
    class Meta:
        verbose_name = "Adviser Table"

    def __str__(self):
        return self.name


class CommonPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        abstract = True


class Blog_CommuniteeStory(CommonPost):
    date_published = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog CommuniteeStory Table"


class News_Update(CommonPost):
    date_published = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News_Update Table"


class Initiative(CommonPost):
    published_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Initiative Table"
        ordering = ['-published_date']


class LockdownRead(CommonPost):
    date_published = models.DateField()

    # you_tube_playlist =EmbedVideoField()
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "LockdownRead Table"


class BreathingBook(CommonPost):
    date_published = models.DateField()

    # you_tube_playlist = EmbedVideoField()
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "BreathingBook Table"


class DrukyulSalon(CommonPost):
    date_published = models.DateField()
    # you_tube_playlist = EmbedVideoField()
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "DrukyulSalon Table"


class BhutanPage(CommonPost):
    date_published = models.DateField()

    # you_tube_playlist = EmbedVideoField()
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "BhutanPage Table"



SPONSOR_CHOICES=(
    ('PP','PRINCIPAL PARTNERS'),
    ('VP','VENUE PARTNERS'),
    ('MP','MEDIA PARTNERS'),
    ('PP2','PROJECT PARTNERS'),
    ('SD','SPONSORS DIRECTORY'),
)

class Sponsor_Partner(models.Model):
    sponsor_type=models.CharField(choices=SPONSOR_CHOICES,max_length=50)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="Sponsor_Partner")
    website_link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sponsor_Partner Table"





class StoryTelling(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateField()



    # you_tube_playlist = EmbedVideoField()
    # slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "StoryTelling Table"
