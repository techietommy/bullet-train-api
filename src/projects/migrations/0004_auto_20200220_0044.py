# Generated by Django 2.2.10 on 2020-02-20 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
        ('projects', '0003_auto_20200216_2050'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectPermission',
        ),
        migrations.CreateModel(
            name='ProjectPermissionModel',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('permissions.permissionmodel',),
        ),
        migrations.AlterField(
            model_name='userpermissiongroupprojectpermission',
            name='permissions',
            field=models.ManyToManyField(to='permissions.PermissionModel'),
        ),
        migrations.AlterField(
            model_name='userpermissiongroupprojectpermission',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='grouppermission', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='userprojectpermission',
            name='permissions',
            field=models.ManyToManyField(to='permissions.PermissionModel'),
        ),
        migrations.AlterField(
            model_name='userprojectpermission',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='userpermission', to='projects.Project'),
        ),
    ]
