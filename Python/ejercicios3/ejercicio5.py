año1 = int(input('año actual: '))
año2 = int(input('año anterior o proximo: '))

if año1 < año2:
    años = año2 - año1
    print('faltan ' + str(años) + ' años para llegar al año ' + str(año2))

elif año1 > año2:
    años = año1 - año2
    print('han pasado ' + str(años) + ' desde el ' + str(año2))
