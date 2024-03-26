# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from jsonpath import jsonpath
from django.views import View
from django.http import HttpResponse
from supaswa1.models import Data

# coding: utf-8

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkiotda.v5 import *
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials

# from huaweicloudsdkcore.exceptions import exceptions
# from huaweicloudsdkcore.region.region import Region
# from huaweicloudsdkiotda.v5 import IoTDAClient, CreateCommandRequest, DeviceCommandRequest
# from huaweicloudsdkcore.auth.credentials import BasicCredentials, DerivedCredentials

# Create your views here.

class IotDataView(APIView):

    def post(self, request, *args,**kwargs):

        data = request.data

        print(data)

        notify_data = request.data.get('notify_data')

        event_time = jsonpath(notify_data,'$..event_time')

        device_id = jsonpath(notify_data,'$..device_id')
        service_id = jsonpath(notify_data,'$..service_id')
        Temperature = jsonpath(notify_data,'$..Temperature')

        iota = Data.objects.create(
            event_time=event_time[0],
            device_id=device_id[0],
            service_id=service_id[0],
            Temperature=Temperature[0],
            original_data=data
        )

        iota.save()

        return HttpResponse('200 OK')


class IotDataView1(APIView):

    def post(self, request):

        from huaweicloudsdkcore.exceptions import exceptions
        from huaweicloudsdkcore.region.region import Region
        from huaweicloudsdkiotda.v5 import IoTDAClient, CreateCommandRequest, DeviceCommandRequest
        from huaweicloudsdkcore.auth.credentials import BasicCredentials, DerivedCredentials

        ak = 'MCAKQAIYC5SPGS6XNTOE'
        sk = '7DQG6oQenMRC2bGRQnPSK2Hghh54xEAtDRVDltYy'

        project_id = "f69c0e3892f8473aa4b49bd3832e0ec5"
        # region_id：如果是上海一，请填写"cn-east-3"；如果是北京四，请填写"cn-north-4"；如果是华南广州，请填写"cn-south-1"
        region_id = "cn-north-4"
        # endpoint：请在控制台的"总览"界面的"平台接入地址"中查看"应用侧"的https接入地址
        endpoint = "45230d01bf.st1.iotda-app.cn-north-4.myhuaweicloud.com"

        # 标准版/企业版：需自行创建Region对象
        REGION = Region(region_id, endpoint)

        # 创建认证
        # 创建BasicCredentials实例并初始化
        credentials = BasicCredentials(ak, sk, project_id)

        # 标准版/企业版需要使用衍生算法，基础版请删除配置"with_derived_predicate"
        credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

        # credentials = BasicCredentials(ak, sk)\
        #     .with_derived_predicate(DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(REGION) \
            .build()

        try:
            request = CreateCommandRequest()
            # 实例化请求对象
            # request = ListDevicesRequest()

            request.device_id = "65e700652ccc1a58387ac9ae_1234"
            # request.instance_id = "af4d4490-01e9-4947-8231-efa40bc79008"
            request.body = DeviceCommandRequest(
                # paras="{\"Light\":\"ON\"}",
                paras='{"Light":"ON"}',
                command_name="Agriculture_Control_light",
                # service_id="Agriculture"
            )
            response = client.create_command(request)
            print('电灯打开测试后端连接成功')

            return HttpResponse(response)

        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)

            return HttpResponse('error')

class IotDataView2(APIView):

    def post(self, request):

        from huaweicloudsdkcore.exceptions import exceptions
        from huaweicloudsdkcore.region.region import Region
        from huaweicloudsdkiotda.v5 import IoTDAClient, CreateCommandRequest, DeviceCommandRequest
        from huaweicloudsdkcore.auth.credentials import BasicCredentials, DerivedCredentials

        ak = 'MCAKQAIYC5SPGS6XNTOE'
        sk = '7DQG6oQenMRC2bGRQnPSK2Hghh54xEAtDRVDltYy'

        project_id = "f69c0e3892f8473aa4b49bd3832e0ec5"
        # region_id：如果是上海一，请填写"cn-east-3"；如果是北京四，请填写"cn-north-4"；如果是华南广州，请填写"cn-south-1"
        region_id = "cn-north-4"
        # endpoint：请在控制台的"总览"界面的"平台接入地址"中查看"应用侧"的https接入地址
        endpoint = "45230d01bf.st1.iotda-app.cn-north-4.myhuaweicloud.com"

        # 标准版/企业版：需自行创建Region对象
        REGION = Region(region_id, endpoint)

        # 创建认证
        # 创建BasicCredentials实例并初始化
        credentials = BasicCredentials(ak, sk, project_id)

        # 标准版/企业版需要使用衍生算法，基础版请删除配置"with_derived_predicate"
        credentials.with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

        # credentials = BasicCredentials(ak, sk)\
        #     .with_derived_predicate(DerivedCredentials.get_default_derived_predicate())
        client = IoTDAClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(REGION) \
            .build()

        try:
            request = CreateCommandRequest()
            # 实例化请求对象
            # request = ListDevicesRequest()

            request.device_id = "65e700652ccc1a58387ac9ae_1234"
            # request.instance_id = "af4d4490-01e9-4947-8231-efa40bc79008"
            request.body = DeviceCommandRequest(
                # paras="{\"Light\":\"ON\"}",
                paras='{"Light":"OFF"}',
                command_name="Agriculture_Control_light",
                # service_id="Agriculture"
            )
            response = client.create_command(request)
            print('电灯打开测试后端连接成功')

            return HttpResponse(response)

        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)

            return HttpResponse('error')

class APPData(APIView):

     def post(self, request):

        try:
            MysqlData = Data.objects.last()

            print(MysqlData.Temperature_value)
            return HttpResponse(MysqlData.Temperature_value)

        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)

            return HttpResponse('error')