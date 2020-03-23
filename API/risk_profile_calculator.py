from datetime import date

def riskcalculator(personal_info):
#   Começamos calculando o risco base, somando os risk_scoreados das questões binárias e            #
#   colocando o valor num dict de score de risco com os tipos de seguro a serem perfilados.         #

    baserisk = sum(personal_info['risk_questions'])

    if personal_info['age'] < 30:
        baserisk -= 2
    if personal_info['age'] >= 30 and personal_info['age'] <= 40:
        baserisk -= 1
    if personal_info['income'] > 200000:
        baserisk -= 1

    risk_score = {'life':baserisk,'disability':baserisk,'home':baserisk,'auto':baserisk}

#   Com o dicionário definido, aplicamos todas as regras de cálculo definidas no assignment.          #

    if personal_info['house'] == 'mortgaged':
        risk_score['home'] += 1
        risk_score['disability'] -= 1

    if personal_info['dependents'] >= 1:
        risk_score['disability'] += 1
        risk_score['life'] += 1

    if personal_info['marital_status'] == 'married':
        risk_score['life'] += 1
        risk_score['disability'] -= 1

    if personal_info['vehicle'] != None:
        current_year = date.today().year
        if personal_info['vehicle']['year'] >= current_year - 5:
            risk_score['auto'] += 1

#   Aqui, aplicamos as regras de inelegibilidade para seguro definidas no assignment.               #

    if personal_info['age'] > 60:
        risk_score['disability'] = None
        risk_score['life'] = None

    if personal_info['income'] == 0 or personal_info['income'] == None:
        risk_score['disability'] = None

    if personal_info['house'] == None:
        risk_score['home'] = None

    if personal_info['vehicle'] == None:
        risk_score['auto'] = None

#   Por fim, transformamos os valores numéricos do dict de score de risco em texto para o retorno  #

    for key, value in risk_score.items():
        if risk_score[key] == None:
            risk_score[key] = 'Ineligible'
        elif risk_score[key] <= 0:
            risk_score[key] = 'Economic'
        elif risk_score[key] > 0 and risk_score[key] < 3:
            risk_score[key] = 'Regular'
        else:
            risk_score[key] = 'Responsible'

    return risk_score
