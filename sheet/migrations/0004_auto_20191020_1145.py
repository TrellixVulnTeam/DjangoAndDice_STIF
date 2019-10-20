# Generated by Django 2.2.6 on 2019-10-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheet', '0003_auto_20191020_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='acrobatics',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='animal_handling',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='arcana',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='armor_class',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='athletics',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='atk_spell_bonus',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='atk_spell_name',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='atk_spell_type',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='charisma',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='charisma_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='constitution',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='constitution_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='deception',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='dexterity',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='dexterity_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='dth_fail',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='dth_succ',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='feat_trait',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='history',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='hit_dice',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='hp_curr',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='hp_temp',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='initiative',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='insight',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='inspiration',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='intelligence',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='intelligence_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='intimidation',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='investigation',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='medicine',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='nature',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='oth_prof_lang',
            field=models.CharField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='pass_wisdom',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='perception',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='performance',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='persuasion',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='proficiency',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='religion',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_charisma',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_constitution',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_dexterity',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_intelligence',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_strength',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sav_wisdom',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='sleight_hand',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='speed',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='stealth',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='strength',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='strength_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='survival',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='wisdom',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sheet',
            name='wisdom_mod',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
