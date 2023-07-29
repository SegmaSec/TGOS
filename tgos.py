from colorit import *
init_colorit()
import requests
import argparse
import threading

#Colors code
ORANGE=255, 165, 0
GREEN=0, 255, 0
RED=255,0,0
YELLOW=255, 255, 0
PURPLE=148,0,211
DEEPPINK=255,20,147
CYAN=0,238,238
WHITE=255, 255, 255
print(color("""
                ████████╗ ██████╗  ██████╗ ███████╗      ██████╗  ██████╗ ██████╗ ██████╗ 
                ╚══██╔══╝██╔════╝ ██╔═══██╗██╔════╝      ╚════██╗██╔═████╗╚════██╗╚════██╗
                   ██║   ██║  ███╗██║   ██║███████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝
                   ██║   ██║   ██║██║   ██║╚════██║╚════╝██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗
                   ██║   ╚██████╔╝╚██████╔╝███████║      ███████╗╚██████╔╝███████╗██████╔╝
                   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝      ╚══════╝ ╚═════╝ ╚══════╝╚═════╝                                                                         
		                                                             "By: SegmaSec" """,(WHITE)))
print(color("		        [~]",(WHITE)) + color(" The Best Tools For Brute Forcing Subdomain!!!",(CYAN)))
print(color("		        [~]",(WHITE)) + color(" Usage: python3 tgos.py -u <url> -w <wordlist> -m HEAD -t 100",(CYAN)))
print(color("				--------------",(CYAN))+color("Social Media",(WHITE))+color("---------------",(CYAN)))
print(color("				|                                       |",(CYAN)))
print(color("				|",(CYAN))+color("  https://discord.gg/alx-segmasec      ",(ORANGE))+color("|",(CYAN)))
print(color("				|",(CYAN))+color("  https://github.com/SegmaSec          ",(ORANGE))+color("|",(CYAN)))
print(color("				|_______________________________________|\n",(CYAN)))


def check_subdomain(subdomain, domain, method):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.request(method, url)
        if response.status_code == 200:
            print(color(f"[+] Subdomain found:",(WHITE))+color(" {}".format(url),(GREEN)))
    except requests.ConnectionError:
        pass

def brute_force_subdomains(domain, subdomains_list, method, num_threads):
    threads = []
    for subdomain in subdomains_list:
        thread = threading.Thread(target=check_subdomain, args=(subdomain, domain, method))
        thread.start()
        threads.append(thread)

        # Limit the number of concurrent threads to the specified number
        if len(threads) >= num_threads:
            for t in threads:
                t.join()
            threads.clear()

    # Wait for the remaining threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute Force Subdomains")
    parser.add_argument("-u", "--target", help="Target domain to check for subdomains", required=True)
    parser.add_argument("-w", "--wordlist", help="Wordlist containing subdomains to check", required=True)
    parser.add_argument("-m", "--method", help="HTTP method for requests (GET or HEAD)", default="GET")
    parser.add_argument("-t", "--threads", help="Number of threads for multithreading", type=int, default=10)
    args = parser.parse_args()

    target_domain = args.target
    with open(args.wordlist, "r") as file:
        subdomains = [line.strip() for line in file]

    brute_force_subdomains(target_domain, subdomains, args.method.upper(), args.threads)
