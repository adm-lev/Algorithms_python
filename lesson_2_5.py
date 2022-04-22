"""
https://drive.google.com/file/d/1lbDmorKEVNW1aGfTm4FM3Sv3kPy9e2-2/view?usp=sharing
Вывести на экран коды и символы таблицы ASCII, начиная с символа под
номером 32 и заканчивая 127-м включительно. Вывод выполнить в
табличной форме: по десять пар "код-символ" в каждой строке.

"""


def sipher(start=32, stop=127):

    if stop - start <= 10:
        i = start
        while i < stop:
            print(f'{i}={chr(i)}', end=' ')
            i += 1
        print('\n')
    else:
        sipher(start, start+10)
        sipher(start+11, stop)


sipher()
