from peewee import SqliteDatabase, Model, CharField, DateField, ForeignKeyField, DateTimeField, DoubleField

db = SqliteDatabase("payments.db")


class Payer(Model):
    class Meta:
        database = db
        table_name = "payer"

    name = CharField(unique=True)
    b_date = DateField(null=True)


class Payment(Model):
    class Meta:
        database = db

    payer = ForeignKeyField(Payer)
    created = DateTimeField()
    amount = DoubleField()


def init_db():
    db.drop_tables([Payment, Payer], safe=True)
    db.create_tables([Payment, Payer], safe=True)


if __name__ == '__main__':
    init_db()
