#!/usr/bin/env python3

from qftimports import *


def help():
    print("------------------------------------")
    print("| Quantum Field Theory - Help menu |")
    print("------------------------------------")
    print("")
    print("parameters")
    print("----------")
    print("Wick contractions")
    print(".................")
    print("Used for calculating all possibile Wick contractions for free vev.")
    print("syntax: --wick <type> <mode> <fields>")
    print("type: rsf (real scalar field), csf (complex scalar field)")
    print("mode: all, vac (vacuum only), nvac (non-vacuum only)")
    print("fields: numbered fields, e.g. 1 2 3 3 (note the spacing)")
    print("")


def main():
    version = 1.0

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
        sys.exit(2)

    for o, a in opts:
        if o in ("-v", "--version"):
            print("version: {}".format(version))

        elif o in ("-h", "--help"):
            help()

        elif o in ("-w", "--wick"):
            field_type = sys.argv[2]
            mode = sys.argv[3]
            fields = sys.argv[4:]

            if len(fields) > 10:
                question = input("This may take a while. Continue? [y/n]")
                if question == "y":
                    wickContractions(field_type, fields, mode)
                elif question == "n":
                    print("process stopped.")
                else:
                    print("unknown input parameter. process stopped.")
                    
            else:
                wickContractions(field_type, fields, mode)

        else:
            print("Error: unknown arg")
            sys.exit(1)


if __name__ == '__main__':
    main()
