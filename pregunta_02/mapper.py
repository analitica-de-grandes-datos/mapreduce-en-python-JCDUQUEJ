#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    for row in sys.stdin:
        word = row.split(',')
        sys.stdout.write("{}\t{}\n".format(word[3],word[4]))