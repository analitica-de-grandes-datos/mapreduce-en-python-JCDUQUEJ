#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
from operator import itemgetter
if __name__ == '__main__':
    for row in sys.stdin:
        separado = row.replace('\n','').split('\t')
        key = int(separado[0])
        claves = sorted(separado[1].split(','), key=itemgetter(0), reverse = False)
        for clave in claves:
            sys.stdout.write('{}\t{}\n'.format(clave, key))
