import re

class PhishingDetector:
    def __init__(self):
        # List of suspicious keywords
        self.suspicious_keywords = ['login', 'verify', 'secure', 'account', 'update', 'confirm', 'password']
        self.suspicious_domains = ['.xyz', '.club', '.top', '.gq', '.tk']
        self.blacklisted_domains = ['example.com', 'phishingsite.com']

    def check_url(self, url: str):
        """
        Check if the URL is suspicious or potentially a phishing attempt
        """
        # Check for suspicious keywords in the URL path
        for keyword in self.suspicious_keywords:
            if keyword in url:
                print(f"Suspicious keyword found in URL: {keyword}")
                return True

        # Check for suspicious domains in the URL
        for domain in self.suspicious_domains:
            if domain in url:
                print(f"Suspicious domain found: {domain}")
                return True

        # Check for blacklisted domains
        for blacklisted in self.blacklisted_domains:
            if blacklisted in url:
                print(f"Blacklisted domain found: {blacklisted}")
                return True

        # If none of the above checks are triggered, URL is considered safe
        return False

if __name__ == "__main__":
    # Example URLs for testing
    urls_to_check = [
        "http://example.com/secure-login",
        "https://phishingsite.com/verify-account",
        "http://mysite.xyz/confirm-update",
        "https://www.trusteddomain.com",
    ]

    detector = PhishingDetector()
    
    for url in urls_to_check:
        print(f"Checking URL: {url}")
        if detector.check_url(url):
            print("Phishing detected!\n")
        else:
            print("URL is safe.\n")
