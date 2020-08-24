from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.iotcloud.v20180614 import iotcloud_client, models 
try: 
    cred = credential.Credential("appid", "appkey") 
    httpProfile = HttpProfile()
    httpProfile.endpoint = "iotcloud.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = iotcloud_client.IotcloudClient(cred, "ap-guangzhou", clientProfile) 

    req = models.DescribeProductsRequest()
    params = '{\"Offset\":0,\"Limit\":10}'
    req.from_json_string(params)

    resp = client.DescribeProducts(req) 
    print(resp.to_json_string()) 

except TencentCloudSDKException as err: 
    print(err) 