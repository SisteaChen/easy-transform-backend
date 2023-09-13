from rest_framework.views import APIView
from random import randint
from django_redis import get_redis_connection
from ronglian_sms_sdk import SmsSDK
from rest_framework.response import Response
import json

accId = '8aaf0708780055cd01783c965955165c'
accToken = '313c46d3d1714d639eac7d0d06ca8686'
appId = '8aaf0708780055cd01783c965a501663'
tid = '1'
time_limit = 3

# Create your views here.
class SMSCodeView(APIView):
    """
        短信验证码
        000000	请求成功
        172001	网络错误
    """
    def get(self, request, mobile):
        # 1. 生成验证码
        sms_code = str(randint(0, 999999)).zfill(6)
        # 2. 存redis
        redis_conn = get_redis_connection('verify_sms_codes')
        redis_conn.setex('sms_{}'.format(mobile), time_limit*60, sms_code)
        # 3. 容联云发送验证码
        sdk = SmsSDK(accId, accToken, appId)
        datas = (sms_code, str(time_limit))
        resp = sdk.sendMessage(tid, str(mobile), datas)
        try:
            resp = json.loads(resp)
        except:
            resp = {'statusCode': '172001'}
        # 4. response
        return Response({"code": 200})
