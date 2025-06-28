import os
import json
from utils import geoip_lookup, fetch_abuse_data
from rich.console import Console
from tabulate import tabulate

console = Console()

def load_iocs(file_path):
    with open(file_path, 'r') as f:
        iocs = [line.strip() for line in f if line.strip()]
    return iocs

def classify_ioc(ioc):
    if ioc.count('.') == 3 and all(part.isdigit() for part in ioc.split('.') if part):
        return "IP"
    elif any(c in ioc for c in ['@', '.com', '.net', '.org']):
        return "Domain"
    elif len(ioc) in [32, 40, 64, 128]:
        return "Hash"
    else:
        return "Unknown"

def enrich_iocs(iocs):
    enriched = []
    for ioc in iocs:
        ioc_type = classify_ioc(ioc)
        geo = geoip_lookup(ioc)
        abuse = fetch_abuse_data(ioc)

        entry = {
            "Type": ioc_type,
            "Value": ioc,
            "Source": "User Input",
            "Threat": "Suspicious",
            "Location": geo.get("location", "Unknown"),
            "Abuse": abuse if abuse else "N/A"
        }
        enriched.append(entry)
    return enriched

def display_data(data):
    table = [[d["Type"], d["Value"], d["Source"], d["Threat"], d["Location"], d["Abuse"]] for d in data]
    console.print(tabulate(table, headers=["Type", "Value", "Source", "Threat", "Location", "Abuse"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    ioc_file = "iocs.txt"

    if not os.path.exists(ioc_file):
        print(f"[!] IOC file not found: {ioc_file}")
    else:
        console.print("[bold cyan]Threat Intel Harvester Starting...[/bold cyan]")
        iocs = load_iocs(ioc_file)
        enriched_data = enrich_iocs(iocs)
        display_data(enriched_data)

        # ✅ Save enriched IOCs for dashboard
        with open("enriched_iocs.json", "w") as f:
            json.dump(enriched_data, f, indent=4)
        print("[+] Enriched IOCs saved to enriched_iocs.json")
