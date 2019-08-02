# -*- coding: utf-8 -*-
__author__ = 'shifeixiang'

from django.views.decorators.csrf import csrf_exempt    #用于处理post请求出现的错误
from django.shortcuts import render_to_response

from append_predict_sandd.models import ProbUser
from append_predict_sandd.models import KillPredict,PredictLottery
from append_predict_sandd.thread import ThreadControl
from append_predict_sandd.predict_append_rule import spider_predict_selenium,get_purchase_list_sandd
from append_predict_sandd.spider_pk10 import get_html_result,get_lottery_id_number,load_lottery_predict

import time
import datetime
import math

from pkten_log.pk_log import PkLog
pk_logger = PkLog('append_predict_sandd.main').log()

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class SingleDriver(Singleton):
    # def __init__(self, driver):
    #   self.driver = driver
    def get_driver(self):
        return self.driver
    def set_driver(self, driver):
        self.driver = driver

class SingleDriverMultiple(Singleton):
    # def __init__(self, driver):
    #   self.driver = driver
    def get_driver(self):
        return self.driver
    def set_driver(self, driver):
        self.driver = driver

#主页面
def predict_main(request):
    # ProbTotals.objects.all().delete()
    # thread_list =  ProbUser.objects.get(thread_name=th_name)
    prob_user_list =  ProbUser.objects.all()
    for prob_user in prob_user_list:
        c  = ThreadControl()
        try:
            #查看是否处于活跃状态
            status = c.is_alive(prob_user.user_name)
            if status:
                #设置状态为1
                prob_user.user_status = 1
                prob_user.save()
            else:
                #设置状态为0
                prob_user.user_status = 0
                prob_user.save()
        except:
            #print prob_user.user_name, " not start"
            pk_logger.info("%s not start",prob_user.user_name)
            prob_user.user_status = 0
            prob_user.save()
    return render_to_response('append_predict_sandd_main.html',{"prob_user_list":prob_user_list})


@csrf_exempt   #处理Post请求出错的情况
def control_predict_thread(request):
    user_name = request.POST['user_name']
    control = request.POST['control']
    info_dict = {}

    #显示活跃状态
    prob_user = ProbUser.objects.get(user_name=user_name)
    if control == 'start':
        # driver = spider_predict_selenium()
        # info_dict["driver"] = driver
        #状态信息
        c  = ThreadControl()
        #出现错误，则线程不存在，因此启动线程
        try:
            status = c.is_alive(user_name)
            #print "thread is alive? ",status
            pk_logger.debug("thread is alive? %s",status)
            if status:
                #print "thread is alive,caonot start twice!"
                pk_logger.debug("thread is alive,caonot start twice!")
            else:
                #print "start ..........thread1"
                pk_logger.debug("start ..........thread1")
                c.start(user_name, info_dict)
        except:
            #print "thread is not alive start!!!"
            pk_logger.debug("thread is not alive start!!!")
            c.start(user_name, info_dict)
        prob_user.user_status = 1
        prob_user.save()
    if control == 'stop':
        c  = ThreadControl()
        try :
            c.stop(user_name)
            prob_user.user_status = 0
            prob_user.save()
        except:
            pk_logger.debug("not thread alive")
            #print "not thread alive"
    prob_user_list =  ProbUser.objects.all()
    return render_to_response('append_predict_sandd_main.html',{"prob_user_list":prob_user_list})



def spider_save_predict(interval):
    time.sleep(10)
    #爬取当天结果,存入objects
    html_json = get_html_result()
    if html_json == '':
        pass
    else:
        load_lottery_predict(html_json)

        #获取models predict最新值
        lottery_id, kill_predict_number, xiazhu_money, xiazhu_beishu_str  = get_predict_model_value()
        pk_logger.debug("lottery_id: %s",lottery_id)
        #print "lottery_id",lottery_id
        if lottery_id == 0:
            #print "no predict record in history"
            pk_logger.debug("no predict record in history")
            last_purchase_hit = True
            xiazhu_nums = 1
            get_predict_kill_and_save(interval)
        else:
            #获取该期的开奖号码
            lottery_num,lottery_time = get_lottery_id_number(lottery_id)
            #print "lottery_num:",lottery_num
            pk_logger.info("lottery_num: %s",lottery_num)
            if (lottery_num):
                #计算命中率并更新models
                #print "save lottery_number"
                last_purchase_hit,xiazhu_nums = calculate_percisoin(lottery_id, lottery_num, kill_predict_number, lottery_time, xiazhu_money, xiazhu_beishu_str)
                pk_logger.info("last_purchase_hit: %s",last_purchase_hit)
                pk_logger.info("xiazhu_nums: %s",xiazhu_nums)
                get_predict_kill_and_save(interval)
            else:
                #print "pay interface lottery id request faild. continue...."
                pk_logger.error("pay interface lottery id request faild. continue....")
                time.sleep(10)
                spider_save_predict(interval)
                
    #get_predict_kill_and_save(interval)

def get_predict_kill_and_save(interval):
    #爬取下一期predict
    predict_lottery_id, purchase_number_list, beishu_number_list, purchase_number_list_str, beishu_number_list_str = get_purchase_list_sandd()
    if predict_lottery_id != 0:
        #更新models
        #print "save:",predict_lottery_id,'  ',purchase_number_list
        pk_logger.info("save predict_lottery_id : %s",predict_lottery_id)
        pk_logger.info("save purchase_number_list : %s", purchase_number_list)
        pk_logger.info("save beishu_number_list : %s", beishu_number_list)
        #current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

        #根据时间判断日期是否加一天
        jump_flag_date = time.strftime("%H:%M:%S", time.localtime())
        if jump_flag_date > '23:57:59' or jump_flag_date <= '00:03:00':
            current_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        save_predict_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #保存
        p = KillPredict(kill_predict_date=current_date, save_predict_time=save_predict_time, lottery_id = int(predict_lottery_id),
                        kill_predict_number = purchase_number_list_str,kill_predict_number_desc='', percent_all_list_desc='',
                            predict_total=0, target_total=0, predict_accuracy=0,
                            predict_number_all='', xiazhu_money=0,xiazhu_beishu=beishu_number_list_str,
                            gain_money=0, is_xiazhu=0, input_money=0, xiazhu_nums=0)
        p.save()



#获取最新一期的预测值得相关信息
def get_predict_model_value():
    current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    predicts = KillPredict.objects.filter(kill_predict_date=current_date).order_by("-lottery_id")
    lottery_id = 0
    kill_predict_number = 0
    xiazhu_money = 0
    xiazhu_beishu_str = ''
    if len(predicts) == 0:
        #print "predicts is null"
        pk_logger.debug("predicts is null")
    else:
        lottery_id = predicts[0].lottery_id
        kill_predict_number = predicts[0].kill_predict_number
        xiazhu_money = predicts[0].xiazhu_money
        xiazhu_beishu_str = predicts[0].xiazhu_beishu
    return lottery_id, kill_predict_number, xiazhu_money, xiazhu_beishu_str


def calculate_percisoin(lottery_id, lottery_num, kill_predict_number, lottery_time, xiazhu_money, xiazhu_beishu_str):
    #lottery_num 转数组，kill_predict_number 转二位数组
    result_data = lottery_num.split(',')

    purchase_number_list = []
    all_beishu_count = 0
    xiazhu_beishu_list = xiazhu_beishu_str.split(',')
    for elet in kill_predict_number.split(','):
        tmp_list = elet.split('|')
        purchase_number_list.append(tmp_list)

    if len(result_data) == len(purchase_number_list):
        all_count = 0
        target_count = 0
        for i in range(len(result_data)):
            pk_logger.debug("mingci [%d]: %s",(i+1),str(int(result_data[i])))
            pk_logger.debug("purchase_number_list[i]: %s",purchase_number_list[i][0])
            if int(xiazhu_beishu_list[i]) != 0:
                if int(result_data[i])%2 == int(purchase_number_list[i][0]):
                    target_count = target_count +  1

                all_beishu_count = all_beishu_count + int(xiazhu_beishu_list[i])
                all_count = all_count + len(purchase_number_list[i])
        pk_logger.debug("------all_count: %d  ----target_count: %d ",all_count,target_count)
        if all_count == 0:
            predict_accuracy = 0
            gain_money = 0
        else:
            predict_accuracy = float(float(target_count)/float(all_count))
            gain_money = (target_count * 1.98 - all_count) * xiazhu_money * all_beishu_count
            pk_logger.debug("target_count: %f",float(float(target_count)/float(all_count)))
        try:
            p = KillPredict.objects.get(lottery_id=lottery_id)
            xiazhu_nums = p.xiazhu_nums
            p.kill_predict_time = lottery_time
            p.lottery_number = lottery_num
            p.predict_total = all_count
            p.target_total = target_count
            p.predict_accuracy = predict_accuracy
            if p.is_xiazhu == 1:
                p.gain_money = gain_money
            #p.input_money = all_count * xiazhu_money
            #p.is_xiazhu = 1
            p.save()
            #判断上一期是否盈利，未盈利，则记录该名词，以后每期购买该名次，知道买中
            if gain_money<0:
                return False, xiazhu_nums
            else:
                return True, xiazhu_nums
        except:
            #print "the ",lottery_id," is repeat!!!"
            pk_logger.debug("the %d is repeat!!!",lottery_id)
            return True,1
    else:
        #print 'length error'
        pk_logger.debug("length error")
        return True,1


#删除当天的信息
def delete_kill_predict_current_date(request):

    current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    KillPredict.objects.filter(kill_predict_date=current_date).delete()

    obj_pro_predict = KillPredict.objects.filter(kill_predict_date=current_date)
    return render_to_response('test.html',{"obj_pro_predict":obj_pro_predict})

import json
from django.http import HttpResponse
#获取杀号预测数据接口
def get_predict(request):
    current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    result_info = {}
    # lotterys = KillPredict.objects.filter(lottery_date=current_date)
    #获取预测的lottery id 和预测的号码
    obj_pro_predict = KillPredict.objects.filter(kill_predict_date=current_date).order_by("-lottery_id")
    if len(obj_pro_predict) == 0:
        pass
    else:
        result_info['predict_lottery_id'] = int(obj_pro_predict[0].lottery_id)
        result_info['predict_number_list'] = obj_pro_predict[0].kill_predict_number
        result_info['predict_number_list_desc'] = obj_pro_predict[0].kill_predict_number_desc
        result_info['xiazhu_beishu'] = obj_pro_predict[0].xiazhu_beishu
        result_info['save_predict_time'] = obj_pro_predict[0].save_predict_time
        #print "predict lottery_id:",obj_pro_predict[0].lottery_id

        #pk_logger.info("predict lottery_id: %d",obj_pro_predict[0].lottery_id)
        #pk_logger.info("kill_predict_number: %s",obj_pro_predict[0].kill_predict_number)
        #print "kill_predict_number:",obj_pro_predict[0].kill_predict_number

    obj_pro_lottery = PredictLottery.objects.filter(lottery_date=current_date).order_by("-lottery_id")
    if len(obj_pro_lottery) == 0:
        result_info['last_lottery_id'] = 0
        pass
    else:
        result_info['last_lottery_id'] = int(obj_pro_lottery[0].lottery_id)
        result_info['lottery_number'] = obj_pro_lottery[0].lottery_number
        #print "last lottery_id:",obj_pro_lottery[0].lottery_id
        #pk_logger.info("last lottery_id: %d",obj_pro_lottery[0].lottery_id)
    return HttpResponse(json.dumps(result_info), content_type="application/json")