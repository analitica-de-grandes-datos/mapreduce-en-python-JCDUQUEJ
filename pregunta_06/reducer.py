#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    min = 0
    max = 0

    for line in sys.stdin:

        key, val = line.split('\t')

        if key == curkey:
            if val > max:
                max = val

            if val  < min:
                min = val

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max, min))

            curkey = key
            min = val
            max = val
