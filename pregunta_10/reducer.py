#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    total = ''

    for line in sys.stdin:

        key, val = line.replace('\n','').split("\t")

        if key == curkey:
            total +=  ',' + str(val)

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = str(val)

    sys.stdout.write("{}\t{}\n".format(curkey, total))