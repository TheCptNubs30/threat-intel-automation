import os
import requests
from dotenv import load_dotenv

# Load environment variables from the secure .env file
load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

# The endpoint URL for checking IP addresses via VirusTotal v3 API
BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

def analyze_ip(ip_address):
    """Queries the VirusTotal API to determine if an IP address is malicious."""
    if not API_KEY:
        print("[-] Error: Missing VirusTotal API Key in .env file.")
        return

    # Set up the secure authentication header required by the API
    headers = {
        "accept": "application/json",
        "x-apikey": API_KEY
    }

    print(f"\n[+] Querying VirusTotal for telemetry on: {ip_address}...")
    
    try:
        # Send a secure GET request to the threat intelligence database
        response = requests.get(f"{BASE_URL}{ip_address}", headers=headers)
        
        # If the request is successful (HTTP Status 200)
        if response.status_code == 200:
            data = response.json()
            
            # Extract the analysis results from the JSON payload
            stats = data['data']['attributes']['last_analysis_stats']
            malicious_count = stats['malicious']
            suspicious_count = stats['suspicious']
            harmless_count = stats['harmless']
            
            # --- INCIDENT TRIAGE LOGIC ---
            print("=========================================")
            print(f"📊 REPORT FOR IP: {ip_address}")
            print("=========================================")
            print(f"🔴 Malicious Flags: {malicious_count}")
            print(f"🟡 Suspicious Flags: {suspicious_count}")
            print(f"🟢 Clean/Harmless Flags: {harmless_count}")
            print("-----------------------------------------")
            
            # Automated alerting threshold based on industry standards
            if malicious_count > 0:
                print(f"🚨 ALERT: {ip_address} has been flagged as MALICIOUS by {malicious_count} security vendors!")
                print("[ACTION REQUIRED] Isolate endpoint and block this IP on the perimeter firewall.")
            else:
                print(f"✅ STATUS: {ip_address} appears clean. No malicious signatures detected.")
            print("=========================================\n")
            
        elif response.status_code == 401:
            print("[-] Error 401: Unauthorized. Please check your API key.")
        elif response.status_code == 404:
            print("[-] Error 404: Invalid IP address format.")
        else:
            print(f"[-] Error: Received unexpected status code {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"[-] Critical Error connecting to Threat Intel API: {e}")

if __name__ == "__main__":
    print("--- SOC Analyst Threat Intelligence Automation Tool ---")
    # Prompt the user for an IP address to parse
    target_ip = input("Enter an external IP address to analyze (e.g., 8.8.8.8): ").strip()
    analyze_ip(target_ip)