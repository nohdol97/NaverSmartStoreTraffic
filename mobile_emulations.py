import random

def getMobileEmulation():
    mobile_emulations = [
        {
            "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        },
        {
            "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.5 },
            "userAgent": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 430, "height": 932, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        },
        {
            "deviceMetrics": { "width": 412, "height": 892, "pixelRatio": 4.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 12; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 4.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 12; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 2.625 },
            "userAgent": "Mozilla/5.0 (Linux; Android 11; LM-V500N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 412, "height": 869, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 10; Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 11; SM-A516N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 412, "height": 892, "pixelRatio": 4.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 430, "height": 932, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
        }
    ]

    # 랜덤하게 하나의 에뮬레이션 설정 선택
    selected_emulation = random.choice(mobile_emulations)

    return selected_emulation