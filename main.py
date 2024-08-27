import crawl
from utils.insert_database import insert_leadership
from utils.ai_processing import ai_processing

if __name__ == '__main__':
    period = 70
    leadership_list = crawl.crawl_website_JJ(period)
    for leadership in leadership_list:
        print(leadership.to_dict())

    '''
    period = 7
    leadership_list = crawl.crawl_website_JX(period)
    insert_leadership(leadership_list)
    print("Success!")
    '''