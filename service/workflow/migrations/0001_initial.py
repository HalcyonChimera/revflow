# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 21:32
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('values', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('inherit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='heirs', to='workflow.Context')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('message_type', models.CharField(max_length=24)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('ctx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='workflow.Context')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('operation', models.CharField(max_length=32)),
                ('view', models.TextField(blank=True, null=True)),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('responsibilities', models.TextField()),
                ('operation', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='workflow.Operation')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('base_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('key', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('type', models.TextField(default='Any')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('resolver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflow.Operation')),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='service',
            field=models.ManyToManyField(to='workflow.Service'),
        ),
        migrations.AddField(
            model_name='operation',
            name='parameters',
            field=models.ManyToManyField(blank=True, related_name='operations', through='workflow.Argument', to='workflow.Value'),
        ),
        migrations.AddField(
            model_name='operation',
            name='return_value',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='source_operation', to='workflow.Value'),
        ),
        migrations.AddField(
            model_name='message',
            name='origin',
            field=models.ManyToManyField(default=None, related_name='messages', to='workflow.Operation'),
        ),
        migrations.AddField(
            model_name='message',
            name='response',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caller', to='workflow.Operation'),
        ),
        migrations.AddField(
            model_name='context',
            name='workflows',
            field=models.ManyToManyField(related_name='ctxs', to='workflow.Workflow'),
        ),
        migrations.AddField(
            model_name='argument',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='workflow.Operation'),
        ),
        migrations.AddField(
            model_name='argument',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='workflow.Value'),
        ),
    ]
