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
        },
        {
            "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 11; SM-A516N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.5 },
            "userAgent": "Mozilla/5.0 (Linux; Android 13; Galaxy S22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 430, "height": 932, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1"
        },
        {
            "deviceMetrics": { "width": 412, "height": 892, "pixelRatio": 4.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 12; Galaxy Note20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 360, "height": 800, "pixelRatio": 4.0 },
            "userAgent": "Mozilla/5.0 (Linux; Android 12; Galaxy Z Flip3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 390, "height": 844, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1"
        },
        {
            "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.5 },
            "userAgent": "Mozilla/5.0 (Linux; Android 13; Galaxy S22 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Mobile Safari/537.36"
        },
        {
            "deviceMetrics": { "width": 430, "height": 932, "pixelRatio": 3.0 },
            "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        }
    ]

    # 랜덤하게 하나의 에뮬레이션 설정 선택
    selected_emulation = random.choice(mobile_emulations)

    return selected_emulation

def random_mime_types():
    mime_types = [
        [{'type': 'application/pdf'}, {'type': 'application/x-nacl'}, {'type': 'application/x-pnacl'}],
        [{'type': 'application/vnd.mozilla.xul+xml'}, {'type': 'application/x-shockwave-flash'}, {'type': 'application/futuresplash'}],
        [{'type': 'application/haansoft-hwp'}, {'type': 'application/x-hwp'}, {'type': 'application/x-hwt'}],
        [{'type': 'application/whale-pdf'}, {'type': 'application/x-kakaotalk'}, {'type': 'application/x-nateon'}],
        [{'type': 'application/x-webtoon'}, {'type': 'application/x-alpdf'}, {'type': 'application/x-web-music'}],
        [{'type': 'video/mp4'}, {'type': 'video/webm'}, {'type': 'video/x-flv'}],
        [{'type': 'audio/mpeg'}, {'type': 'audio/ogg'}, {'type': 'audio/wav'}]
    ]
    return random.choice(mime_types)

def random_device_memory():
    return random.choice([4, 6, 8, 12])

def random_hardware_concurrency():
    return random.choice([4, 8])

def mobile_setting(driver, mobile_emulation):
    screen_width = mobile_emulation["deviceMetrics"]["width"]
    screen_height = mobile_emulation["deviceMetrics"]["height"]
    pixel_ratio = mobile_emulation["deviceMetrics"]["pixelRatio"]
    user_agent = mobile_emulation["userAgent"]
    platform = "Linux armv8l" if "Android" in user_agent else "iPhone"
    mime_types = random_mime_types()
    device_memory = random_device_memory()
    hardware_concurrency = random_hardware_concurrency()

    driver.execute_script(f"""
        // navigator.webdriver 제거
        Object.defineProperty(navigator, 'webdriver', {{ get: () => undefined }});

        // Screen Resolution 및 Color Depth 변조
        Object.defineProperty(screen, 'width', {{ get: () => {screen_width} }});
        Object.defineProperty(screen, 'height', {{ get: () => {screen_height} }});
        Object.defineProperty(screen, 'pixelDepth', {{ get: () => {pixel_ratio * 24} }});

        // MimeTypes 변조
        Object.defineProperty(navigator, 'mimeTypes', {{
            get: () => {mime_types}
        }});

        // Navigator 객체 속성 변조
        Object.defineProperty(navigator, 'languages', {{
            get: () => ['ko-KR', 'ko']
        }});
        Object.defineProperty(navigator, 'platform', {{
            get: () => '{platform}'
        }});

        // Hardware Concurrency 변조
        Object.defineProperty(navigator, 'hardwareConcurrency', {{
            get: () => {hardware_concurrency}
        }});

        // Device Memory 변조
        Object.defineProperty(navigator, 'deviceMemory', {{
            get: () => {device_memory}
        }});
    """)