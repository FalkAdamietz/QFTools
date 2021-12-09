#!/usr/bin/env python3

from qftimports import *


def help():
    print("------------------------------------")
    print("| Quantum Field Theory - Help menu |")
    print("------------------------------------")
    print("")
    print("parameters")
    print("----------")
    print("")
    print("Wick contractions")
    print(".................")
    print("Used for calculating all possibile Wick contractions for free vev.")
    print("")
    print("syntax: --wick <type> <mode> <output> <fields>")
    print("")
    print("type: rsf (real scalar field), csf (complex scalar field)")
    print("mode: all, vac (vacuum only), nvac (non-vacuum only)")
    print("output: print (prints result on console), save (saves result in csv-file)")
    print("fields: numbered fields, e.g. 1 2 3 3 (note the spacing)")
    print("")


def main():
    version = 1.1

    short = "vhw"
    long = [
        "version",
        "help",
        "wick",
    ]

    try:
        opts, args = getopt.getopt(sys.argv[1:], short, long)
    except getopt.GetoptError as err:
        print(err)
        print("")
        help()
        sys.exit(2)

    for o, a in opts:
        if o in ("-v", "--version"):
            print("version: {}".format(version))

        elif o in ("-h", "--help"):
            help()

        elif o in ("-w", "--wick"):
            field_type = sys.argv[2]
            mode = sys.argv[3]
            output = sys.argv[4]
            fields = sys.argv[5:]

            if len(fields) > 10:
                question = input("This may take a while. Continue? [y/n]")
                if question == "y":
                    wickContractions(field_type, fields, mode, output)
                elif question == "n":
                    print("process stopped.")
                else:
                    print("unknown input parameter. process stopped.")

            else:
                wickContractions(field_type, fields, mode, output)

        else:
            print("unknown input parameter")
            print("")
            help()
            sys.exit(1)


if __name__ == '__main__':
    main()
