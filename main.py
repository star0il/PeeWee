from csv import reader

from PeeWee_test import Payer, Payment

all_payers = {}


def parse_file(fname="payments.txt"):
    with open(fname) as f:
        csv = reader(f, delimiter=';')
        payments_gen = (p for p in csv if p[-2] == "out")

        for p in payments_gen:
            payer = get_payer(p[0])
            amount, currency = p[1].split()
            Payment.create(payer=payer, amount=amount, currency=currency, created=p[2])

    print(all_payers)
    print("Finished")


def get_payer(payer_name):
    if payer_name not in all_payers:
        all_payers[payer_name] = Payer.create(name=payer_name)
    return all_payers[payer_name]


def main():
    # parse_file()
    q = Payer.select()
    print(q)

    # for p in q:
    #     print(p.id, p.name, p.b_date)

    q = q.where(Payer.name ** "%re%")
    for p in q:
        print(p.id, p.name, p.b_date)
    # print(list(q)[0].name)
    # payments = Payment.select(Payment, Payer).join(Payer).order_by(Payment.payer)
    # payments = payments.where(Payment.payer == 1)
    # for p in payments:
    #     print(p.created, p.amount, p.currency, p.payer.name)


if __name__ == '__main__':
    main()
