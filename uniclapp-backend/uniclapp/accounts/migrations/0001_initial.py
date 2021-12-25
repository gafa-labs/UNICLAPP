# Generated by Django 4.0 on 2021-12-25 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('full_name', models.CharField(max_length=60)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_club_advisor', models.BooleanField(default=False)),
                ('is_board_member', models.BooleanField(default=False)),
                ('is_board_chairman', models.BooleanField(default=False)),
                ('is_oem', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BoardChairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ClubAdvisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.TextField(choices=[('ACC', 'Acc'), ('ADA', 'Ada'), ('AMER', 'Amer'), ('ARCH', 'Arch'), ('BF', 'Bf'), ('BTE', 'Bte'), ('CHEM', 'Chem'), ('CI', 'Ci'), ('CINT', 'Cint'), ('COMD', 'Comd'), ('CS', 'Cs'), ('CTE', 'Cte'), ('CTIS', 'Ctis'), ('ECON', 'Econ'), ('EDEB', 'Edeb'), ('EEE', 'Eee'), ('EEPS', 'Eeps'), ('ELIT', 'Elit'), ('ELS', 'Els'), ('EMBA', 'Emba'), ('ENG', 'Eng'), ('ETE', 'Ete'), ('FA', 'Fa'), ('FRP', 'Frp'), ('GE', 'Ge'), ('GRA', 'Gra'), ('HART', 'Hart'), ('HCIV', 'Hciv'), ('HIST', 'Hist'), ('HUM', 'Hum'), ('IAED', 'Iaed'), ('IE', 'Ie'), ('IR', 'Ir'), ('LAUD', 'Laud'), ('LAW', 'Law'), ('LNG', 'Lng'), ('MAN', 'Man'), ('MATH', 'Math'), ('MBA', 'Mba'), ('MBG', 'Mbg'), ('ME', 'Me'), ('MIAPP', 'Miapp'), ('MSC', 'Msc'), ('MSN', 'Msn'), ('MTE', 'Mte'), ('MUS', 'Mus'), ('NSC', 'Nsc'), ('PE', 'Pe'), ('PHIL', 'Phil'), ('PHYS', 'Phys'), ('POLS', 'Pols'), ('PREP', 'Prep'), ('PSYC', 'Psyc'), ('SFL', 'Sfl'), ('SOC', 'Soc'), ('TE', 'Te'), ('TEFL', 'Tefl'), ('THEA', 'Thea'), ('THM', 'Thm'), ('THR', 'Thr'), ('TRIN', 'Trin'), ('TURK', 'Turk')])),
                ('student_id', models.CharField(max_length=8, unique=True)),
                ('hes_code', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('ge_point', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='accounts.user')),
            ],
        ),
        migrations.CreateModel(
            name='PSIScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='psi', to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='OEM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oem', to='accounts.user')),
            ],
        ),
    ]
