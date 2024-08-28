import crawl
from utils.insert_database import insert_leadership


if __name__ == '__main__':
    period = 7
    leadership_list = crawl.crawl_website_NC(period)

    '''
    period = 7
    leadership_list = []
    leadership_list.extend(crawl.crawl_website_JX(period))
    leadership_list.extend(crawl.crawl_website_JJ(period))
    insert_leadership(leadership_list)
    print("Success!")
    '''