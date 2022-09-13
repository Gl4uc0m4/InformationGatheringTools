import dns.resolver
import sys

'''
 Returns the dns records specified in rtypes, if you want to change this script feel free to do it. :)

 To run this script just type --> python3 dnsenum.py <domain name>  e.g domain name <example.com>

 For the first import install dnspython using pip3 install dnspython

'''


def main():
    try:
        domain = sys.argv[1]
    except:
        print('SYNTAX ERROR ---- python3 dnsenum.py <domain name>')
        exit()

    rtypes = ['A','AAAA', 'NS','MX', 'TXT', 'SOA', 'PTR','CNAME']
    for records in rtypes:
        try: 
            target = dns.resolver.resolve(qname=domain,rdtype=records)
            print('/' + '*'*10 + '/')
            print(f'{records} records')
            print('-'*100)
            for e in target:
                print(e.to_text() + '\n')
        except dns.resolver.NoAnswer:
            print('No records found for ' + f'{records}')
        except dns.resolver.NXDOMAIN:
            print('ERROR ---- The DNS query name does not exist')
            exit()
        except dns.resolver.NoNameservers:
            print('ERROR ---- All nameservers failed to answer the query or you mistyped the domain name')
            exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()