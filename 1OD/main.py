import os

def deal(line):
    # line = line.strip()
    line = line.split(' ')
    return ','.join(line)

def main():
    data_dir = '.\\data'
    files = os.listdir(data_dir)

    first = open('first.xls', 'w')
    last = open('last.xls', 'w')

    for file in files:
        with open(os.path.join(data_dir,file)) as f:
            lines = f.readlines()
            first.write(deal(lines[0]))
            last.write(deal(lines[-1]))
    first.close()
    last.close()

if __name__ == '__main__':
    main()
