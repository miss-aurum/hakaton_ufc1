# Generated by Django 4.1.6 on 2023-02-09 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ufc', '0002_alter_info_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleTurnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowdown', models.CharField(max_length=10, verbose_name='Нокдауны')),
                ('tot_strokes', models.CharField(max_length=10, verbose_name='Всего ударов')),
                ('accent_hits', models.CharField(max_length=10, verbose_name='Акцент удары')),
                ('tr_ground', models.CharField(max_length=10, verbose_name='Переводы в партер')),
                ('surr_attemps', models.CharField(max_length=10, verbose_name='Попытки сдачи')),
            ],
            options={
                'verbose_name': 'Участник турнира',
                'verbose_name_plural': 'Учасники турнира',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=500)),
                ('youtube', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=20, verbose_name='')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ф.И.О тренера')),
                ('image', models.ImageField(upload_to='photoTrainer/%Y/%m/%d/', verbose_name='Фотка Информация о тренере ')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Турнир',
                'verbose_name_plural': 'Турниры',
            },
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Social',
        ),
        migrations.DeleteModel(
            name='Treiner',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт для сотрудничество', 'verbose_name_plural': 'Контакты для сотрудничество'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='sportman',
            options={'verbose_name': 'Спортсмен', 'verbose_name_plural': 'Спортсмены'},
        ),
        migrations.AddField(
            model_name='sportman',
            name='image',
            field=models.ImageField(default=123, upload_to='Фото спортсмена', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='massage',
            field=models.TextField(verbose_name='Сообщения о сотрудничестве'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='sportman',
            name='category',
            field=models.CharField(choices=[('w_1', 'Наилегчайший вес'), ('w_2', 'Легчайший вес'), ('w_3', 'Полулёгкий вес'), ('w_4', 'Легкий вес '), ('w_5', 'Полусредний вес'), ('w_6', 'Средний вес'), ('w_7', 'Полутяжёлый вес'), ('w_8', 'Тяжёлый вес')], max_length=3),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='peopleturnir',
            name='sportsmen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ufc.sportman'),
        ),
        migrations.AddField(
            model_name='peopleturnir',
            name='turnir',
            field=models.ManyToManyField(to='app_ufc.turnir', verbose_name='Номер турнира'),
        ),
        migrations.AddField(
            model_name='sportman',
            name='trainer',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='app_ufc.trainer'),
            preserve_default=False,
        ),
    ]
