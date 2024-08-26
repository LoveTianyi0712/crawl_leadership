from crawl.crawl_website_JX import crawl_website_JX
from insert_database import insert_leadership

if __name__ == '__main__':
    period = 7
    leadership_list = crawl_website_JX(period)
    insert_leadership(leadership_list)
