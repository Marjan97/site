from campaign_site.settings import Kavenegar_API
from kavenegar import *
from random import randint
from zeep import Client
import time
from identity.models import UserEntity
import datetime


class SendOTPHelper:

    @classmethod
    def send_otp_soap(cls, mobile, otp):

        time.sleep(10)
        client = Client('http://api.kavenegar.com/soap/v1.asmx?WSDL')
        receptor = [mobile, ]

        empty_array_placeholder = client.get_type('ns0:ArrayOfString')
        receptors = empty_array_placeholder()
        for item in receptor:
            receptors['string'].append(item)

        api_key = Kavenegar_API
        message = 'Your OTP is {}'.format(otp)
        sender = ''  #
        status = 0
        status_message = ''

        result = client.service.SendSimpleByApikey(api_key,
                                                   sender,
                                                   message,
                                                   receptors,
                                                   0,
                                                   1,
                                                   status,
                                                   status_message)
        print(result)
        print('OTP: ', otp)
        # 403 errror

    @classmethod
    def send_otp(cls, mobile, otp):
        mobile = [mobile, ]
        try:
            api = KavenegarAPI(Kavenegar_API)
            params = {
                'sender': '',  # optional
                'receptor': mobile,  # multiple mobile number
                'message': 'Your OTP is {}'.format(otp),
            }
            response = api.sms_send(params)
            print('OTP: ', otp)
            print(response)
        except APIException as e:
            print(e)
        except HTTPException as e:
            print(e)

    @classmethod
    def get_random_otp(cls):
        return randint(1000, 9999)

    @classmethod
    def check_otp_expiration(cls, mobile):
        try:
            user = UserEntity.objects.get(mobile_phone_number=mobile)
            now = datetime.datetime.now()
            otp_time = user.otp_create_time
            diff_time = now - otp_time
            print('OTP TIME: ', diff_time)

            if diff_time.seconds > 120:
                return False
            return True

        except UserEntity.DoesNotExist:
            return False