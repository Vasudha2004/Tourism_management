# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    booking_id = models.CharField(primary_key=True, max_length=10)
    pack = models.ForeignKey('Package', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    fromdate = models.CharField(db_column='FromDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    todate = models.CharField(db_column='ToDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='RegDate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)
    cancelledby = models.CharField(db_column='CancelledBy', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'


class Category(models.Model):
    cat_id = models.IntegerField(db_column='Cat_id', primary_key=True)  # Field name made lowercase.
    cat_name = models.CharField(db_column='Cat_name', max_length=2000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Contactus(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    phno = models.BigIntegerField(db_column='PhNo', unique=True)  # Field name made lowercase.
    email_id = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'contactus'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    feedback = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class Issues(models.Model):
    query_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    email_id = models.CharField(max_length=200, blank=True, null=True)
    query = models.CharField(max_length=1000, blank=True, null=True)
    reply_given = models.CharField(max_length=2000, blank=True, null=True)
    show_faq = models.IntegerField(db_column='show_FAQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'issues'


class Package(models.Model):
    pack_id = models.IntegerField(primary_key=True)
    pack_name = models.CharField(max_length=1000)
    cat = models.ForeignKey(Category, models.DO_NOTHING)
    subcat = models.ForeignKey('Subcategory', models.DO_NOTHING)
    pack_price = models.IntegerField()
    pic1 = models.CharField(max_length=600)
    pic2 = models.CharField(max_length=600)
    detail = models.CharField(max_length=600)

    class Meta:
        managed = False
        db_table = 'package'


class Payment(models.Model):
    payment_id = models.CharField(max_length=50)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.IntegerField()
    mode = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'


class Subcategory(models.Model):
    cat = models.ForeignKey(Category, models.DO_NOTHING, db_column='Cat_id')  # Field name made lowercase.
    subcat_id = models.CharField(db_column='Subcat_id', primary_key=True, max_length=200)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=1000)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=2000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subcategory'


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=2000)
    mob_num = models.BigIntegerField(unique=True)
    email_id = models.CharField(unique=True, max_length=50)
    pswd = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'
