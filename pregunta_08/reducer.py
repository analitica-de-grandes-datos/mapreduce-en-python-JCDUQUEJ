#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    curkey = None
    total = 0
    cuenta = 0

    for line in sys.stdin:

        key, val1, val2 = line.replace('\n','').split("\t")
        val1 = int(val1)
        val2 = int(val2)

        if key == curkey:
            total += val1
            cuenta += val2
            promedio = total/cuenta

        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))

            curkey = key
            total = val1
            cuenta = val2
            promedio = total/cuenta

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))