#coding=utf-8
__author__ = 'shifeixiang'

# from __future__ import unicode_literals

from selenium import webdriver
import time

from pkten_log.pk_log import PkLog

pk_logger = PkLog('xyft_purchase_wow.purchase_driver').log()

def get_driver(username,password):
    #谷歌
    chromedriver = "./pkten_log/chromedriver37.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
    driver = webdriver.Chrome(executable_path=chromedriver,chrome_options=options )
    #狐火
    # driver = webdriver.Firefox(executable_path = './pkten_log/geckodriver.exe')
    code_flag = True
    while(code_flag):
        try:
            # 进入地址
            driver.get("http://www.m1888.net")
            time.sleep(3)
            # 搜索号码
            driver.find_element_by_id("LoginCodeId").send_keys("406923")
            time.sleep(2)
            driver.find_element_by_id("submit2").click()
            pk_logger.info("select lines")
            time.sleep(3)
            # 选择线路
            driver.find_element_by_xpath('//*[@id="ultest"]/div[5]/div[1]/a[1]').click()
            time.sleep(3)
            # 最大化
            driver.maximize_window();
            pk_logger.info("switch to mem_index")
            time.sleep(2)
            # 切换到框架
            driver.switch_to.frame("mem_index")
            time.sleep(2)

            user_elem = driver.find_element_by_name("Account")
            user_elem.send_keys(username)

            pwd_elem = driver.find_element_by_name("PassWD")
            pwd_elem.send_keys(password)

            pk_logger.info("click commit")
            button = driver.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div/div/ul/div[4]')
            button.click()
            time.sleep(2)

            pk_logger.info("click agree")
            agree = driver.find_element_by_name("Submit2")
            agree.click()
            time.sleep(2)
            code_flag = False
        except:
            driver.quit()
            pk_logger.warn("启动过程失败，重新启动...")
            time.sleep(5)
            code_flag = True
    time.sleep(1)

    #点击广告
    try:
        driver.find_element_by_xpath('//*[@id="toclose"]').click()
        time.sleep(1)
    except:
        pk_logger.warn("unfound button1")

    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]').click()
        time.sleep(1)
    except:
        pk_logger.warn("unfound button2")

    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]').click()
        time.sleep(1)
    except:
        pk_logger.warn("unfound button3")

    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]').click()
        time.sleep(1)
    except:
        pk_logger.warn("unfound button4")

    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]').click()
        time.sleep(1)
    except:
        pk_logger.warn("unfound button5")

    #返回原始框架
    pk_logger.info("return frame")
    driver.switch_to.default_content()
    pk_logger.info("switch mem_index")
    time.sleep(1)
    #切换到mem_index
    driver.switch_to.frame("mem_index")
    pk_logger.info("click caipiao dating")
    time.sleep(1)

    #彩票大厅
    # try:
    #     pk_logger.info("click caipiao dating 2")
    #     driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/a[2]').click()
    # except:
    #     pk_logger.info("click caipiao dating 1")
    #     driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/a[2]').click()
    # #driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/a[2]').click()
    #
    # #切换到mainFrame
    # pk_logger.info("switch mainFrame ")
    # time.sleep(1)
    # driver.switch_to.frame("mainFrame")
    # pk_logger.info("click xyft ")
    # #点击幸运飞艇
    # time.sleep(1)
    # xyft = driver.find_element_by_xpath('//*[@id="gametable"]/table/tbody/tr[4]/td[2]/a[3]')
    # xyft.click()
    #
    # #先回默认iframe,在逐层切换到IndexFrame
    # pk_logger.info("switch IndexFrame ")
    # time.sleep(1)

    dating_flag = True
    while (dating_flag):
        try:
            pk_logger.info("click caipiao dating 2")
            driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/a[2]').click()
        except:
            pk_logger.info("click caipiao dating 1")
            driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/a[2]').click()
        # driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/a[2]').click()

        # 切换到mainFrame
        pk_logger.info("switch mainFrame ")
        time.sleep(1)
        driver.switch_to.frame("mainFrame")
        pk_logger.info("click xyft ")
        # 点击幸运飞艇
        time.sleep(2)
        try:
            xyft = driver.find_element_by_xpath('//*[@id="gametable"]/table/tbody/tr[4]/td[2]/a[3]')
            xyft.click()
            dating_flag = False
        except:
            pk_logger.error("click xyft faild!")
            time.sleep(3)
            pk_logger.info("return frame")
            driver.switch_to.default_content()
            pk_logger.info("switch mem_index")
            time.sleep(1)
            # 切换到mem_index
            driver.switch_to.frame("mem_index")
            pk_logger.info("click caipiao dating")
            time.sleep(1)

    # 先回默认iframe,在逐层切换到IndexFrame
    pk_logger.info("switch IndexFrame ")
    time.sleep(1)

    # 1-10
    try:
        driver.switch_to.default_content()
        driver.switch_to.frame("mem_index")
        time.sleep(1)
        driver.switch_to.frame("mainFrame")
        time.sleep(1)
        driver.switch_to.frame("IndexFrame")
    except:
        pk_logger.info("not found IndexFrame")

    #切到1-10号码盘
    pk_logger.info("click 1-10 ")
    time.sleep(1)
    element_1_10 = driver.find_element_by_xpath('//*[@id="NUMERIC"]/a')
    element_1_10.click()
    time.sleep(1)

    #测试购买
    # pk_logger.info("send_keys")
    # driver.find_element_by_xpath('//*[@id="NUM-N0102-TEXT"]').send_keys(str(2))
    # driver.find_element_by_xpath('//*[@id="NUM-N0103-TEXT"]').send_keys(str(2))
    # driver.find_element_by_xpath('//*[@id="NUM-N0104-TEXT"]').send_keys(str(2))
    # driver.find_element_by_xpath('//*[@id="NUM-N0105-TEXT"]').send_keys(str(2))
    #
    # #确认
    # pk_logger.info("click confirm")
    # time.sleep(1)
    # confirm_button = driver.find_element_by_xpath('//*[@id="BetType-NUMERIC"]/div/input[2]')
    # confirm_button.click()
    # pk_logger.info("click submit")
    # time.sleep(1)
    #
    # #提交
    #
    # submit_button = driver.find_element_by_xpath('//*[@id="submitbtn"]')
    # submit_button.click()
    # pk_logger.info("purchase ok ")
    # time.sleep(5)

    return driver

