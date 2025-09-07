'''
'''

def main():
    filename = 'cinderella.txt'
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            
if __name__ == '__main__':
    main()