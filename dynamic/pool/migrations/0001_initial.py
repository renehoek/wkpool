# Generated by Django 3.2.12 on 2022-10-27 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plays_at', models.DateTimeField()),
                ('stadion', models.CharField(choices=[('AL_BAYT', 'Al Bayt'), ('KHALIFA_INT', 'Khalifa Int'), ('AHMAD_BIN_ALI', 'Ahmad Bin Ali'), ('AL_THUMAMA', 'Al Thumama')], max_length=255)),
                ('team_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='match_team_1', to='pool.team')),
                ('team_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='match_team_2', to='pool.team')),
            ],
            options={
                'verbose_name': 'The match',
                'verbose_name_plural': 'The matches',
            },
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('person_name', models.CharField(max_length=255)),
                ('team_1_points', models.PositiveIntegerField()),
                ('team_2_points', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=0, max_digits=3)),
                ('the_match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pool.match')),
            ],
            options={
                'verbose_name': 'Bet',
            },
        ),
    ]
