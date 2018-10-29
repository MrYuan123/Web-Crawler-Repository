from bs4 import BeautifulSoup

class detail_analysis(object):
    def __init__(self):
        pass

    def detail_analysis(self, page_detail):
        soup = BeautifulSoup(page_detail,'lxml')
        return_data = dict()
        #=======================================
        #==== tags section
        #=======================================
        try:
            tagC = soup.find('div', class_ = 'tag')
            flag = 1
            tag_list = list()
            for item in tagC.span:
                if flag%2 != 0:
                    pass
                else:
                    soupT = BeautifulSoup(str(item),'lxml')
                    tag_list.append(soupT.get_text())
                flag+=1
            return_data['tags'] = tag_list
        except:
            return_data['tags'] = None

        #=======================================
        #==== intro section
        #=======================================
        intro = soup.find('div', id = "intro")
        return_data['intro'] = intro.text[:-11]

        #=======================================
        #==== infolist
        #=======================================
        infolist = soup.find('ul',class_ = 'infolist')
        soup2 = BeautifulSoup(str(infolist),'lxml')
        introdetail = soup2.find_all('li')

        return_data[introdetail[0].b.text] = '[' + introdetail[0].text.strip()[6:].replace('\n',',') + ']'

        return_data[introdetail[1].b.text] = introdetail[1].text.strip()[5:]

        return_data[introdetail[2].b.text] = introdetail[2].text.strip()[5:]

        #========================================
        #==== info detail
        #========================================
        info_list = soup.find_all('div', class_ = 'lbox catalogItem')
        info_details = dict()
        for item in info_list:
            if '相关疾病' in item.h3.text:
                soup3 = BeautifulSoup(str(item),'lxml')
                temp = list()
                for m in soup3.find_all('li'):
                    temp.append(m.text)
                info_details[item.h3.text] = temp
            elif '相关症状' in item.h3.text:
                soup3 = BeautifulSoup(str(item),'lxml')
                temp = list()
                for m in soup3.find_all('li'):
                    temp.append(m.text)
                info_details[item.h3.text] = temp
            else:
                info_details[item.h3.text] = item.text[len(item.h3.text) + 2:].strip()
        return_data['details'] = info_details
        return return_data
