# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountDeposits(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    beneficiary = models.ForeignKey('Beneficiaries', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'account_deposits'
        unique_together = (('user', 'beneficiary', 'amount', 'created_at'),)


class Accounts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class ActivityLog(models.Model):
    log_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    subject_type = models.CharField(max_length=255, blank=True, null=True)
    subject_id = models.BigIntegerField(blank=True, null=True)
    causer_type = models.CharField(max_length=255, blank=True, null=True)
    causer_id = models.BigIntegerField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    batch_uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class Beneficiaries(models.Model):
    name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiaries'


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    owner = models.CharField(max_length=255)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache_locks'


class Cashes(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashes'


class Cashings(models.Model):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashings'


class Categories(models.Model):
    name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Configs(models.Model):
    logo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    telephone = models.TextField()  # This field type is a guess.
    operators = models.TextField()  # This field type is a guess.
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configs'


class DemandProduct(models.Model):
    demand = models.ForeignKey('Demands', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'demand_product'
        unique_together = (('product', 'demand'),)


class Demands(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    to_id = models.IntegerField(blank=True, null=True)
    validated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demands'


class Deposits(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    date = models.DateField()
    amount = models.FloatField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deposits'


class Expenses(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    beneficiary_id = models.BigIntegerField(blank=True, null=True)
    motif = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField()
    status = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenses'


class FailedJobs(models.Model):
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Fees(models.Model):
    min = models.FloatField()
    max = models.FloatField()
    fee = models.FloatField()
    mobile_money = models.ForeignKey('MobileMoney', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fees'


class Messages(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    body = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MobileMoney(models.Model):
    name = models.CharField(max_length=255)
    fee = models.FloatField(blank=True, null=True)
    send = models.BooleanField()
    product = models.ForeignKey('Products', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=qTrue)

    class Meta:
        managed = False
        db_table = 'mobile_money'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class Money(models.Model):
    customer = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    raw = models.FloatField()
    net = models.FloatField()
    fee = models.FloatField()
    mobile_money = models.ForeignKey(MobileMoney, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'money'


class Notifications(models.Model):
    id = models.UUIDField(primary_key=True)
    type = models.CharField(max_length=255)
    notifiable_type = models.CharField(max_length=255)
    notifiable_id = models.BigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class ObjectiveProduct(models.Model):
    objective = models.ForeignKey('Objectives', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'objective_product'


class Objectives(models.Model):
    date = models.DateField()
    amount = models.FloatField()
    operator = models.ForeignKey('Operators', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'objectives'


class Operators(models.Model):
    priority = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operators'


class OrderProduct(models.Model):
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    price = models.FloatField()
    commission = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField(blank=True, null=True)
    net = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_product'
        unique_together = (('order', 'product'),)


class Orders(models.Model):
    reference = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    payment = models.CharField(max_length=255)
    operator = models.ForeignKey(Operators, models.DO_NOTHING)
    validated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Participants(models.Model):
    thread_id = models.IntegerField()
    user_id = models.IntegerField()
    last_read = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participants'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Payments(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    sale = models.ForeignKey('Sales', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments'


class Permissions(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PersonalAccessTokens(models.Model):
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class ProductSale(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    sale = models.ForeignKey('Sales', models.DO_NOTHING)
    quantity = models.FloatField()
    price = models.FloatField()
    before = models.FloatField(blank=True, null=True)
    after = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    net = models.FloatField(blank=True, null=True)
    commission = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_sale'
        unique_together = (('sale', 'product'),)


class ProductType(models.Model):
    product = models.ForeignKey('Products', models.DO_NOTHING)
    type = models.ForeignKey('Types', models.DO_NOTHING)
    before = models.FloatField()
    after = models.FloatField()

    class Meta:
        managed = False
        db_table = 'product_type'


class Products(models.Model):
    priority = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    commission = models.FloatField()
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    operator = models.ForeignKey(Operators, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Regions(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'


class Resellers(models.Model):
    avatar = models.CharField(max_length=255, blank=True, null=True)
    number = models.BigIntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=255)
    birthday = models.DateField()
    birthplace = models.CharField(max_length=255)
    telephone = models.TextField()  # This field type is a guess.
    type = models.ForeignKey('Types', models.DO_NOTHING)
    region = models.ForeignKey(Regions, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resellers'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Salaries(models.Model):
    amount = models.FloatField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    period = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salaries'


class Sales(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    reseller_id = models.BigIntegerField(blank=True, null=True)
    type_sale = models.ForeignKey('TypeSales', models.DO_NOTHING)
    cash = models.FloatField()
    customer = models.CharField(max_length=255, blank=True, null=True)
    payed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class Stocks(models.Model):
    product = models.ForeignKey(Products, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    quantity = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'


class Surpluses(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surpluses'


class Threads(models.Model):
    subject = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'threads'


class TransferCashes(models.Model):
    from_field = models.ForeignKey('Users', models.DO_NOTHING, db_column='from_id')  # Field renamed because it was a Python reserved word.
    to = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.FloatField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transfer_cashes'


class TypeSales(models.Model):
    name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_sales'


class Types(models.Model):
    name = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class Users(models.Model):
    avatar = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=255)
    birthday = models.DateField()
    birthplace = models.CharField(max_length=255)
    telephone = models.TextField()  # This field type is a guess.
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    salary = models.FloatField()
    region = models.ForeignKey(Regions, models.DO_NOTHING)
    accountable = models.BooleanField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class WebsocketsStatisticsEntries(models.Model):
    app_id = models.CharField(max_length=255)
    peak_connection_count = models.IntegerField()
    websocket_message_count = models.IntegerField()
    api_message_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'websockets_statistics_entries'
