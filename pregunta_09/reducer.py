#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter

if __name__ == '__main__':
    tablefile = [lines.replace("\n", "").split('\t') for lines in sys.stdin]

    list_dict0=[]
    list_dict1=[]
    list_dict2=[]

    for i in tablefile:
        list_dict0.append(i[0])
        list_dict1.append(i[1])
        list_dict2.append(int(i[2]))

    data = list(zip(list_dict0, list_dict1, list_dict2))
    result = sorted(data, key=itemgetter(2), reverse = False)

    for lineas in result[:6]:
        sys.stdout.write('{}   {}   {}\n'.format(lineas[0], lineas[1], lineas[2]))