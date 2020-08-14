import sys
import checker

def main():
    if sys.argv[1:][0] == "--notf":
        checkEmpty(checker.notFollowingBack())

    if sys.argv[1:][0] == "--needf":
        checkEmpty(checker.needToFollowBack())

def checkEmpty(set):
    if set:
        print(set)
    else:
        print("None")

if __name__ == "__main__":
    main()