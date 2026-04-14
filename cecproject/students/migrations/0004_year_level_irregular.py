from django.db import migrations, models


def migrate_fifth_year_to_irregular(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student.objects.filter(year_level='5th Year').update(year_level='Irregular Student')


def revert_irregular_to_fifth_year(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Student.objects.filter(year_level='Irregular Student').update(year_level='5th Year')


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_status_note_and_pending_reason'),
    ]

    operations = [
        migrations.RunPython(migrate_fifth_year_to_irregular, revert_irregular_to_fifth_year),
        migrations.AlterField(
            model_name='student',
            name='year_level',
            field=models.CharField(
                choices=[
                    ('1st Year', '1st Year'),
                    ('2nd Year', '2nd Year'),
                    ('3rd Year', '3rd Year'),
                    ('4th Year', '4th Year'),
                    ('Irregular Student', 'Irregular Student'),
                ],
                max_length=20,
            ),
        ),
    ]
