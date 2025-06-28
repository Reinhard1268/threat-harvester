import geoip2.database

def geoip_lookup(ip):
    try:
        reader = geoip2.database.Reader("GeoLite2-City.mmdb")
        response = reader.city(ip)
        city = response.city.name or ""
        country = response.country.name or ""
        location = f"{city}, {country}".strip(", ")
        return {"location": location if location else "Unknown"}
    except Exception:
        return {"location": "Unknown"}

def fetch_abuse_data(ioc):
    known_abuse_ips = {
        "8.8.8.8": "High",
        "185.220.101.1": "Critical"
    }
    return known_abuse_ips.get(ioc, "N/A")
