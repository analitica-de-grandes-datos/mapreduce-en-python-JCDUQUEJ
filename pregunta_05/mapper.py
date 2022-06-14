#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for row in sys.stdin:
        linea = row.split('   ')[1]
        linea2 = linea.split('-')[1]
        sys.stdout.write('{}\t1\n'.format(linea2))
