from datetime import date

def calculator(customer):

    baserisk = sum(customer['risk_questions'])

    if customer['age'] < 30:
        baserisk -= 2
    if customer['age'] >= 30 and customer['age'] <= 40:
        baserisk -= 1
    if customer['income'] > 200000:
        baserisk -= 1

    result = {'life':baserisk,'disability':baserisk,'home':baserisk,'auto':baserisk}

    if customer['house'] == 'mortgaged':
        result['home'] += 1
        result['disability'] -= 1

    if customer['dependents'] >= 1:
        result['disability'] += 1
        result['life'] += 1

    if customer['marital_status'] == 'married':
        result['life'] += 1
        result['disability'] -= 1

    if customer['vehicle'] != None:
        current_year = date.today().year
        if customer['vehicle']['year'] >= current_year - 5:
            result['auto'] += 1

    if customer['age'] > 60:
        result['disability'] = None
        result['life'] = None

    if customer['income'] == 0 or customer['income'] == None:
        result['disability'] = None

    if customer['house'] == None:
        result['home'] = None

    if customer['vehicle'] == None:
        result['auto'] = None


    for key, value in result.items():
        if result[key] == None:
            result[key] = 'Ineligible'
        elif result[key] <= 0:
            result[key] = 'Economic'
        elif result[key] > 0 and result[key] < 3:
            result[key] = 'Regular'
        else:
            result[key] = 'Responsible'

    return result
