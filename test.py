import sys, argv

if __name__ == "__main__":
    args_v1 = argv.main(sys.argv)
    args_v2 = argv.start([1],b=2)
    print args_v1, 'or', args_v2
