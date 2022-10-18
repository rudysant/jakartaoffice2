from email.policy import default
from random import choices

from django.db import models

class Catalogues(models.Model):
    entry_date = models.DateField()
    consignment_no = models.IntegerField(default=461)
    title = models.TextField()

    work_type = models.CharField(max_length=20, choices=[
        ('Original','Original'),
        ('Translation','Translation'),
        ('Adaptation','Adaptation')
        ], default='Original')

    publish_year = models.IntegerField()

    volume = models.CharField(max_length=20, choices=[
        ('Single','Single'),
        ('Multi-complete','Multi-complete'),
        ('Multi-incomplete','Multi-incomplete'),
        ], default='Single')

    copycat = models.CharField(max_length=20, choices=[
        ('No','No'),
        ('Partial copycat','Partial copycat'),
        ('Full copycat','Full copycat'),
        ], default='No')

    ISBN = models.CharField(max_length=20, choices=[
        ('No','No'),
        ('Yes-valid','Yes-valid'),
        ('Yes-invalid','Yes-invalid'),
        ], default='No')

    authorship_type = models.CharField(max_length=50, choices=[
        ('Single author','Single author'),
        ('Collaboration','Collaboration'),
        ('Compilation','Compilation'),
        ('Others','Others')
        ], default='Single')

    language = models.CharField(max_length=50, choices=[
        ('Indonesian','Indonesian'),
        ('English','English'),
        ('Indonesian local','Indonesian local'),
        ('Multi language','Multi language'),
        ('Unknown','Unknown')
        ], default='Indonesian')

    bibliography = models.CharField(max_length=20, choices=[
        ('No','No'),
        ('Yes','Yes'),
        ], default='No')

    indexx = models.CharField(max_length=20, choices=[
        ('No','No'),
        ('Yes','Yes'),
        ], default='No')

    publisher_type = models.CharField(max_length=100, choices=[
        ('Commercial','Commercial'),
        ('Government-department','Government-department'),
        ('Government-nondepartment','Government-nondepartment'),
        ('Government-local','Government-local'),
        ('Universities','Universities'),
        ('NGO','NGO'),
        ('Others','Others')
        ], default='Commercial')

    genre = models.CharField(max_length=100, choices=[
        ('General non fiction','General non fiction'),
        ('Fiction-novel','Fiction-novel'),
        ('Fiction-short stories','Fiction-short stories'),
	    ('Fiction-biographic','Fiction-biographic'),
        ('Poetry','Poetry'),
        ('Folktales','Folktales'),
        ('Biography-single','Biography-single'),
        ('Biography-collective','Biography-collective'),
        ('Biography-auto','Biography-auto'),
        ('Dictionaries','Dictionaries'),
        ('Proceeding','Proceeding'),
        ], default='General non fiction')

    format = models.CharField(max_length=100, choices=[
        ('Book-printed','Book-printed'),
        ('Book-electronic','Book-electronic'),
        ('Non book video','Non book video'),
        ('Non book audio','Non book audio'),
        ('Map-single','Map-single'),
        ('Map-atlas','Map-atlas'),
        ('Ephemera','Ephemera')
        ], default='Book')

    size = models.CharField(max_length=10, choices=[
        ('YY','YY'),
        ('YYq', 'YYq'),
        ('YYp','YYp')
        ],default='YY')

    subject = models.CharField(max_length=50, choices=[
       ('000-Generalities','100-Generalities'),
       ('000-Library science','100-Library science'),
       ('000-Journalism and media','100-Journalism and media'),
       ('100-Philosophy and ethics','100-Philosophy and ethics'),
       ('200-Religions-general','200-Religions-general'),
       ('200-Religion-Islam','200-Religion-Islam'),
       ('200-Religion-Christianity','200-Religion-Christianity'),
       ('200-Religion-Hinduism','200-Religion-Hinduism'),
       ('200-Religion-Buddhism and others','200-Religion-Buddhism and others'),
       ('300-Social-anthropology and sociology','300-Social-anthropology and sociology'),
       ('300-Social-problems and services','300-Social-problems and services'),
       ('300-Social-politics','300-Social-politics'),
       ('300-Social-economics-general','300-Social-economics-general'),
       ('300-Social-economics-resources','300-Social-economics-resources'),
       ('300-Social-economics-policy and development','300-Social-economics-policy and development'),
       ('300-Social-economics-financial and monetary','300-Social-economics-financial and monetary'),
       ('300-Social-economics-industries and production','300-Social-economics-industries and production'),
       ('300-Social-macroeconomics','300-Social-macroeconomics'),
       ('300-Social-culture','300-Social-culture'),
       ('300-Social-military','300-Social-military'),
       ('300-Social-education','300-Social-education'),
       ('300-Social-law','300-Social-law'),
       ('300-Social-public administration','300-Social-public administration'),
       ('300-Social-human rights','300-Social-human rights'),
       ('400-Language-linguistics','400-Language-linguistics'),
       ('400-Language-sociolinguistics','400-Language-sociolinguistics'),
       ('500-Science-general','500-Science-general'),
       ('600-Technology-general','600-Technology-general'),
       ('600-Agriculture and agribusiness','600-Agriculture and agribusiness'),
       ('700-Arts-general','700-Arts-general'),
       ('700-Arts-visual','700-Arts-visual'),
       ('700-Arts-performance','700-Arts-performance'),
       ('700-Arts-music','700-Arts-music'),
       ('800-Literature-general','800-Literature-general'),
       ('800-Literature-fiction and poetry','800-Literature-fiction and poetry'),
       ('900-History-world','900-History-world'),
       ('900-History-Indonesia','900-History-Indonesia'),
       ('900-Geography and travel','900-Geography and travel'),
       ('900-Biography','900-Biography')
       ], null=True)


class Book_source(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=[
        ('Regular supplier','Regular supplier'),
        ('Book store','Book store'),
        ('Field trip','Field trip'),
        ('Gift/Exchange','Gift/Exchange')
    ],)

    def __str__(self):
        return self.name

class Consignment(models.Model):
    consign_no = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, default='In process')
    box_count = models.IntegerField(default=0)
    total_weight = models.IntegerField(default=0)
    shipment_date = models.DateField(blank=True, null=True)

class Acquisition2(models.Model):
    entry_date = models.DateField()
    cons_no = models.IntegerField(default=461)
    titles_proc = models.IntegerField()
    vendor = models.ForeignKey(Book_source, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)

class Trip_place(models.Model):
    place_name = models.CharField(max_length=100)
    place_category = models.CharField(max_length=100, choices=[
        ('Government office','Government Office'),
        ('NGO office','NGO Office'),
        ('Book store','Book store'),
        ('Book fair','Book fair'),
        ('Personal','Personal')
        ],)
    address = models.CharField(max_length=200)

class FieldTrip(models.Model):
    plan_date = models.DateField()
    place = models.ForeignKey(Trip_place, on_delete=models.CASCADE)
    visit_date = models.DateField(blank=True, null=True)
    titles_acq = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[
        ('Scheduled','Scheduled'),
        ('Completed','Completed'),
        ('Postponed','Postponed'),
        ('Canceled','Canceled')
    ], default='Scheduled')





