# Generated by Django 4.0.6 on 2022-10-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlajkt_cat_stat', '0002_acquisition_alter_catalogues_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogues',
            name='subject',
            field=models.CharField(choices=[('000-Generalities', '100-Generalities'), ('000-Library science', '100-Library science'), ('000-Journalism and media', '100-Journalism and media'), ('100-Philosophy and ethics', '100-Philosophy and ethics'), ('200-Religions-general', '200-Religions-general'), ('200-Religion-Islam', '200-Religion-Islam'), ('200-Religion-Christianity', '200-Religion-Christianity'), ('200-Religion-Hinduism', '200-Religion-Hinduism'), ('200-Religion-Buddhism and others', '200-Religion-Buddhism and others'), ('300-Social-anthropology and sociology', '300-Social-anthropology and sociology'), ('300-Social-problems and services', '300-Social-problems and services'), ('300-Social-politics', '300-Social-politics'), ('300-Social-economics', '300-Social-economics'), ('300-Social-economics-policy and development', '300-Social-economics-policy and development'), ('300-Social-economics-financial and monetary', '300-Social-economics-financial and monetary'), ('300-Social-economics-industries and production', '300-Social-economics-industries and production'), ('300-Social-macroeconomics', '300-Social-macroeconomics'), ('300-Social-culture', '300-Social-culture'), ('300-Social-military', '300-Social-military'), ('300-Social-education', '300-Social-education'), ('300-Social-law', '300-Social-law'), ('300-Social-public administration', '300-Social-public administration'), ('300-Social-human rights', '300-Social-human rights'), ('400-Language-linguistics', '400-Language-linguistics'), ('400-Language-sociolinguistics', '400-Language-sociolinguistics'), ('500-Science-general', '500-Science-general'), ('600-Technology-general', '600-Technology-general'), ('600-Agriculture and agribusiness', '600-Agriculture and agribusiness'), ('700-Arts-general', '700-Arts-general'), ('700-Arts-visual', '700-Arts-visual'), ('700-Arts-performance', '700-Arts-performance'), ('700-Arts-music', '700-Arts-music'), ('800-Literature-general', '800-Literature-general'), ('800-Literature-fiction and poetry', '800-Literature-fiction and poetry'), ('900-History-world', '900-History-world'), ('900-History-Indonesia', '900-History-Indonesia'), ('900-Geography and travel', '900-Geography and travel'), ('900-Biography', '900-Biography')], max_length=50, null=True),
        ),
    ]