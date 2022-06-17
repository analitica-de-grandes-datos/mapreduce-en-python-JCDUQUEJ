#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter

if __name__ == '__main__':


    tablefile = [lines.replace("\n", "").split('\t') for lines in sys.stdin]

    list_dict0=[]
    list_dict1=[]

    for i in tablefile:
        list_dict0.append(i[0])
        list_dict1.append(int(i[1]))

    data = list(zip(list_dict0, list_dict1))
    data = sorted(data, key = itemgetter(0,1), reverse = False)

    curkey = None
    total = ''

    for lineas in data:

        key = lineas[0]
        val = lineas[1]

        if key == curkey:
            total +=  ',' + str(val)

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = str(val)
    sys.stdout.write("{}\t{}\n".format(curkey, total))

