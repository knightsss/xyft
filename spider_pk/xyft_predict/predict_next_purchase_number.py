#coding=utf-8
__author__ = 'shifeixiang'


import time
from selenium import webdriver
from bs4 import BeautifulSoup
from append_predict.models import KillPredict

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xyft_predict.models import PredictLottery

import datetime

from pkten_log.pk_log import PkLog
pk_logger = PkLog('append_predict.predict_append_rule_100_continue5').log()
#获取predict driver
def spider_predict_selenium():

    driver_flag = True
    while(driver_flag):
        # driver = webdriver.Firefox(executable_path = './pkten_log/geckodriver.exe')

        chromedriver = "./pkten_log/chromedriver37.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

        driver.get("https://www.1399p.com/pk10/shdd")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "lotteryNumber")))
            driver_flag = False
            return driver
        except:
            print "get driver time out"
            driver.quit()
            time.sleep(10)


def get_purchase_list(interval):
    current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    lotterys = PredictLottery.objects.filter(lottery_date=current_date).order_by("-lottery_id")
    current_count = 0

    #[1|2|3, 7|8, 10|2]
    mingci_predict_numbers_list = [0 for i in range(10)]
    mingci_predict_numbers_2bit_list = [0 for i in range(10)]
    predict_mingci_len_list = [0 for i in range(10)]
    for lottery in lotterys:
        if current_count == 0:
            protty_id = lottery.lottery_id + 1
            kaijiang_number_list = lottery.lottery_number.split(',')
            print "kaijiang_number_list1:",kaijiang_number_list
            for i in range(10):
                mingci_predict_numbers_list[i] = str(int(kaijiang_number_list[i])) + '|'
                mingci_predict_numbers_2bit_list[i] = kaijiang_number_list[i] +  '|'
                predict_mingci_len_list[i] = 1
        else:

            kaijiang_number_list = lottery.lottery_number.split(',')
            print "kaijiang_number_list2:", kaijiang_number_list
            for i in range(10):
                #if  str(int(kaijiang_number_list[i])) in mingci_predict_numbers_list[i]:
                if kaijiang_number_list[i] in mingci_predict_numbers_2bit_list[i]:
                    pass
                else:
                    if predict_mingci_len_list[i] < 6:
                        mingci_predict_numbers_list[i] = mingci_predict_numbers_list[i] + str(int(kaijiang_number_list[i])) + '|'
                        mingci_predict_numbers_2bit_list[i] = mingci_predict_numbers_2bit_list[i] + kaijiang_number_list[i] + '|'
                        predict_mingci_len_list[i] = predict_mingci_len_list[i] + 1
                    elif predict_mingci_len_list[i] == 6:
                        mingci_predict_numbers_list[i] = mingci_predict_numbers_list[i] + str(int(kaijiang_number_list[i]))
                        mingci_predict_numbers_2bit_list[i] = mingci_predict_numbers_2bit_list[i] + kaijiang_number_list[i]
                        predict_mingci_len_list[i] = predict_mingci_len_list[i] + 1
                    else:
                        pass
        current_count = current_count + 1
        if min(predict_mingci_len_list) == 7:
            break
    if min(predict_mingci_len_list) < 7:
        last_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        lotterys = PredictLottery.objects.filter(lottery_date=last_date).order_by("-lottery_id")
        for lottery in lotterys:
            if len(mingci_predict_numbers_list) == 0:
                protty_id = lottery.lottery_id + 1
                kaijiang_number_list = lottery.lottery_number.split(',')
                for i in range(10):
                    mingci_predict_numbers_list[i] = str(int(kaijiang_number_list[i])) + '|'
                    mingci_predict_numbers_2bit_list[i] = kaijiang_number_list[i] + '|'
                    predict_mingci_len_list[i] = 1
            else:
                kaijiang_number_list = lottery.lottery_number.split(',')
                for i in range(10):
                    #判断在第n名，该数字是否出现过
                    print "22222kaijiang_number_list:",kaijiang_number_list[i]
                    print "mingci_predict_numbers_2bit_list:", mingci_predict_numbers_2bit_list[i]
                    if kaijiang_number_list[i] in mingci_predict_numbers_2bit_list[i]:
                    #if str(int(kaijiang_number_list[i])) in mingci_predict_numbers_list[i]:
                        pass
                    else:
                        #判断个数是否小于7个，否则已经满足7个的条件
                        if predict_mingci_len_list[i] < 6:
                            mingci_predict_numbers_list[i] = mingci_predict_numbers_list[i] + str(int(kaijiang_number_list[i])) + '|'
                            mingci_predict_numbers_2bit_list[i] = mingci_predict_numbers_2bit_list[i] + \
                                                                  kaijiang_number_list[i] + '|'
                            predict_mingci_len_list[i] = predict_mingci_len_list[i] + 1
                        elif predict_mingci_len_list[i] == 6:
                            mingci_predict_numbers_list[i] = mingci_predict_numbers_list[i] + str(
                                int(kaijiang_number_list[i]))
                            mingci_predict_numbers_2bit_list[i] = mingci_predict_numbers_2bit_list[i] + \
                                                                  kaijiang_number_list[i]
                            predict_mingci_len_list[i] = predict_mingci_len_list[i] + 1
                        else:
                            pass
            if min(predict_mingci_len_list) == 7:
                break

    index_count = 1
    for i in range(10):
        if str(index_count) not in interval["rule_id_list"]:
            mingci_predict_numbers_list[i] = '0'
        index_count = index_count + 1

    purchase_number_list =  ",".join(mingci_predict_numbers_list)
    purchase_number_list_desc = purchase_number_list
    save_predict_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print "purchase_number_list",purchase_number_list

    # if len(purchase_number.split('|')) < 7:
    #     purchase_number = '0'
    # if count == len(soup_list) - 1:
    #     purchase_number_list = purchase_number_list + str(purchase_number)
    #     purchase_number_list_desc = purchase_number_list_desc + '[' + str(purchase_number) + ']'
    # else:
    #     purchase_number_list = purchase_number_list + str(purchase_number) + ','
    #     purchase_number_list_desc = purchase_number_list_desc + '[' + str(purchase_number) + ']---,'

    return protty_id, purchase_number_list, purchase_number_list_desc

def get_last_number_predict_kill_result(protty_id,index):
    last_protty_id = int(protty_id) - 1
    try:
        p = KillPredict.objects.get(lottery_id=last_protty_id)
        number_all_list = p.predict_number_all.split(',')[index]
        number_hit = str(int(p.lottery_number.split(',')[index]))
        #print "number_hit,number_all_list ",number_hit,number_all_list
        pk_logger.info("number_hit:%s", number_hit)
        pk_logger.info("number_all_list:%s", number_all_list)
        if number_hit in number_all_list:
            # print "no kill all"
            return False
        else:
            # print "kill all"
            return True
    except:
        #print "kill error"
        pk_logger.info("kill error")
        return False

