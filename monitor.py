import time
from rss_client import RSSClient
from printer import IncidentPrinter

class StatusMonitor:
    #this class coordinates RSS fetching and printing new incidents
    def __init__(self, rss_url, interval=60):
        #initialize RSS client and monitoring interval
        self.rss_client = RSSClient(rss_url)
        self.interval = interval
        self.last_seen_id = None

    def check_for_update(self):
        #check RSS feed and print incident if new update is found
        entry = self.rss_client.get_latest_entry()

        if entry:
            current_id = entry.id

            if self.last_seen_id != current_id:
                IncidentPrinter.print_incident(entry)
                self.last_seen_id = current_id

    def start(self):
        #start continuous monitoring loop
        print("Monitoring OpenAI Status Page...\n")

        while True:
            self.check_for_update()
            time.sleep(self.interval)