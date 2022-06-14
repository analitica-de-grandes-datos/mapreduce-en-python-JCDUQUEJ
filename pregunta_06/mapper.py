#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for row in sys.stdin:
        row1 = row.replace('\n','').split('   ')
        sys.stdout.write('{}\t{}\n'.format(row1[0], row1[2]))