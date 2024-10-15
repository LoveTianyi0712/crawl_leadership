import time

import crawl
from utils.insert_database import insert_leadership
from Config import Config


if __name__ == '__main__':
    period = Config.CRAWL_PERIOD
    leadership_list = []

    print("开始爬取数据...")
    print("爬取江西省数据")
    leadership_list.extend(crawl.crawl_website_JX(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取江西省数据完成")

    print("爬取抚州市数据")
    leadership_list.extend(crawl.crawl_website_FZ(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取抚州市数据完成")

    print("爬取赣州市数据")
    leadership_list.extend(crawl.crawl_website_GZ(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取赣州市数据完成")

    print("爬取吉安市数据")
    leadership_list.extend(crawl.crawl_website_JA(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取吉安市数据完成")

    print("爬取景德镇市数据")
    # leadership_list.extend(crawl.crawl_website_JDZ(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取景德镇市数据完成")

    print("爬取九江市数据")
    leadership_list.extend(crawl.crawl_website_JJ(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取九江市数据完成")

    print("爬取南昌市数据")
    leadership_list.extend(crawl.crawl_website_NC(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取南昌市数据完成")

    print("爬取萍乡市数据")
    # leadership_list.extend(crawl.crawl_website_PX(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取萍乡市数据完成")

    print("爬取上饶市数据")
    leadership_list.extend(crawl.crawl_website_SR(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取上饶市数据完成")

    print("爬取新余市数据")
    leadership_list.extend(crawl.crawl_website_XY(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取新余市数据完成")

    print("爬取宜春市数据")
    leadership_list.extend(crawl.crawl_website_YC(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取宜春市数据完成")

    print("爬取鹰潭市数据")
    # leadership_list.extend(crawl.crawl_website_YT(period))
    time.sleep(Config.TIME_INTERVAL)
    print("爬取鹰潭市数据完成")

    print("正在插入数据")
    insert_leadership(leadership_list)
    print("数据插入完成")
