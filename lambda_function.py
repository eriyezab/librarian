from librarian import send_to_kindle, download_epub
import urllib.parse

def lambda_handler(event, context):
    print("Received event: " + str(event))
    if "Body" not in event:
        print("Error - unexpected event: " + str(event))
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message><Body>Unexpected event. -Lambda</Body></Message></Response>"
    url = urllib.parse.unquote(event["Body"])
    try:
        filename, file_data = download_epub(url)
    except:
        print("Error - failed to download epub: " + str(event))
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message><Body>Error downloading epub. -Lambda</Body></Message></Response>"
    if not filename or not file_data:
        print("Error - failed to download epub: " + str(event))
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
           "<Response><Message><Body>Error downloading epub. -Lambda</Body></Message></Response>"
    else:
        try:
            send_to_kindle(filename, file_data)
            print("Success!")
            return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
                "<Response><Message><Body>Successful sent to kindle. -Lambda</Body></Message></Response>"
        except:
            print("Error - failed to email epub: " + str(event))
            return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"\
            "<Response><Message><Body>Error sending epub to kindle. -Lambda</Body></Message></Response>"
