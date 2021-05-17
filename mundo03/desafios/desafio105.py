def notas(*nota, sit=False):
    lista = {}
    aux = []
    for v in nota:
        aux.append(v)
    lista['total'] = len(aux)
    lista['maior'] = max(aux)
    lista['menor'] = min(aux)
    lista['média'] = sum(aux)/len(aux)
    if sit:
        if 6 < lista['média'] < 7:
            lista['situação'] = 'RAZOÁVEL'
        elif lista['média'] > 7:
            lista['situação'] = 'BOM'
        else:
            lista['situação'] = 'RUIM'
    return lista


print(notas(8, 9, 5, 9, sit=True))