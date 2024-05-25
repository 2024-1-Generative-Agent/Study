# Generated by Django 2.2 on 2023-03-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prolific_id', models.CharField(max_length=127)),
                ('attention_check', models.CharField(max_length=256)),
                ('q1_v1', models.IntegerField()),
                ('q1_v2', models.IntegerField()),
                ('q1_v3', models.IntegerField()),
                ('q1_v4', models.IntegerField()),
                ('q2_v1', models.IntegerField()),
                ('q2_v2', models.IntegerField()),
                ('q2_v3', models.IntegerField()),
                ('q2_v4', models.IntegerField()),
                ('q3_v1', models.IntegerField()),
                ('q3_v2', models.IntegerField()),
                ('q3_v3', models.IntegerField()),
                ('q3_v4', models.IntegerField()),
                ('q4_v1', models.IntegerField()),
                ('q4_v2', models.IntegerField()),
                ('q4_v3', models.IntegerField()),
                ('q4_v4', models.IntegerField()),
                ('q5_v1', models.IntegerField()),
                ('q5_v2', models.IntegerField()),
                ('q5_v3', models.IntegerField()),
                ('q5_v4', models.IntegerField()),
                ('rank', models.CharField(max_length=256)),
                ('justification', models.CharField(max_length=2055)),
            ],
        ),
    ]
