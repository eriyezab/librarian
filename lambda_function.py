from librarian import send_to_kindle, download_epub

def lambda_handler(event, context):
    print("Received event: " + str(event))
    url = event["Body"]
    filename = download_epub(url)
    if not filename:
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message><Body>Error downloading epub. -Lambda</Body></Message></Response>"
    else:
        try:
            send_to_kindle(filename)
            return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
                "<Response><Message><Body>Successful sent to kindle. -Lambda</Body></Message></Response>"
        except:
            return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
            "<Response><Message><Body>Error sending epub to kindle. -Lambda</Body></Message></Response>"
