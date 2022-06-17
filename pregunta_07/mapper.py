#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for line in sys.stdin:
        line = line.replace('\n','').split('   ')
        sys.stdout.write('{}\t{}\t{}\n'.format(line[0], line[1], line[2]))

