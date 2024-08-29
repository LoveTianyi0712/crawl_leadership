import time

import crawl
from utils.insert_database import insert_leadership


if __name__ == '__main__':
    period = 7
    leadership_list = []

    leadership_list.extend(crawl.crawl_website_JX(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_FZ(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_GZ(period))
    time.sleep(20)

    # leadership_list.extend(crawl.crawl_website_JA(period))
    time.sleep(20)

    # leadership_list.extend(crawl.crawl_website_JDZ(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_JJ(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_NC(period))
    time.sleep(20)

    # leadership_list.extend(crawl.crawl_website_PX(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_SR(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_XY(period))
    time.sleep(20)

    leadership_list.extend(crawl.crawl_website_YC(period))
    time.sleep(20)

    # leadership_list.extend(crawl.crawl_website_YT(period))
    time.sleep(20)

    insert_leadership(leadership_list)
    print("Success!")