#coding=utf-8
"""spider_pk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from prob.views import index,admin
from prob.views_month import admin_month,index_month,index_month_evaluation
import prob.views_times
import prob.views_month_times


######################
import predict.main
import predict.report

######################
import cross.cross_day
import cross.cross_month

########################
import auto_visit.main
import auto_visit.list

########################
# from auto_purchase.purchase_main import auto_admin,control_probuser_thread,set_user_data
import auto_purchase.purchase_main
import auto_purchase.purchase_client_main
import auto_purchase.user

########################
import auto_pxiagme1_purchase.purchase_client_main
import auto_pxiagme1_purchase.user

#######################追加方式自动化，宝岛
import append_predict.main
import append_predict.user
import append_predict.report
import append_purchase.purchase_client_main
#####电邮 自动化购买
import append_purchase_dianyou.purchase_client_main

#####新金沙 自动化购买
import append_purchase_jinsha.purchase_client_main


#####力德 自动化购买
import append_purchase_lide.purchase_client_main

#####HF 自动化购买
import append_purchase_hf.purchase_client_main



#######################追加方式自动化 --两面盘
import append_predict_sandd.main
import append_predict_sandd.report
import append_predict_sandd.user
import append_purchase_lide_sandd.purchase_client_main



#######################幸运飞艇自动化
import xyft_predict.main
import xyft_predict.user
import xyft_predict.report
import xyft_purchase.purchase_client_main

#新金沙
import xyft_purchase_jinsha.purchase_client_main

#沃龙
import xyft_purchase_wow.purchase_client_main



#######################澳洲幸运自动化
import azxy10_predict.main
import azxy10_predict.user
import azxy10_predict.report
import azxy10_purchase.purchase_client_main

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    ##########################################V8版本#####################################
    url(r'^admin/$', admin),
    url(r'^index/$', index),


    url(r'^admin_month/$', admin_month),
    url(r'^index_month/$', index_month),
    url(r'^index_month_evaluation/$', index_month_evaluation),

    url(r'^admin_times/$', prob.views_times.admin),
    url(r'^index_times/$', prob.views_times.index),
    # url(r'^index_month_times/$', index_month),
    url(r'^admin_month_times/$', prob.views_month_times.admin_month_times),
    url(r'^index_month_times/$', prob.views_month_times.index_month_times),
    url(r'^index_month_times_evaluation/$', prob.views_month_times.index_month_times_evaluation),
    ########################################V9版本  交叉分析与直线分析###########################################
    url(r'^cross_day_admin/$', cross.cross_day.admin),
    url(r'^cross_day_index/$', cross.cross_day.index),

    url(r'^cross_month_admin/$', cross.cross_month.admin_month),
    url(r'^cross_month_index/$', cross.cross_month.index_month),
    url(r'^cross_month_evaluation/$', cross.cross_month.index_month_evaluation),

    ########################################v1.0版本，自动化####################################
    url(r'^auto_main/$', auto_visit.main.auto_admin),
    url(r'^control_probuser_thread/$', auto_visit.main.control_probuser_thread),
    # url(r'^stop_probuser_thread/$', auto_visit.main.stop_probuser_thread),
    url(r'^auto_list/$', auto_visit.list.auto_list),
    url(r'^auto_list_refresh/$', auto_visit.list.auto_list_refresh),

    url(r'^set_user/$', auto_visit.list.set_user),
    # url(r'^get_prob_data/$', auto_visit.main.get_prob_data),
    url(r'^get_purchase_data/$', auto_visit.main.get_purchase_data),
    url(r'^get_fiance_data/$', auto_visit.main.get_fiance_data),

    #######################################v1.1  ,预测###########################################
    url(r'^predict_main/$', predict.main.predict_main),
    url(r'^control_predict_thread/$', predict.main.control_predict_thread),
    url(r'^predict_report/$', predict.report.predict_report),
    url(r'^control_predict_report/$', predict.report.control_predict_report),
    #测试
    url(r'^delete_kill_predict_current_date/$', predict.main.delete_kill_predict_current_date),
    url(r'^get_lottery/$', predict.report.get_lottery_msg),
    url(r'^get_kill_predict_msg/$', predict.report.get_kill_predict_msg),

    ###################################基于杀号自动化购买######################################
    url(r'^auto_purchase/$', auto_purchase.purchase_main.auto_admin),
    url(r'^auto_purchase_control/$', auto_purchase.purchase_main.control_probuser_thread),
    ########客户端
    url(r'^auto_purchase_client/$', auto_purchase.purchase_client_main.auto_admin),
    url(r'^auto_purchase_client_control/$', auto_purchase.purchase_client_main.control_probuser_thread),

    #设置用户set_user_data
    url(r'^set_user_data_v2/$', auto_purchase.purchase_main.set_user_data),
    url(r'^set_auto_purchase_user/$', auto_purchase.user.set_user),
    ########测试
    url(r'^get_kill_predict_lottery_msg/$', auto_purchase.purchase_client_main.get_lottery_msg),


    ###################################获取杀号预测数据接口#############################################
    url(r'^get_predict_data/$', predict.main.get_predict),

    ############################第一版自动化重构，基于概率规则#####################33333
    url(r'^auto_purchase_pxiagme1_client_main/$', auto_pxiagme1_purchase.purchase_client_main.auto_admin),
    url(r'^auto_purchase_pxiagme1_client_control/$', auto_pxiagme1_purchase.purchase_client_main.control_probuser_thread),

    #设置用户set_user_data
    url(r'^set_pxiagme1_auto_purchase_user/$', auto_pxiagme1_purchase.user.set_user),




    #######!!!++++++++++++++++++++++++++++++++基于追加方式的新一期优化   自动化购买类似于predict++++++++++++++++++######################
    url(r'^append_predict_main/$', append_predict.main.predict_main),
    url(r'^append_control_predict_thread/$', append_predict.main.control_predict_thread),
    url(r'^append_predict_report/$', append_predict.report.predict_report),
    url(r'^append_control_predict_report/$', append_predict.report.control_predict_report),

    #演示数据
    url(r'^show_report/', append_predict.report.get_yanshi_report_max_incerease),

    #######返回部分报表
    url(r'^report/$', append_predict.report.get_last_ten_report),
    ###获取预测数据
    url(r'^get_append_predict_data/$', append_predict.main.get_predict),
    #设置用户set_user_data
    url(r'^set_append_auto_purchase_user/$', append_predict.user.set_user),
    #删除当天数据
    url(r'^delete_append_kill_predict_current_date/$', append_predict.main.delete_kill_predict_current_date),

    ######基于杀号自动化购买####
    url(r'^append_purchase/$', append_purchase.purchase_client_main.auto_admin),
    url(r'^append_purchase_control/$', append_purchase.purchase_client_main.control_probuser_thread),



     #######!!!++++++++++++++++++++++++++++++++基于追加方式的新一期优化  电邮系统自动化购买++++++++++++++++++######################
    ######基于杀号自动化购买####
    url(r'^append_purchase_dianyou/$', append_purchase_dianyou.purchase_client_main.auto_admin),
    url(r'^append_purchase_dianyou_control/$', append_purchase_dianyou.purchase_client_main.control_probuser_thread),


     #######!!!++++++++++++++++++++++++++++++++基于追加方式的新一期优化  新金沙系统自动化购买++++++++++++++++++######################
    ######基于杀号自动化购买####
    url(r'^append_purchase_jinsha/$', append_purchase_jinsha.purchase_client_main.auto_admin),
    url(r'^append_purchase_jinsha_control/$', append_purchase_jinsha.purchase_client_main.control_probuser_thread),


    #######!!!++++++++++++++++++++++++++++++++基于追加方式的新一期优化  力德系统自动化购买++++++++++++++++++######################
    ######基于杀号自动化购买####
    url(r'^append_purchase_lide/$', append_purchase_lide.purchase_client_main.auto_admin),
    url(r'^append_purchase_lide_control/$', append_purchase_lide.purchase_client_main.control_probuser_thread),


    #######!!!++++++++++++++++++++++++++++++++基于追加方式的新一期优化  HF系统自动化购买++++++++++++++++++######################
    ######基于杀号自动化购买####
    url(r'^append_purchase_hf/$', append_purchase_hf.purchase_client_main.auto_admin),
    url(r'^append_purchase_hf_control/$', append_purchase_hf.purchase_client_main.control_probuser_thread),


    ###################################################################################################
    #########################################两面盘####################################################
    ###################################################################################################
    url(r'^append_predict_sandd_main/$', append_predict_sandd.main.predict_main),
    url(r'^append_control_predict_sandd_thread/$', append_predict_sandd.main.control_predict_thread),
    url(r'^append_predict_sandd_report/$', append_predict_sandd.report.predict_report),
    url(r'^append_control_predict_sandd_report/$', append_predict_sandd.report.control_predict_report),

    #设置用户set_user_data
    url(r'^set_append_sandd_user/$', append_predict_sandd.user.set_user),
    ###获取预测数据
    url(r'^get_append_predict_sandd_data/$', append_predict_sandd.main.get_predict),
    #力德
    url(r'^append_purchase_lide_sandd/$', append_purchase_lide_sandd.purchase_client_main.auto_admin),
    url(r'^append_purchase_lide_sandd_control/$', append_purchase_lide_sandd.purchase_client_main.control_probuser_thread),




    #######!!!++++++++++++++++++++++++++++++++  幸运飞艇  普通模式 predict++++++++++++++++++######################
    url(r'^xyft_predict_main/$', xyft_predict.main.predict_main),
    url(r'^xyft_control_predict_thread/$', xyft_predict.main.control_predict_thread),

    url(r'^xyft_predict_report/$', xyft_predict.report.predict_report),
    url(r'^xyft_control_predict_report/$', xyft_predict.report.control_predict_report),

    #删除当天数据
    url(r'^delete_xyft_kill_predict_current_date/$', xyft_predict.main.delete_kill_predict_current_date),

    #设置用户set_user_data
    url(r'^set_xyft_auto_purchase_user/$', xyft_predict.user.set_user),


    ######基于预测自动化购买####
    url(r'^xyft_purchase/$', xyft_purchase.purchase_client_main.auto_admin),
    url(r'^xyft_purchase_control/$', xyft_purchase.purchase_client_main.control_probuser_thread),
    ###获取预测数据
    url(r'^get_xyft_predict_data/$', xyft_predict.main.get_predict),



    ######新金沙 幸运飞艇####
    url(r'^xyft_purchase_jinsha/$', xyft_purchase_jinsha.purchase_client_main.auto_admin),
    url(r'^xyft_purchase_jinsha_control/$', xyft_purchase_jinsha.purchase_client_main.control_probuser_thread),

    ######沃龙######
    url(r'^xyft_purchase_wow/$', xyft_purchase_wow.purchase_client_main.auto_admin),
    url(r'^xyft_purchase_wow_control/$', xyft_purchase_wow.purchase_client_main.control_probuser_thread),



    #######!!!++++++++++++++++++++++++++++++++  澳洲幸运  普通模式 predict++++++++++++++++++######################
    url(r'^azxy10_predict_main/$', azxy10_predict.main.predict_main),
    url(r'^azxy10_control_predict_thread/$', azxy10_predict.main.control_predict_thread),

    url(r'^azxy10_predict_report/$', azxy10_predict.report.predict_report),
    url(r'^azxy10_control_predict_report/$', azxy10_predict.report.control_predict_report),

    # 删除当天数据
    url(r'^delete_azxy10_kill_predict_current_date/$', azxy10_predict.main.delete_kill_predict_current_date),

    # 设置用户set_user_data
    url(r'^set_azxy10_auto_purchase_user/$', azxy10_predict.user.set_user),

    ######基于预测自动化购买####
    url(r'^azxy10_purchase/$', azxy10_purchase.purchase_client_main.auto_admin),
    url(r'^azxy10_purchase_control/$', azxy10_purchase.purchase_client_main.control_probuser_thread),
    ###获取预测数据
    url(r'^get_azxy10_predict_data/$', azxy10_predict.main.get_predict),






]
