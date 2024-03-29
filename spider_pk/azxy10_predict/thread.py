#coding=utf-8
__author__ = 'shifeixiang'
import time
import threading
import datetime
import azxy10_predict.main

from pkten_log.pk_log import PkLog

pk_logger = PkLog('azxy10_predict.thread').log()

class Spider(threading.Thread):
    # __metaclass__ = Singleton
    thread_stop = False
    thread_num = 0
    interval = {}
    behavior = None
    def run(self):
        self.behavior(self,self.thread_num,self.interval)
    def stop(self):
        self.thread_stop = True

class ThreadControl():
    thread_stop = False
    current_thread = {}
    def start(self,thread_num,interval):
        spider = Spider()
        spider.behavior = loaddata
        spider.thread_num = thread_num
        spider.interval = interval
        spider.start()
        self.current_thread[str(thread_num)] = spider
    #判断进程是否活跃
    def is_alive(self,thread_num):
        tt = self.current_thread[str(thread_num)]
        return tt.isAlive()
    #获取当前线程名称
    # def get_name(self):
    def stop(self,thread_num):
        #print "stop"
        pk_logger.info("stop")
        spider = self.current_thread[str(thread_num)]
        spider.stop()

def loaddata(c_thread,thread_num,interval):
    base_date = time.strftime("%Y%m%d", time.localtime())
    count = 0
    #初次启动开始购买---可以通过购买记录来初始化last_minute
    last_minute = -1
    while not c_thread.thread_stop:
        flag_date = time.strftime("%H:%M:%S", time.localtime())
        # print "flag_date:",flag_date

        if flag_date >= '06:59:00' or flag_date <= "05:59:59":
            current_minute = (datetime.datetime.now()).minute
            current_hour = (datetime.datetime.now()).hour
            # print "current_minute ",current_minute
            if current_hour == 9 and current_minute < 9 and last_minute> 0:
                last_minute = -2
            if current_minute<5 and last_minute> 0:
                last_minute = -1
            if current_minute - last_minute > 3 or current_minute == 4 :

                judge_num = (current_minute%5)
                print "judge_num",judge_num
                if judge_num == 0 or judge_num == 4:
                    # if 1:
                    current_date = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
                    #print current_date
                    #print "start purchase"
                    azxy10_predict.main.spider_save_predict(interval)
                    # auto_visit.main.auto_visit_commit(interval)
                    last_minute = current_minute
                    if current_minute < 5:
                        time.sleep(120)
                    else:
                        time.sleep(3)
                    count = count + 1
                else:
                    # print current_minute, " ", last_minute," wait open prob"
                    time.sleep(10)
            else:
                # print current_minute, " ", last_minute," current prob already purchase"
                time.sleep(10)
        else:
            time.sleep(60)
    #print "exit!"
    pk_logger.info("exit")
    time.sleep(10)
    interval['driver'].quit()
