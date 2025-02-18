# Generated by Django 4.0.5 on 2022-08-01 18:53

from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=100)),
                ('Student_id', models.CharField(max_length=100)),
                ('Sponsor_email', models.EmailField(max_length=100, unique=True)),
                ('Sponsor_No', models.CharField(default=234, max_length=15)),
                ('Sponsor_location', models.CharField(max_length=255)),
                ('Full_name', models.CharField(max_length=255)),
                ('Debt', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Body', models.TextField(help_text='Enter help here')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Local_Government', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('School_owner', models.CharField(max_length=255)),
                ('School_name', models.CharField(max_length=255)),
                ('school_id', shortuuid.django_fields.ShortUUIDField(alphabet='123456efghij', length=5, max_length=7, prefix='DebPay', primary_key=True, serialize=False)),
                ('Reg_number', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.locality')),
                ('debtor', models.ManyToManyField(blank=True, to='Debtor.debtor')),
            ],
        ),
        migrations.CreateModel(
            name='School_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pics', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Debtor.school')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Body', models.TextField(help_text='Enter post here...')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_pics')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deptors_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.debtor')),
                ('school_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.school')),
            ],
        ),
        migrations.CreateModel(
            name='Deptors_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pics', models.ImageField(default='default.png', upload_to='debt_profile_pics')),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.debtor')),
            ],
        ),
        migrations.AddField(
            model_name='debtor',
            name='Student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.level'),
        ),
        migrations.CreateModel(
            name='Contend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=100)),
                ('Student_id', models.CharField(max_length=50)),
                ('How_to_be_contacted', models.CharField(help_text='specify email or phone number', max_length=255)),
                ('Complain', models.TextField(help_text='Enter your complain here...')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.school')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Body', models.TextField(help_text='Enter your comments here...')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Debtor.post')),
            ],
        ),
    ]
