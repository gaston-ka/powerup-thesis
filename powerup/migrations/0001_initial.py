# Generated by Django 4.0.4 on 2022-04-30 07:31

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('nid', models.CharField(help_text='National ID', max_length=16, unique=True)),
                ('first_name', models.CharField(help_text='First Name', max_length=250)),
                ('last_name', models.CharField(help_text='Last Name', max_length=250)),
                ('phone', models.CharField(help_text='Last Name', max_length=16, unique=True)),
                ('email', models.EmailField(help_text='Email', max_length=250, unique=True)),
                ('address', models.CharField(help_text='Address', max_length=250)),
                ('dob', models.DateField(help_text='Date of Birth', max_length=250)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('NONE', 'NONE')], help_text='Gender', max_length=250)),
                ('marital_status', models.CharField(help_text='Marital Status', max_length=250)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'Client',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('phone', models.CharField(help_text='Phone number', max_length=10, unique=True)),
                ('balance', models.FloatField(default=0.0, help_text='UNIT')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date created')),
                ('client', models.ForeignKey(help_text='Client', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Pivot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('number', models.CharField(help_text='Plot Number', max_length=255)),
                ('unit', models.IntegerField(default=0, help_text='Pivot Number')),
                ('longitude', models.FloatField(default=0.0, help_text='Longitude')),
                ('latitude', models.FloatField(default=0.0, help_text='Latitude')),
            ],
            options={
                'verbose_name': 'Pivot',
                'verbose_name_plural': 'Pivots',
                'db_table': 'Pivot',
            },
        ),
        migrations.CreateModel(
            name='Suprima',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('name', models.CharField(help_text='Name', max_length=255)),
                ('tin', models.CharField(help_text='TIN Number', max_length=255)),
                ('location', models.CharField(help_text='Location', max_length=255)),
                ('unit', models.FloatField(default=0.0, help_text='UNIT')),
            ],
            options={
                'verbose_name': 'suprima',
                'verbose_name_plural': 'suprima',
                'db_table': 'suprima',
            },
        ),
        migrations.CreateModel(
            name='TopUp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('balance', models.FloatField(default=0.0, help_text='UNIT')),
                ('new_unit', models.FloatField(default=0.0, help_text='UNIT')),
                ('encr_message', models.CharField(help_text='Encrypted Message', max_length=255)),
                ('top_up_date', models.DateTimeField(auto_now_add=True, help_text='TopUP Date')),
                ('account', models.ForeignKey(help_text='Related Momo Account', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.account')),
                ('pivot_number', models.ForeignKey(help_text='Pivot Number', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.pivot')),
            ],
            options={
                'verbose_name': 'TopUp',
                'verbose_name_plural': 'TopUp',
                'db_table': 'top_up',
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('message', models.CharField(help_text='Message Code', max_length=255)),
                ('reg_tel', models.IntegerField(default=0, help_text='REG Phone number')),
                ('pivot_number', models.ForeignKey(help_text='Related Pivot', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.pivot')),
            ],
            options={
                'verbose_name': 'Emergency',
                'verbose_name_plural': 'Emergencies',
                'db_table': 'Emergency',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('message', models.CharField(help_text='Message', max_length=255)),
                ('pivot_number', models.ForeignKey(help_text='Related Pivot', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.pivot')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alert',
                'db_table': 'Alert',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='suprima',
            field=models.ForeignKey(help_text='Suprima', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.suprima'),
        ),
        migrations.CreateModel(
            name='REG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='UUID')),
                ('location', models.CharField(help_text='Location', max_length=255)),
                ('phone', models.CharField(help_text='REG Phone number', max_length=13)),
                ('client', models.ForeignKey(help_text='Related Client', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('pivot', models.ForeignKey(help_text='Related Pivot', null=True, on_delete=django.db.models.deletion.SET_NULL, to='powerup.pivot')),
            ],
            options={
                'verbose_name': 'REG',
                'verbose_name_plural': 'REG',
                'db_table': 'reg',
                'unique_together': {('client_id', 'pivot_id')},
            },
        ),
    ]
