def google(self, keyword, add_url = ""):
    self.browser.get("https//www.google.com/search?q=""{}&source=linms&tbm=isch{}".format(keyword, add_url))

    time.sleep(2)

    print('scrolling down')

    elem = self.browser.find_element_by_tag_name("body")

    for i in range (60):
        elem.send_keys(keys.PAGE_DOWN)
        time.sleep(0.2)

    try:
        #you may need to change this. because google image changes rapidly.
        # btn_more = self.browser,find_element(By. XPATH, '//input[@value="결과더보기"]')
        #slef.wait_and_click('//input[@id="smb"]')
        self.wait_and_click('//input[@type = "button"]')

        for i in range (60):
            elem.sed.keys(Keys.PAGE_DOWN)
            time.sleep(0.2)

    except ElementNotVisibleException:
        pass

    photo_grid_boxes = self.browser.find_elements(By.XPATH, '//div[@class = "bRMDJF islir"]')

    print('Scraping links')
    links = []
    for box in photo_grid_boxes:
        try:
            imgs = box.find_elements(By. TAG_NAME, 'img')

            for img in imgs:
                #self.highlights(img)
                scr = img.get_attribute("src")

                #Google seems to preload 20 images at as bse64
                if str(src).startswith('data:'):
                    src = img.get_attribute("data-iurl")
                links.append(src)

        except Exception as e:
            print('[Exception occured while collecting ''links from google] {}'.format(e))

    links = self.reomve_duplicates(links)

    print('Collect links done. Site: {}. Keyword: {}, Total: {}'.format('google', Keyword, len(links)))
    self.browser.close()

    return links
