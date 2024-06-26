import re
import time
import argparse
from core import Honeyscanner

def print_ascii_art_honeyscanner():
    message = r"""
    Vulnerability Assessment Initiated!
        """
    print(message)

def sanitize_string(s):  
    s = s.strip()  
    s = s.lower()  
    # Remove special characters using regex (it matches any character that is not a lowercase letter, a number, a space, a dot, an underscore, or a hyphen and removes it.)  
    s = re.sub('[^a-z0-9._\- ]', '', s)  
    return s  

def parse_arguments():
    parser = argparse.ArgumentParser(description="Honeyscanner: A vulnerability analyzer for honeypots")
    parser.add_argument(
        "--honeypot",
        type=sanitize_string,
        required=True,
        choices=["cowrie", "kippo", "dionaea", "conpot"],
        help="Honeypot to analyze, currently supported: (cowrie, kippo, dionaea and conpot)",
    )
    parser.add_argument(
        "--honeypot_version",
        type=sanitize_string,
        required=True,
        help="The version of the honeypot to analyze",
    )
    parser.add_argument(
        "--target_ip",
        type=sanitize_string,
        required=True,
        help="The IP address of the honeypot to analyze",
    )
    parser.add_argument(
        "--port",
        type=int,
        required=True,
        help="The port to connect to the honeypot to analyze",
    )
    parser.add_argument(
        "--username",
        type=str,
        required=False,
        help="The username to connect to the honeypot",
    )
    parser.add_argument(
        "--password",
        type=str,
        required=False,
        help="The password to connect to the honeypot",
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    print_ascii_art_honeyscanner()
    honeyscanner = Honeyscanner(args.honeypot, args.honeypot_version, args.target_ip, args.port, args.username, args.password)

    sleep_time = 0
    print(f"Starting in {sleep_time} seconds...")
    time.sleep(sleep_time)
    honeyscanner.run_all_attacks()  
    honeyscanner.generate_evaluation_report()  

    

if __name__ == "__main__":
    main()