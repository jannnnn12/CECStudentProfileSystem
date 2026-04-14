from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_email_student_is_active_student_school_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status_note',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='status_reason',
            field=models.CharField(
                blank=True,
                choices=[
                    ('active', 'Active'),
                    ('pending_approval', 'Pending Approval'),
                    ('school_transfer', 'School Transfer'),
                    ('stopped_school', 'Stopped School'),
                    ('other', 'Other'),
                ],
                default='active',
                max_length=20,
            ),
        ),
    ]
