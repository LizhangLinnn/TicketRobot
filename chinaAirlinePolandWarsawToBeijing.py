
curl_search_all_query_base = '''
curl -H 'Host: m.airchina.com.cn:9061' -H 'X-Requested-With: XMLHttpRequest' -H 'User-Agent: AirChina/6.6.0.0 (iPhone; iOS 13.3.1; Scale/3.00)/WLNativeAPI/6.3.0.0' -H 'Cookie: WL_PERSISTENT_COOKIE=46bbfb66-3e9d-4295-9133-0f18b8c0e13d; JSESSIONID=0000eK0FiETJGaNX71b5CrAg5YI:-1; NSC_xpslmjhiu=ffffffff0901ec1e45525d5f4f58455e445a4a42154b' -H 'WL-Instance-Id: 7ou4bdaj0pej6js81sptbbvlf1' -H 'x-wl-clientlog-osversion: 13.3.1' -H 'x-wl-clientlog-env: iphone' -H 'X-Tingyun-Id: UiLVhboHIX8;c=2;r=8936987;u=784cac62f93e13cb2f4898448a2880a87f3120089f2cb5e6e5f88a44f703b30f9d34f226f66e997699a570f7fa3d7efd::4C53E4C67027E44C' -H 'x-wl-clientlog-deviceId: 92706437-7FF4-4AA5-9003-D4E2949F87E7' -H 'x-wl-clientlog-model: iPhone11,2' -H 'x-wl-analytics-tracking-id: 3079A562-3B67-418D-A37C-CB91B9536F34' -H 'Connection: keep-alive' -H 'x-wl-clientlog-appname: AirChina' -H 'x-wl-platform-version: 6.3.0.0' -H 'Accept-Language: en-GB' -H 'x-wl-clientlog-appversion: 1.0' -H 'Accept: */*' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' --compressed -H 'x-wl-app-version: 1.0' -X POST https://m.airchina.com.cn:9061/worklight/apps/services/api/AirChina/iphone/query -d '__wl_deviceCtx=AXieR9utui9quBAA&adapter=ACCommon&compressResponse=true&isAjaxRequest=true&parameters=%5B%7B%22secureToken%22%3A%22AppSecureToken%22%2C%22ziYinNo%22%3A%22058002950208%22%2C%22userID%22%3A%22FC06FA9EEBB0624E4BE85732D1B5AC51%22%2C%22userInfo3%22%3A%220730C7172DD4226EB77B6939007C6368B300FE827FB0C955A66013D2341BF029%22%2C%22req%22%3A%22%7B%5Cn%20%20%5C%22userId%5C%22%20%3A%20%5C%22FC06FA9EEBB0624E4BE85732D1B5AC51%5C%22%2C%5Cn%20%20%5C%22IOSUSERSYSTEMDATE%5C%22%20%3A%20%5C%222020-06-16%2000%3A19%3A51-Europe%5C%5C%2FLondon%20%28BST%29%20offset%203600%20%28Daylight%29%5C%22%2C%5Cn%20%20%5C%22org%5C%22%20%3A%20%5C%22WAW%5C%22%2C%5Cn%20%20%5C%22isTransDst%5C%22%20%3A%20%5C%220%5C%22%2C%5Cn%20%20%5C%22dst%5C%22%20%3A%20%5C%22PEK%5C%22%2C%5Cn%20%20%5C%22mId%5C%22%20%3A%20%5C%221-13QF5K89%5C%22%2C%5Cn%20%20%5C%22isTransOrg%5C%22%20%3A%20%5C%220%5C%22%5Cn%7D%22%2C%22mobileSysVer%22%3A%2213.3.1%22%2C%22primaryTierName%22%3A%22Normal%22%2C%22deviceId%22%3A%22F0ED0121-C51F-4DA4-A55E-10EE095CF68A%22%2C%22crmMemberId%22%3A%221-13QF5K89%22%2C%22userInfo1%22%3A%2260600%22%2C%22userInfo4%22%3A%2294BFC263BF027389174A9A1EA88C833F%22%2C%22token%22%3A%227d02b5044417de0cf64854d50b123e61857d0f4d2ba2f243c8541822822c0d37%22%2C%22deviceType%22%3A%22iPhone%22%2C%22appVer%22%3A%226.6.0%22%2C%22deviceModel%22%3A%22iPhone11%2C2%22%2C%22lang%22%3A%22en_US%22%2C%22userInfo2%22%3A%22F06B0827791A19043AEC6351B77AD673%22%2C%22dxRiskToken%22%3A%225ee797589SU4If4s3oRzPzzQMkEnRa6dW0P8kWL2%22%2C%22infoID%22%3A%222BCB9C4CEA779F82CDD1B93481F63C17%22%7D%5D&procedure=qryLowCalendar'
'''

from util import *
air_china_curl(curl_search_all_query_base, 'Poland Warsaw', 'Beijing', 4) # 4 == Friday (index starting from 0)