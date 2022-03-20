import requests

cookies = {

}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Origin': 'https://www.ajihuo.com',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.ajihuo.com/pycharm/4197.html',
    'Accept-Language': 'zh,en;q=0.9,zh-CN;q=0.8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'Hm_lvt_30e155ae2d2fcd1332fa3746413210ee=1644235401,1644636578; session_prefix=821409ea4390560811ae93f9c050dd51; Hm_lvt_bc4856baaeecfd9234b878603add3a71=1647510147; Hm_lpvt_bc4856baaeecfd9234b878603add3a71=1647754175',
}

data = {
    'secret_key': '199992',
    'Submit': '\u9605\u8BFB\u5168\u6587',
}

response = requests.post('https://www.ajihuo.com/pycharm/4197.html', headers=headers, cookies=cookies, data=data)
print()