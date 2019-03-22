import BattleshipRefactored

if __name__ == "__main__":
    import sys
    import time


    for j in range(5):
        for i in range(10):
            sys.stdout.write("{0}>\n".format("="*(j+i)))
            sys.stdout.flush()
        for _ in range(10): 
            sys.stdout.write("\033[F")
            sys.stdout.flush()
        time.sleep(0.5)