from monitor import StatusMonitor
def main():
    #openAI status RSS feed URL
    rss_url = "https://status.openai.com/history.rss"

    #create monitor object
    monitor = StatusMonitor(rss_url, interval=60)

    #start monitoring
    monitor.start()

if __name__ == "__main__":
    main()