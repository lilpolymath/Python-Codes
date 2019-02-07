import re
def main():
    ReplaceWord()
    DemarcationLine()
    MatchAndReplaceWord()

def ReplaceWord():
    try:
        files = open('regex.txt')
        for line in files:
            #Search for any word
            print(re.sub('lenor|more', "####",line), end = ' ')
    except FileNotFoundError as e:
        print("File not found: ",e)

def MatchAndReplaceWord():
    try:
        files = open('regex.txt')
        for line in files:
            #you can search for anything that can matches a particular pattern
            match = re.search('(len|neverm)ore', line)
            if match:
                print(line.replace(match.group(), '####'), end = ' ')
    except FileNotFoundError as e:
        print("File not found: ", e)

def DemarcationLine():
    print("\n*********")

if __name__ == '__main__':
    main()
