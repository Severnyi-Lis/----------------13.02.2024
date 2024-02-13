hour = int(input('Сколько сейчас времени (в часах)?'))
if hour>= 4 and hour<=11:
    print('Сейчас утро')
if hour > 11 and hour<=17:
 print('Сейчас день')
if hour > 17 and hour<= 23:
   print('Сейчас вечер')
if hour > 23 or hour<=3:
   print('Сейчас ночь')
 