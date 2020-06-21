curl_base = '''
curl 'https://b2c.csair.com/ita/rest/intl/shop/nearAirline/search?execution=4abf4578eb2f3032bebfb3e8423c65eb&language=zh&date=2020-{}-{}&tsf=2'
'''

from util import *
china_southern_curl(curl_base, 'london', 'shanghai')