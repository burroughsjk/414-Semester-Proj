import dns.resolver
import sys
# Subdomain list sourced from https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt


domain = sys.argv[1]
subdomain_array = ['lib', 'img', 'dns', 'open', 'm', 'a', 'studio', 'tv']


def logException(subdom, exceptionType, file):
		print('[NOT FOUND - ' + exceptionType + '] ' + f'{subdom}.{domain}')
		file.write('[NOT FOUND - ' + exceptionType + '] ' + f'{subdom}.{domain} \n')

def summarize(num_total, num_valid, num_invalid, file):
	print('\n')
	print('---------------- Summary ----------------')
	print('Total subdomains checked: ' + str(num_total))
	print('Total valid subdomains found: ' + str(num_valid))
	print('Total invalid subdomains: ' + str(num_invalid))
	
	file.write('\n')
	file.write('---------------- Summary ----------------\n')
	file.write('Total subdomains checked: ' + str(num_total) + '\n')
	file.write('Total valid subdomains found : ' + str(num_valid) + '\n')
	file.write('Total invalid subdomains: ' + str(num_invalid) + '\n')
	
def main():
	count = 0
	count_valid = 0
	count_invalid = 0
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
						count_valid += 1
					else:
						pass
			except dns.resolver.NXDOMAIN:
				logException(subdoms, "NXDOMAIN", l)
				count_invalid += 1
				pass
			except dns.resolver.NoAnswer:
				logException(subdoms, "NoAnswer", l)
				count_invalid += 1
				pass
			except dns.resolver.Timeout:
				logException(subdoms, "Timeout", l)
				count_invalid += 1
				pass
			except KeyboardInterrupt:
				print("---------------- Keyboard interrupt detected - program killed ----------------")
				l.write("---------------- Keyboard interrupt detected - program killed ----------------\n")
				summarize(count, count_valid, count_invalid, l)
				quit()
			count += 1

	with open('log.txt', 'a') as l:
		summarize(count, count_valid, count_invalid, l)

main()
