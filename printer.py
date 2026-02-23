from datetime import datetime
from bs4 import BeautifulSoup

class IncidentPrinter:
    #this class prints RSS incidents in clean readable format

    @staticmethod
    def clean_html(raw_html):
        """
        Parse HTML content and preserve line breaks.
        Convert <br> and <li> to newline for readability.
        """
        soup = BeautifulSoup(raw_html, "html.parser")

        #replace <br> with newline
        for br in soup.find_all("br"):
            br.replace_with("\n")

        #replace <li> with newline + dash
        for li in soup.find_all("li"):
            li.replace_with(f"\n- {li.get_text()}")

        #get clean text
        clean_text = soup.get_text()
        return clean_text.strip()

    @staticmethod
    def print_incident(entry):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        product = entry.title
        status = IncidentPrinter.clean_html(entry.summary)

        print(f"\n[{timestamp}]")
        print(f"Product: {product}")
        print(f"Status: {status}")