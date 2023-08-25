"""Decoder ring for the WebUI on the murideo"""

Murideo_WebUI = {  # Master Dictionary for WebUI of Murideo 8K Seven Genderator
    "video_generator": {
        "timing": {
            "function": "sendsingle",  # Function needed to send the command ex: SENDSINGLE||97,110
            "category_type": 97,  # ID For the category in this case it's 97=Timing
            "8k": {
                "7680x4320@30": {
                    "id": 110,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "7680x4320 30Hz",  # The actual Button text
                },
                "7680x4320@29.97": {
                    "id": 111,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "7680x4320 29.97Hz",  # The actual Button text
                },
                "7680x4320@25": {
                    "id": 112,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "7680x4320 25Hz",  # The actual Button text
                },
                "7680x4320@24": {
                    "id": 113,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "7680x4320 24Hz",  # The actual Button text
                },
                "7680x4320@23.98": {
                    "id": 114,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 23.98,  # Refresh Rate
                    "tag": "7680x4320 23.98Hz",  # The actual Button text
                },
                "7680x4320@60": {
                    "id": 115,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "7680x4320 60Hz",  # The actual Button text
                },
                "7680x4320@59.94": {
                    "id": 116,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "7680x4320 59.94Hz",  # The actual Button text
                },
                "7680x4320@50": {
                    "id": 117,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "7680x4320 50Hz",  # The actual Button text
                },
                "7680x4320@48": {
                    "id": 118,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "7680x4320 48Hz",  # The actual Button text
                },
                "7680x4320@47.95": {
                    "id": 119,  # command to be called for this resolution
                    "h_rez": 7680,  # Horizontal Pixels
                    "v_rez": 4320,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "7680x4320 47.95Hz",  # The actual Button text
                },
            },
            "uhd": {
                "3840x2160@30": {
                    "id": 28,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "3840x2160 30Hz",  # The actual Button text
                },
                "3840x2160@29.97": {
                    "id": 29,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "3840x2160 29.97Hz",  # The actual Button text
                },
                "3840x2160@25": {
                    "id": 30,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "3840x2160 25Hz",  # The actual Button text
                },
                "3840x2160@24": {
                    "id": 31,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "3840x2160 24Hz",  # The actual Button text
                },
                "3840x2160@23.98": {
                    "id": 32,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 23.98,  # Refresh Rate
                    "tag": "3840x2160 23.98Hz",  # The actual Button text
                },
                "3840x2160@60": {
                    "id": 34,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "3840x2160 60Hz",  # The actual Button text
                },
                "3840x2160@59.94": {
                    "id": 35,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "3840x2160 59.94Hz",  # The actual Button text
                },
                "3840x2160@50": {
                    "id": 36,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "3840x2160 50Hz",  # The actual Button text
                },
                "3840x2160@48": {
                    "id": 103,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "3840x2160 48Hz",  # The actual Button text
                },
                "3840x2160@47.95": {
                    "id": 104,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "3840x2160 47.95Hz",  # The actual Button text
                },
                "3840x2160@100": {
                    "id": 107,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 100,  # Refresh Rate
                    "tag": "3840x2160 100Hz",  # The actual Button text
                },
                "3840x2160@120": {
                    "id": 108,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 120,  # Refresh Rate
                    "tag": "3840x2160 120Hz",  # The actual Button text
                },
                "3840x2160@119.88": {
                    "id": 109,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 119.88,  # Refresh Rate
                    "tag": "3840x2160 119.88Hz",  # The actual Button text
                },
            },
            "4k-dci": {
                "4096x2160@30": {
                    "id": 53,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "4096x2160 30Hz",  # The actual Button text
                },
                "4096x2160@29.97": {
                    "id": 54,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "4096x2160 29.97Hz",  # The actual Button text
                },
                "4096x2160@25": {
                    "id": 55,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "4096x2160 25Hz",  # The actual Button text
                },
                "4096x2160@24": {
                    "id": 44,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "4096x2160 24Hz",  # The actual Button text
                },
                "4096x2160@23.976": {
                    "id": 56,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "4096x2160 23.976Hz",  # The actual Button text
                },
                "4096x2160@60": {
                    "id": 57,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "4096x2160 60Hz",  # The actual Button text
                },
                "4096x2160@59.94": {
                    "id": 58,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "4096x2160 59.94Hz",  # The actual Button text
                },
                "4096x2160@50": {
                    "id": 59,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "4096x2160 50Hz",  # The actual Button text
                },
                "4096x2160@48": {
                    "id": 105,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 48,  # Refresh Rate
                    "tag": "4096x2160 48Hz",  # The actual Button text
                },
                "4096x2160@47.95": {
                    "id": 106,  # command to be called for this resolution
                    "h_rez": 4096,  # Horizontal Pixels
                    "v_rez": 2160,  # Vertical Pixels
                    "refresh": 47.95,  # Refresh Rate
                    "tag": "4096x2160 47.95Hz",  # The actual Button text
                },
            },
            "2k-dci": {
                "2048x1080@30": {
                    "id": 73,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "2048x1080 30Hz",  # The actual Button text
                },
                "2048x1080@29.97": {
                    "id": 74,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "2048x1080 29.97Hz",  # The actual Button text
                },
                "2048x1080@25": {
                    "id": 75,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "2048x1080 25Hz",  # The actual Button text
                },
                "2048x1080@24": {
                    "id": 76,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "2048x1080 24Hz",  # The actual Button text
                },
                "2048x1080@23.976": {
                    "id": 77,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "2048x1080 23.976Hz",  # The actual Button text
                },
                "2048x1080@60": {
                    "id": 78,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "2048x1080 60Hz",  # The actual Button text
                },
                "2048x1080@59.94": {
                    "id": 79,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "2048x1080 59.94Hz",  # The actual Button text
                },
                "2048x1080@50": {
                    "id": 80,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "2048x1080 50Hz",  # The actual Button text
                },
            },
            "hd": {
                "1280x720p@60": {
                    "id": 12,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "720P 60Hz",  # The actual Button text
                },
                "1280x720p@59.94": {
                    "id": 13,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "720P 59.94Hz",  # The actual Button text
                },
                "1920x1080i@60": {
                    "id": 14,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "1080i 60Hz",  # The actual Button text
                },
                "1920x1080i@59.94": {
                    "id": 15,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "1080i 59.94Hz",  # The actual Button text
                },
                "1920x1080p@30": {
                    "id": 16,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 30,  # Refresh Rate
                    "tag": "1080p 30Hz",  # The actual Button text
                },
                "1920x1080p@29.97": {
                    "id": 17,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 29.97,  # Refresh Rate
                    "tag": "1080p 29.97Hz",  # The actual Button text
                },
                "1920x1080p@24": {
                    "id": 18,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "1080p 24Hz",  # The actual Button text
                },
                "1920x1080p@23.976": {
                    "id": 19,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "1080p 23.976Hz",  # The actual Button text
                },
                "1920x1080p@60": {
                    "id": 20,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "1080p 60Hz",  # The actual Button text
                },
                "1920x1080p@59.94": {
                    "id": 21,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "1080p 59.94Hz",  # The actual Button text
                },
                "1280x720p@50": {
                    "id": 24,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "720P 50Hz",  # The actual Button text
                },
                "1920x1080i@50": {
                    "id": 25,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "1080i 50Hz",  # The actual Button text
                },
                "1920x1080p@25": {
                    "id": 26,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 25,  # Refresh Rate
                    "tag": "1080p 25Hz",  # The actual Button text
                },
                "1920x1080p@50": {
                    "id": 27,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "1080p 50Hz",  # The actual Button text
                },
                "1920x1080p@120": {
                    "id": 81,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 120,  # Refresh Rate
                    "tag": "1080p 120Hz",  # The actual Button text
                },
                "1920x1080p@119.88": {
                    "id": 82,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 119.88,  # Refresh Rate
                    "tag": "1080p 119.88Hz",  # The actual Button text
                },
                "1920x1080p@100": {
                    "id": 102,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 100,  # Refresh Rate
                    "tag": "1080p 100Hz",  # The actual Button text
                },
            },
            "sd": {
                "720x480i@59.94": {
                    "id": 10,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "480i 59.94Hz",  # The actual Button text
                },
                "720x480p@59.94": {
                    "id": 11,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "480p 59.94Hz",  # The actual Button text
                },
                "720x576i@50": {
                    "id": 22,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 576,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "576i 50Hz",  # The actual Button text
                },
                "720x576p@50": {
                    "id": 23,  # command to be called for this resolution
                    "h_rez": 720,  # Horizontal Pixels
                    "v_rez": 576,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "576p 50Hz",  # The actual Button text
                },
            },
            "vesa": {
                "640x480@60": {
                    "id": 0,  # command to be called for this resolution
                    "h_rez": 640,  # Horizontal Pixels
                    "v_rez": 480,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "VGA 640x480",  # The actual Button text
                },
                "800x600@60": {
                    "id": 1,  # command to be called for this resolution
                    "h_rez": 800,  # Horizontal Pixels
                    "v_rez": 600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SVGA 800x600",  # The actual Button text
                },
                "1024x768@60": {
                    "id": 2,  # command to be called for this resolution
                    "h_rez": 1024,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA 1024x768",  # The actual Button text
                },
                "1152x864@60": {
                    "id": 72,  # command to be called for this resolution
                    "h_rez": 1152,  # Horizontal Pixels
                    "v_rez": 864,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA+ 1152x864",  # The actual Button text
                },
                "1360x768@60": {
                    "id": 4,  # command to be called for this resolution
                    "h_rez": 1360,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD 1360x768",  # The actual Button text
                },
                "1280x768@60": {
                    "id": 3,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 768,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD 1280x768",  # The actual Button text
                },
                "1280x960@60": {
                    "id": 5,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 896064,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA 1280x960",  # The actual Button text
                },
                "1400x1050@60": {
                    "id": 7,  # command to be called for this resolution
                    "h_rez": 1400,  # Horizontal Pixels
                    "v_rez": 1050,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA+ 1400x1050",  # The actual Button text
                },
                "1440x900@60": {
                    "id": 69,  # command to be called for this resolution
                    "h_rez": 1440,  # Horizontal Pixels
                    "v_rez": 60,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WXGA+ 1440x900",  # The actual Button text
                },
                "1600x900@60": {
                    "id": 70,  # command to be called for this resolution
                    "h_rez": 1600,  # Horizontal Pixels
                    "v_rez": 900,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "HD+ 1600x900",  # The actual Button text
                },
                "1600x1200@60": {
                    "id": 8,  # command to be called for this resolution
                    "h_rez": 1600,  # Horizontal Pixels
                    "v_rez": 1200,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UXGA 1600x1200",  # The actual Button text
                },
                "1920x1200@60": {
                    "id": 9,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1200,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WUXGA 1920x1200",  # The actual Button text
                },
                "1152x900@60": {
                    "id": 83,  # command to be called for this resolution
                    "h_rez": 1152,  # Horizontal Pixels
                    "v_rez": 900,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "XGA+ 1152x900",  # The actual Button text
                },
                "1280x800@60": {
                    "id": 84,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 800,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WXGA 1280x800",  # The actual Button text
                },
                "1280x1050@60": {
                    "id": 85,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 1050,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SXGA 1280x1050",  # The actual Button text
                },
                "1920x1280@60": {
                    "id": 86,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1280,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 1920x1280",  # The actual Button text
                },
                "1920x1440@60": {
                    "id": 87,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 1920x1440",  # The actual Button text
                },
                "2048x1152@60": {
                    "id": 88,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1152,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QWXGA 2048x1152",  # The actual Button text
                },
                "2048x1536@60": {
                    "id": 89,  # command to be called for this resolution
                    "h_rez": 2048,  # Horizontal Pixels
                    "v_rez": 1536,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QXGA 2048x1536",  # The actual Button text
                },
                "2160x1440@60": {
                    "id": 90,  # command to be called for this resolution
                    "h_rez": 2160,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 2160x1440",  # The actual Button text
                },
                "2560x1080@60": {
                    "id": 91,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UN 2560x1080",  # The actual Button text
                },
                "2560x1440@60": {
                    "id": 92,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QHD 2560x1440",  # The actual Button text
                },
                "2560x1600@60": {
                    "id": 93,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 1600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQXGA 2560x1600",  # The actual Button text
                },
                "2560x2048@60": {
                    "id": 94,  # command to be called for this resolution
                    "h_rez": 2560,  # Horizontal Pixels
                    "v_rez": 2048,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QSXGA 2560x2048",  # The actual Button text
                },
                "2880x1800@60": {
                    "id": 95,  # command to be called for this resolution
                    "h_rez": 2880,  # Horizontal Pixels
                    "v_rez": 1800,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "QWXGA+ 2880x1800",  # The actual Button text
                },
                "2960x1440@60": {
                    "id": 96,  # command to be called for this resolution
                    "h_rez": 2960,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "GAL 2960x1440",  # The actual Button text
                },
                "3000x2000@60": {
                    "id": 97,  # command to be called for this resolution
                    "h_rez": 3000,  # Horizontal Pixels
                    "v_rez": 2000,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "SUR 3000x2000",  # The actual Button text
                },
                "3200x2048@60": {
                    "id": 98,  # command to be called for this resolution
                    "h_rez": 3200,  # Horizontal Pixels
                    "v_rez": 2048,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQSXGA 3200x2048",  # The actual Button text
                },
                "3440x1440@60": {
                    "id": 99,  # command to be called for this resolution
                    "h_rez": 3440,  # Horizontal Pixels
                    "v_rez": 1440,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UWQHD 3440X1440",  # The actual Button text
                },
                "3840x1600@60": {
                    "id": 72,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 1600,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "UW4K 3840x1600",  # The actual Button text
                },
                "3840x2400@60": {
                    "id": 101,  # command to be called for this resolution
                    "h_rez": 3840,  # Horizontal Pixels
                    "v_rez": 2400,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "WQUXGA 3840x2400",  # The actual Button text
                },
            },
            "3d": {
                "1280x720p@60": {
                    "id": 37,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 60,  # Refresh Rate
                    "tag": "720P 60Hz (3D-FP)",  # The actual Button text
                },
                "1280x720p@59.94": {
                    "id": 38,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 59.94,  # Refresh Rate
                    "tag": "720P 59.94Hz (3D-FP)",  # The actual Button text
                },
                "1920x1080p@24": {
                    "id": 39,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 24,  # Refresh Rate
                    "tag": "1080P 24Hz (3D-FP)",  # The actual Button text
                },
                "1920x1080P@23.976": {
                    "id": 40,  # command to be called for this resolution
                    "h_rez": 1920,  # Horizontal Pixels
                    "v_rez": 1080,  # Vertical Pixels
                    "refresh": 23.976,  # Refresh Rate
                    "tag": "1080P 23.976Hz (3D-FP)",  # The actual Button text
                },
                "1280x720p@50": {
                    "id": 41,  # command to be called for this resolution
                    "h_rez": 1280,  # Horizontal Pixels
                    "v_rez": 720,  # Vertical Pixels
                    "refresh": 50,  # Refresh Rate
                    "tag": "720P 50Hz (3D-FP)",  # The actual Button text
                },
            },
            "custom": {
                "USER-1": {
                    "id": 43,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-1",  # The actual Button text
                },
                "USER-2": {
                    "id": 44,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-2",  # The actual Button text
                },
                "USER-3": {
                    "id": 45,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-3",  # The actual Button text
                },
                "USER-4": {
                    "id": 46,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-4",  # The actual Button text
                },
                "USER-5": {
                    "id": 47,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-5",  # The actual Button text
                },
                "USER-6": {
                    "id": 48,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-6",  # The actual Button text
                },
                "USER-7": {
                    "id": 49,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-9",  # The actual Button text
                },
                "USER-8": {
                    "id": 50,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-8",  # The actual Button text
                },
                "USER-9": {
                    "id": 51,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-9",  # The actual Button text
                },
                "USER-10": {
                    "id": 52,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "USER-10",  # The actual Button text
                },
            },
            "auto": {
                "AUTO": {
                    "id": 43,  # command to be called for this resolution
                    "h_rez": None,  # Horizontal Pixels
                    "v_rez": None,  # Vertical Pixels
                    "refresh": None,  # Refresh Rate
                    "tag": "Auto(Output timing based on EDID of sink device)",  # The actual Button text
                    "note": "This needs to send 2 commands, 1. SENDSINGLE||97,42 2. SENDSINGLE||47160,1",  # TODO Figure out how to send 2 commands
                },
            },
        },
        "pattern": {
            "function": "senddouble",  # Function needed to send the command ex: SENDDOUBLE||98,458
            "category_type": 98,  # ID for the category in this case it's 98=Pattern
            "fpga": {
                "100% Color Bars": {
                    "id": 0,
                    "tag": "100% Color Bars",
                },
                "75% Color Bars": {
                    "id": 1,
                    "tag": "75% Color Bars",
                },
                "8 Step Gray Bars": {
                    "id": 2,
                    "tag": "8 Step Gray Bars",
                },
                "16 Step Gray Bars": {
                    "id": 3,
                    "tag": "16 Step Gray Bars",
                },
                "Red Screen": {
                    "id": 4,
                    "tag": "Red Screen",
                },
                "Green Screen": {
                    "id": 5,
                    "tag": "Green Screen",
                },
                "Blue Screen": {
                    "id": 6,
                    "tag": "Blue Screen",
                },
                "Cyan Screen": {
                    "id": 7,
                    "tag": "Cyan Screen",
                },
                "Magenta Screen": {
                    "id": 8,
                    "tag": "Magenta Screen",
                },
                "Yellow Screen": {
                    "id": 9,
                    "tag": "Yellow Screen",
                },
                "Black Screen": {
                    "id": 10,
                    "tag": "Black Screen",
                },
                "White Screen": {
                    "id": 11,
                    "tag": "White Screen",
                },
                "Vertical Split": {
                    "id": 12,
                    "tag": "Vertical Split",
                },
                "Horizontal Split": {
                    "id": 13,
                    "tag": "Horizontal Split",
                },
                "Multiburst Vert.": {
                    "id": 14,
                    "tag": "Multiburst Vert.",
                },
                "Multiburst Hor.": {
                    "id": 15,
                    "tag": "Multiburst Hor.",
                },
                "Quarter Block 1": {
                    "id": 16,
                    "tag": "Quarter Block 1",
                },
                "Quarter Block 2": {
                    "id": 17,
                    "tag": "Quarter Block 2",
                },
                "Alternate W.B": {
                    "id": 18,
                    "tag": "Alternate W.B",
                },
                "RGB CMY Ramps": {
                    "id": 19,
                    "tag": "RGB CMY Ramps",
                },
                "Black Pluge": {
                    "id": 20,
                    "tag": "Black Pluge",
                },
                "White Pluge": {
                    "id": 21,
                    "tag": "White Pluge",
                },
                "Still Gray Ramp 1": {
                    "id": 22,
                    "tag": "Still Gray Ramp 1",
                },
                "Still Gray Ramp 2": {
                    "id": 23,
                    "tag": "Still gray Ramp 2",
                },
                "Smpte Bars": {
                    "id": 24,
                    "tag": "Smpte Bars",
                },
                "Border Lines": {
                    "id": 25,
                    "tag": "Border Lines",
                },
                "Window": {
                    "id": 26,
                    "tag": "Window",
                },
                "3D Boxes": {
                    "id": 27,
                    "tag": "3D Boxes",
                },
                "Line V.Scroll": {
                    "id": 28,
                    "tag": "Line V.Scroll",
                },
                "Line H.Scroll": {
                    "id": 29,
                    "tag": "Line H.Scroll",
                },
                "A/V Sync": {
                    "id": 30,
                    "tag": "A/V Sync",
                },
                "Gray Ramp": {
                    "id": 31,
                    "tag": "Gray Ramp",
                },
                "Red Ramp": {
                    "id": 32,
                    "tag": "Red Ramp",
                },
                "Green Ramp": {
                    "id": 33,
                    "tag": "Green Ramp",
                },
                "Blue Ramp": {
                    "id": 34,
                    "tag": "Blue Ramp",
                },
                "Moving Ball": {
                    "id": 35,
                    "tag": "Moving Ball",
                },
            },
        },
    }
}
