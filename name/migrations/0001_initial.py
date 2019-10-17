# Generated by Django 2.2.6 on 2019-10-15 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTicketing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stub', models.BooleanField(default=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Identifier_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(help_text='What kind of data is this? Personal website? Twitter?', max_length=255)),
                ('icon_path', models.CharField(blank=True, help_text='Path to icon image?', max_length=255)),
                ('homepage', models.URLField(blank=True, help_text='Homepage of label. Twitter.com, Facebook.com, etc')),
            ],
            options={
                'verbose_name': 'Identifier Type',
                'ordering': ['label'],
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please use the general reverse order: LAST, FIRST', max_length=255)),
                ('normalized_name', models.CharField(editable=False, help_text='NACO normalized form of the name', max_length=255)),
                ('name_type', models.IntegerField(choices=[(0, 'Personal'), (1, 'Organization'), (2, 'Event'), (3, 'Software'), (4, 'Building')])),
                ('begin', models.CharField(blank=True, help_text='Conforms to EDTF format YYYY-MM-DD', max_length=25)),
                ('end', models.CharField(blank=True, help_text='Conforms to EDTF format YYYY-MM-DD', max_length=25)),
                ('disambiguation', models.CharField(blank=True, help_text='Clarify to whom or what this record pertains.', max_length=255)),
                ('biography', models.TextField(blank=True, help_text='Compatible with MARKDOWN')),
                ('record_status', models.IntegerField(choices=[(0, 'Active'), (1, 'Deleted'), (2, 'Suppressed')], default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('merged_with', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merged_with_name', to='name.Name')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'name_id')},
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant_type', models.IntegerField(choices=[(0, 'Acronym'), (1, 'Abbreviation'), (2, 'Translation'), (3, 'Expansion'), (4, 'Other')], help_text='Choose variant type.')),
                ('variant', models.CharField(help_text='Fill in the other name variants, if any.', max_length=255)),
                ('normalized_variant', models.CharField(editable=False, help_text='NACO normalized variant text', max_length=255)),
                ('belong_to_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.Name')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(help_text='Enter notes about this record here')),
                ('note_type', models.IntegerField(choices=[(0, 'Biographical/Historical'), (1, 'Deletion Information'), (2, 'Nonpublic'), (3, 'Source'), (4, 'Other')])),
                ('belong_to_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.Name')),
            ],
            options={
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, help_text='\n    <strong>\n        <a target="_blank" href="http://itouchmap.com/latlong.html">\n            iTouchMap\n        </a>\n        : this service might be useful for filling in the lat/long data\n    </strong>\n    ', max_digits=13)),
                ('longitude', models.DecimalField(decimal_places=10, help_text='\n    <strong>\n        <a target="_blank" href="http://itouchmap.com/latlong.html">\n            iTouchMap\n        </a>\n        : this service might be useful for filling in the lat/long data\n    </strong>\n    ', max_digits=13)),
                ('status', models.IntegerField(choices=[(0, 'current'), (1, 'former')], default=0)),
                ('belong_to_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.Name')),
            ],
            options={
                'ordering': ['status'],
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('visible', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=0)),
                ('belong_to_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.Name')),
                ('type', models.ForeignKey(help_text="Catagorize this record's identifiers here", on_delete=django.db.models.deletion.CASCADE, to='name.Identifier_Type')),
            ],
            options={
                'ordering': ['order', 'type'],
            },
        ),
    ]
