import argparse
import math


def loan_principal(payment, periods, interest):
    principal = payment / ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1))
    overpayment = payment * periods - principal
    print("Your loan principal = {0}!".format(principal))
    print("Overpayment = {0}".format(overpayment))


def annuity_payment(principal, periods, interest):
    payment = principal * (interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1)
    print("Your annuity payment = {0}!".format(math.ceil(payment)))
    math.ceil(payment * periods - principal)


def period_payment(principal, payment, interest):
    n = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    number_of_years = n // 12
    number_of_months = n - number_of_years * 12
    output = "It will take "
    if number_of_years != 0:
        if number_of_years == 1:
            output += "1 year "
        else:
            output += "{0} years ".format(number_of_years)
    if number_of_months != 0:
        if number_of_months == 1:
            output += "1 month "
        else:
            output += "{0} months ".format(number_of_months)
    output += "to repay this loan!"
    overpayment = (number_of_years * 12 + number_of_months) * payment - principal
    print(output)
    print("Overpayment = {0}".format(overpayment))


def differentiated_payments(principal, periods, interest):
    overpayment = 0
    for i in range(1, periods + 1):
        payment = math.ceil(principal / periods
                            + interest * (principal - principal * (i - 1) / periods))
        overpayment += payment
        print("Month {0}: payment is {1}".format(i, payment))
    overpayment -= principal
    print()
    print("Overpayment = {0}".format(overpayment))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--principal")
    parser.add_argument("--payment")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    args = parser.parse_args()

    type_of_payment = args.type
    principal = args.principal
    payment = args.payment
    periods = args.periods
    interest = args.interest

    if type_of_payment is None:
        print("Incorrect parameters")
        return

    elif args.type == "diff":
        if payment is not None \
                or principal is None \
                or periods is None \
                or interest is None:
            print("Incorrect parameters")
            return
        else:
            differentiated_payments(float(principal), int(periods), float(interest) / 1200)

    elif type_of_payment == "annuity":
        if principal is None \
                and payment is not None \
                and periods is not None \
                and interest is not None:
            loan_principal(float(payment), int(periods), float(interest) / 1200)
        elif payment is None \
                and principal is not None \
                and periods is not None \
                and interest is not None:
            annuity_payment(float(principal), int(periods), float(interest) / 1200)
        elif periods is None \
                and principal is not None \
                and payment is not None \
                and interest is not None:
            period_payment(float(principal), float(payment), float(interest) / 1200)
        else:
            print("Incorrect parameters")


main()
