from random import randint

pizdec=['ты', 'ебать', 'лох', 'еблан', 'долбоёб', 'хуйло', 'гандон', 'педик', 'черножопый', 'черномазый']
print(pizdec)


match randint(1, 4):
    case 1:
        pizdec.reverse()
        print(pizdec)
    case 2:
        pizdec = pizdec[::-30]
        print(pizdec)
    case 3:
        pizdec = pizdec[2:] + pizdec[:2]
        print(pizdec)
    case 4:
        pizdec = pizdec[5:] + pizdec[:5]
        print(pizdec)

pizdecToString = ' '.join(map(str, pizdec))
print(pizdecToString)