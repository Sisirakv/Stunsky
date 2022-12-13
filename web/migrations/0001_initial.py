# Generated by Django 4.1.3 on 2022-12-10 10:46

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/blog/', verbose_name='Image')),
                ('heading', models.TextField()),
                ('short_heading', models.TextField(max_length=50)),
                ('category', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryDigitalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Category Digital Media',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/Client/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('project_goals', models.TextField()),
                ('phone', models.CharField(max_length=12)),
                ('budeget', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DataProcessingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/imagedataservice/', verbose_name='Image')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ImgageDataService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/imagedataservice/', verbose_name='Image')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.CharField(blank=True, max_length=50, null=True)),
                ('vaccancy', models.IntegerField(blank=True, null=True)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('job_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('job_responsibility', tinymce.models.HTMLField(blank=True, null=True)),
                ('educational_requirments', tinymce.models.HTMLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/team/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/testimagemodel/', verbose_name='Image')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/portfolio/', verbose_name='Image')),
                ('title', models.TextField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='DesignDigitalMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/digitalmedia/', verbose_name='Image')),
                ('media_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.categorydigitalmedia')),
            ],
            options={
                'verbose_name_plural': 'Digital Media',
            },
        ),
        migrations.CreateModel(
            name='ApplyNow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.jobdetails')),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
    ]