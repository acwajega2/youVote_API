# Generated by Django 3.0.2 on 2020-02-01 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('profile_pic', models.CharField(max_length=400)),
                ('vote_count', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Election_Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_name', models.CharField(max_length=150)),
                ('election_status', models.CharField(choices=[('Y', 'Yesy'), ('N', 'No')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voting_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('Y', 'Yesy'), ('N', 'No')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uVote.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election_race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uVote.Election_Race'),
        ),
    ]