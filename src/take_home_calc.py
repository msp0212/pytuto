ctc_per_annum = 111111111.11
# ctc breakup
basic_per_annum = 11111.11
hra_per_annum = 111111.11
food_coupon_per_annum = 1111.11
technical_books_and_training_per_annum = 1111.11
# rent paid
rent_paid_per_annum = 11111.11
living_in_metro = False

# employer pf is 12% of basic
employer_pf_per_annum = 0.12 * basic_per_annum
# gratuity is 4.81% of basic
gratuity_per_annum = .0481 * basic_per_annum

print('A ctc: ', ctc_per_annum)
print('\tA1 basic: ', basic_per_annum)
print('\tA2 hra: ', hra_per_annum)
print('B employer pf (12% of basic): ', employer_pf_per_annum)
print('C gratuity: (4.81% of basic)', gratuity_per_annum)

gross_salary_per_annum = ctc_per_annum - employer_pf_per_annum - gratuity_per_annum
print('D gross salary(A - B - C): ', gross_salary_per_annum)

# hra exemption (section 10-13A) is minimum of below 3:
# actual hra received,
# 40% (non-metro) or 50% (mtero) of basic
# actual rent paid less 10% of basic)
hra_exemption = hra_per_annum
if (living_in_metro):
    tmp1 = 0.50 * basic_per_annum
else:
    tmp1 = 0.40 * basic_per_annum
if (hra_exemption > tmp1):
    hra_exemption = tmp1
tmp2 = rent_paid_per_annum - (.10 * basic_per_annum)
if (hra_exemption > tmp2):
    hra_exemption = tmp2
print('E hra exemption: ', hra_exemption)
misc_exemptions = food_coupon_per_annum + technical_books_and_training_per_annum
print('F misc exemptions (meal coupons, tech books and training): ', misc_exemptions)
# deduction under section 16(ia)
standard_deduction = 50000.00
print('G standard deduction: ', standard_deduction)
# deduction under section 16(iii)
professional_tax_per_annum = 2400.00
print('H professional tax deduction: ', professional_tax_per_annum)

taxable_salary_after_exemptions = gross_salary_per_annum - hra_exemption - misc_exemptions - standard_deduction - professional_tax_per_annum
print('I taxable salary after exemptions (D - E - F - G - H): ', taxable_salary_after_exemptions)

take_home_salay_per_annum_before_taxes = gross_salary_per_annum - misc_exemptions - professional_tax_per_annum

# rental income, interest earned, capital gains etc.
income_from_other_sources_per_annum = 0
print('J income from other sources: ', income_from_other_sources_per_annum)

# gross total income = net salary + income from other sources
taxable_income_per_annum = taxable_salary_after_exemptions + income_from_other_sources_per_annum
print('K total taxable income(I + J): ', taxable_income_per_annum)

# deduction under chapter VI A section 80c
employee_pf_per_annum = 0.12 * basic_per_annum
print('L employee pf: ', employee_pf_per_annum)
life_insurance_premium = 31886.00
print('M life insurance premium: ', life_insurance_premium)
exemption_80c = min(150000.00, employee_pf_per_annum + life_insurance_premium)
print('N 80c exemption: ', exemption_80c)
# deduction section chapter VI A section 80d
medical_insurance_premium = 18000.00
exemption_80d = medical_insurance_premium
print('O 80d exemption: ', exemption_80d)

# taxable income
taxable_income_per_annum_after_exemptions = taxable_income_per_annum - exemption_80c - exemption_80d
print('P total taxable income after exemptions (K - N - O): ', taxable_income_per_annum_after_exemptions)

# income tax
slab1 = 250000.00
slab2 = 500000.00
slab3 = 1000000.00
if taxable_income_per_annum_after_exemptions <= slab1:
    income_tax = 0.0
elif taxable_income_per_annum_after_exemptions > slab1 and taxable_income_per_annum_after_exemptions <= slab2:
    income_tax = 0.05 * (taxable_income_per_annum_after_exemptions - slab1)
elif taxable_income_per_annum_after_exemptions > slab2 and taxable_income_per_annum_after_exemptions <= slab3:
    income_tax = (0.05 * (slab2 - slab1)) + (0.20 * (taxable_income_per_annum_after_exemptions - slab2))
else:  # taxable income > slab3
    income_tax = (0.05 * (slab2 - slab1)) + (0.20 * (slab3 - slab2)) + (
                0.30 * (taxable_income_per_annum_after_exemptions - slab3))
print('Q income tax (per annum | per month): ', income_tax, ' | ', income_tax / 12)

take_home_salay_per_annum = take_home_salay_per_annum_before_taxes - income_tax
print('S take home salary (per annum | per month): ', take_home_salay_per_annum, ' | ', take_home_salay_per_annum / 12)
