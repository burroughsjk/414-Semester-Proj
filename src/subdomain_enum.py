import dns.resolver
import sys
# Subdomain list sourced from https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt


domain = sys.argv[1]
subdomain_array = ['lib', 'img', 'dns', 'open', 'm', 'a', 'studio', 'tv']


def main():
    subdomain_store = []
    with open('output.txt', 'w') as f, open('log.txt', 'w') as l:  
        for subdoms in subdomain_array:
            try:
                ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
                if ip_value:
                    subdomain_store.append(f'{subdoms}.{domain}')
                    if f'{subdoms}.{domain}' in subdomain_store:
                        print(f'[VALID] {subdoms}.{domain}')
                        f.write(f'{subdoms}.{domain} \n')
                        l.write(f'[VALID] {subdoms}.{domain} \n')
                    else:
                        pass
            except dns.resolver.NXDOMAIN:
                logException(subdoms, "NXDOMAIN", l)
                pass
            except dns.resolver.NoAnswer:
                logException(subdoms, "NoAnswer", l)
                pass
            except dns.resolver.Timeout:
                logException(subdoms, "Timeout", l)
                pass
            except KeyboardInterrupt:
                print("--------- Keyboard interrupt detected - program killed ---------")
                l.write("--------- Keyboard interrupt detected - program killed ---------")
                quit()


def logException(subdom, exceptionType, file):
        print('[NOT FOUND - ' + exceptionType + '] ' + f'{subdom}.{domain}')
        file.write('[NOT FOUND - ' + exceptionType + '] ' + f'{subdom}.{domain} \n')

main()