import requests

def get_domain_score(domain, api_key):
    """
    Fetch the VirusTotal reputation score for a given domain.
    
    :param domain: Domain name to check (e.g., "example.com")
    :param api_key: Your VirusTotal API key
    :return: Dictionary with harmless, malicious, suspicious, and undetected counts
    """
    url = f"https://www.virustotal.com/api/v3/domains/{domain}"
    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Extract reputation stats
        stats = data['data']['attributes']['last_analysis_stats']

        print(f"\n🔍 Domain: {domain}")
        print(f"🟢 Harmless:   {stats['harmless']}")
        print(f"🔴 Malicious:  {stats['malicious']}")
        print(f"🟠 Suspicious: {stats['suspicious']}")
        print(f"⚪ Undetected: {stats['undetected']}")
        
        # Simple scoring logic
        score = stats['harmless'] - (stats['malicious'] + stats['suspicious'])
        print(f"\n⭐ Domain Score: {score}")

        return stats

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    api_key = "YOUR_VIRUSTOTAL_API_KEY"
    domain = "example.com"  # Replace with the domain you want to check
    get_domain_score(domain, api_key)
