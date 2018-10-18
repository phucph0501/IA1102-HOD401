import censys.certificates
import socket
import sys
import subprocess

ans = True
while ans:
    print("""
    +++ Menu +++
    1.Check Subdomain with Censys
    2.Check Subdomain with list keyword
    3.Check Subdomain with Censys and list keyword
    4.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        domain = input("Enter Domain: ")
        UID = "83f1de21-5e60-4c6a-8bb1-6afb3617aa6d"
        SECRET = "WVHec4SvOQTBuBZMZpQwVHrjSHABSiS1"

        certificates = censys.certificates.CensysCertificates(UID, SECRET)
        sub = 'parsed.names: %s' % domain
        cert_search_results = certificates.search(sub, fields=['parsed.names'])
        subdomains = []
        for c in cert_search_results:
            subdomains.extend(c['parsed.names'])


        def RemoveDuplication(subdomains):
            final_list = []
            for text in subdomains:
                if text not in final_list:
                    final_list.append(text)
            return final_list


        print("=" * 60)
        for dns in RemoveDuplication(subdomains):
            if domain in dns:
                print(dns)
        print("=" * 60)
    elif ans == "2":
        domain = input("Enter Domain: ")
        with open("names.txt") as file:
            content = file.readlines()
        content = [x.strip() for x in content]
        a = 0
        for content[a] in content:

            add = content[a] + "." + domain
            res = subprocess.call(['ping', '-c', '1', add])
            if res == 0:
                print("Sub Domain: ", add)
                print("=" * 60)
            a += 1
    elif ans == "3":
        domain = input("Enter Domain: ")
        UID = "83f1de21-5e60-4c6a-8bb1-6afb3617aa6d"
        SECRET = "WVHec4SvOQTBuBZMZpQwVHrjSHABSiS1"

        certificates = censys.certificates.CensysCertificates(UID, SECRET)
        sub = 'parsed.names: %s' % domain
        cert_search_results = certificates.search(sub, fields=['parsed.names'])
        subdomains = []
        for c in cert_search_results:
            subdomains.extend(c['parsed.names'])

        with open("names.txt") as file:
            content = file.readlines()
        content = [x.strip() for x in content]
        a = 0
        for content[a] in content:

            add = content[a] + "." + domain
            res = subprocess.call(['ping', '-c', '1', add])
            if res == 0:
                subdomains.append(add)
            a += 1


        def RemoveDuplication(subdomains):
            final_list = []
            for text in subdomains:
                if text not in final_list:
                    final_list.append(text)
            return final_list


        print("=" * 60)
        for dns in RemoveDuplication(subdomains):
            if domain in dns:
                print(dns)
        print("=" * 60)
    elif ans == "4":
        sys.exit()
    elif ans != "":
        print("\n Not Valid Choice Try again")
