import ast
import feedparser

LOG_FILE = 'feed.log'
LINK_RSS_FEED = 'https://www.cert.ssi.gouv.fr/alerte/feed'

def recover_old_info(LOG_FILE):
    with open(LOG_FILE, 'r', encoding='utf-8') as file:
        content = file.read()
    return ast.literal_eval(content)

def get_info(LINK_RSS_FEED):
    data = feedparser.parse(LINK_RSS_FEED)
    info = []
    for entry in data.entries:
        inf = f"{entry.title}\n{entry.description}\n{entry.link}\n{entry.published}"
        info.append(inf)
    return info

def get_diff(info_old, info):
    new_information = []
    for element in info:
        if element not in info_old:
            new_information.append(element)
    return new_information

def save_log(info):
    with open(LOG_FILE, "w+", encoding="utf-8") as log:
        log.write(str(info))
    return 0

def display_information(information):
    for inf in information:
        print(inf)
    return 0

def main():
    info_old = recover_old_info(LOG_FILE)
    info = get_info(LINK_RSS_FEED)
    new_information = get_diff(info_old, info)
    display_information(new_information)

    if new_information != []:
        save_log(info)
    
    return 0

if __name__ == '__main__':
    main()
