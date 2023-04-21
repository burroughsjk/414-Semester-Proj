import dns.resolver
import sys
# Subdomain list sourced from https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt


domain = sys.argv[1]
subdomain_array = ['lib', 'a', 'dns', 'open', 'm', 'img', 'studio', 'tv']


def main():
    subdomain_store = []
    with open('output.txt', 'w') as f:  
        for subdoms in subdomain_array:
            try:
                ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
                if ip_value:
                    subdomain_store.append(f'{subdoms}.{domain}')
                    if f'{subdoms}.{domain}' in subdomain_store:
                        print(f'{subdoms}.{domain} valid')
                        f.write(f'{subdoms}.{domain} \n')
                    else:
                        pass
            except dns.resolver.NXDOMAIN:
                print("Subdomain not found!")
                pass
            except dns.resolver.NoAnswer:
                pass
            except KeyboardInterrupt:
                quit()

main()