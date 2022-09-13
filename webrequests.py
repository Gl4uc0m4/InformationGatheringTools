import requests
import argparse


parser = argparse.ArgumentParser(description='Process url and returns server header response')
parser.add_argument('-t','--target',help='url for target site e.g https://example.com')
parser = parser.parse_args()

def main():
    try:
        target = requests.get(url=parser.target)
        headers = dict(target.headers)
        for h in headers:
            print(h + ' = ' + headers[h])
    except:
        print(' SYNTAX ERROR ---- https://example.com')
 
if __name__=='__main__':
    try:
        main()
    except:
        exit()