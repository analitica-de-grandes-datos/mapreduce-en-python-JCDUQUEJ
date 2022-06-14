#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for row in sys.stdin:
        separado = row.replace('\n','').split(',')
        sys.stdout.write('{}\t{}\n'.format(separado[1], separado[0]))