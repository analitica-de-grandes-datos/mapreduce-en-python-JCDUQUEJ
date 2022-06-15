#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
from operator import itemgetter
if __name__ == '__main__':
    df = sys.stdin
    for line in df:
        line = line.replace('\n','').split('\t')

    dfsort = sorted(df,key=itemgetter(2), reverse = False)
    dfsort = dfsort[:6]

    for row in dfsort:
        row1 = row.replace('\n','').split('   ')
        sys.stdout.write('{}\t{}\t{}\n'.format(row1[0], row1[1], row1[2]))

