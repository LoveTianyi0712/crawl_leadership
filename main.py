from crawl_website import crawl_website

if __name__ == '__main__':
    period = 7
    leadership_list = crawl_website(period)
    for leadership in leadership_list:
        print(leadership.to_dict())
