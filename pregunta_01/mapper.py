#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for row in sys.stdin:
        sys.stdout.write("{}\t1\n".format(row.split(',')[4]))