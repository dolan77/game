tax_income = float(input())

tax_liability = 0.00

tax_rate = 0.00


            ### TAX FOR INCOME ABOVE $10,000,000.00 ###

if tax_income > 10_000_000.00:
        tax_liability = (((tax_income - 510300.00) * 0.37) + 153798.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%\n')

        new_liability = (((tax_income - 10_000_000.00) * 0.70) + 3664987.00)

        new_tax_rate = (new_liability / tax_income) * 100

        print('With a new 70% bracket, your tax liability would be ' + '$' + "{0:,.2f}".format(new_liability))

        print('Your effective tax rate with the new bracket would be ' + f"{new_tax_rate:0.1f}" + '%')


            ### TAX FOR INCOME BETWEEN 510,00.00 AND 10,000,000.00 ###

elif 510_300 < tax_income <= 10_000_000:

        tax_liability = (((tax_income - 510300.00) * 0.37) + 153798.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            ### TAX FOR INCOME BETWEEN 204,100.00 AND 510,300.00 ###

elif 204_100.00 < tax_income <= 510_300.00:

        tax_liability = (((tax_income - 204_100.00) * 0.35) + 46_628.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            ### TAX FOR INCOME BETWEEN 160,725.00 AND 204,100.00 ###

elif 160_725.00 < tax_income <= 204_100.00:

        tax_liability = (((tax_income - 160_725.00) * 0.32) + 32_748.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            ### TAX FOR INCOME BETWEEN 84,200.00 AND 160,725.00 ###

elif 84_200.00 < tax_income <= 160_725.00:

        tax_liability = (((tax_income - 84_201.00) * .24) + 14_382.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            #TAX FOR INCOME BETWEEN 39,475.00 AND 84,200.00 ###

elif 39_475 < tax_income <= 84_200.00:

        tax_liability = (((tax_income - 39_475.00) * 0.22) + 4_543.00)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            ### TAX BETWEEN 9,700.00 AND 39,475.00 ###

elif 9_700 < tax_income <= 39_475.00:

        tax_liability = (((tax_income - 9_700) * .12) + 970)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')

            ### TAX FOR INCOME BETWEEN 0.00 AND 9,700.00 ###

elif 0 <= tax_income <= 9_700:

        tax_liability = (((tax_income - 0) * .10) + 0)

        tax_rate = (tax_liability / tax_income) * 100

        print('Your tax liability is ' + '$' + "{0:,.2f}".format(tax_liability))

        print('Your effective tax rate is ' + f"{tax_rate:0.1f}" + '%')