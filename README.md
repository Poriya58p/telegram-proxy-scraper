# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 11 July 2025, 12:40 UTC (به وقت ایران: 16:10)

این پروژه یه اسکریپت پایتون برای جمع‌آوری خودکار پروکسی‌های MTProto تلگرام از منابع متنی و کانال‌های تلگرامه. پروکسی‌ها تو فایل `proxy.txt` ذخیره می‌شن و هر 6 ساعت به‌صورت خودکار به‌روزرسانی می‌شن.

## درباره پروژه

این اسکریپت با استفاده از `requests` و `BeautifulSoup` پروکسی‌های MTProto رو از منابع متنی (مثل فایل‌های خام گیت‌هاب) و صفحات وب کانال‌های تلگرام (`t.me/s/...`) جمع‌آوری می‌کنه. پروکسی‌های تکراری حذف می‌شن و نتیجه تو فایل `proxy.txt` ذخیره می‌شه. فرآیند به‌صورت خودکار با **GitHub Actions** هر 6 ساعت اجرا می‌شه.

## ویژگی‌ها
- جمع‌آوری پروکسی از منابع متنی و کانال‌های تلگرام
- به‌روزرسانی خودکار هر 6 ساعت
- حذف پروکسی‌های تکراری
- بدون نیاز به سرور یا API تلگرام
- مناسب برای کاربرانی که به دنبال پروکسی‌های MTProto فعال هستن

## پیش‌نیازها
- پایتون 3.9
- کتابخونه‌های مورد نیاز: `requests`, `beautifulsoup4`, `pytz`
- فایل `requirements.txt` شامل تمام وابستگی‌هاست.

## نحوه استفاده
1. فایل `proxy.txt` رو از [اینجا](proxy.txt) دانلود کنید.
2. لینک‌های پروکسی (با فرمت `tg://proxy?...`) رو تو کلاینت تلگرام خودتون وارد کنید.
3. برای کپی کردن پروکسی‌های زیر، روی لینک تو ستون "لینک پروکسی" لمس طولانی کنید و گزینه "Copy" رو انتخاب کنید، سپس تو تلگرام پیست کنید.
4. برای به‌روزرسانی دستی، به تب **Actions** تو مخزن برید و روی **Run workflow** کلیک کنید.

## منابع پروکسی
- **منابع متنی**:
  - [MahsaNetConfigTopic](https://raw.githubusercontent.com/MahsaNetConfigTopic/proxy/main/proxies.txt)
  - [ALIILAPRO/MTProtoProxy](https://raw.githubusercontent.com/ALIILAPRO/MTProtoProxy/main/proxy-list.txt)
- **کانال‌های تلگرام**:
  - iporoto, HiProxy, iproxy, iRoProxy, proxyforopeta, IRN_Proxy, MProxy_ir, ProxyHagh, PyroProxy, ProxyMTProto, MTPro_XYZ, vpns, mtmvpn

## نمونه پروکسی‌ها
جدول زیر 30 پروکسی نمونه از فایل `proxy.txt` رو نشون می‌ده. برای کپی کردن لینک پروکسی، روی متن تو ستون "لینک پروکسی" لمس طولانی کنید و "Copy" رو انتخاب کنید:

| #  | سرور (Server)       | پورت (Port) | وضعیت     | لینک پروکسی                     |
|----|---------------------|-------------|-----------|---------------------------------|
| 1 | 518.8-58-185.ir | 443 | فعال | `tg://proxy?server=518.8-58-185.ir&port=443&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 2 | 91.99.178.38 | 888 | فعال | `tg://proxy?server=91.99.178.38&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 8.215.196.24 | 443 | فعال | `tg://proxy?server=8.215.196.24&port=443&secret=eeb1a24d30c150f2de60fa4d8b1c61ab1d617a7572652e6d6963726f736f66742e636f6d` |
| 4 | 3.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=3.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 95.164.119.4 | 155 | فعال | `tg://proxy?server=95.164.119.4&port=155&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 6 | 77.246.105.56 | 85 | فعال | `tg://proxy?server=77.246.105.56&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 7 | 77.238.233.217 | 443 | فعال | `tg://proxy?server=77.238.233.217&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29tفیلترشکن` |
| 8 | Yoast.harcibasheokeye.ir | 918 | فعال | `tg://proxy?server=Yoast.harcibasheokeye.ir&port=918&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)__` |
| 9 | response.cinere.info | 443 | فعال | `tg://proxy?server=response.cinere.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | Online.harcibasheokeye.ir | 987 | فعال | `tg://proxy?server=Online.harcibasheokeye.ir&port=987&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 11 | 142.132.201.236 | 23 | فعال | `tg://proxy?server=142.132.201.236&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 12 | mtproto.vaheed.net | 2028 | فعال | `tg://proxy?server=mtproto.vaheed.net&port=2028&secret=dd2028b5afa0e6d701acec3cd9bb8a902b` |
| 13 | 188.245.185.185 | 551 | فعال | `tg://proxy?server=188.245.185.185&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 14 | 185.157.214.109 | 443 | فعال | `tg://proxy?server=185.157.214.109&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 15 | 204.76.203.40 | 443 | فعال | `tg://proxy?server=204.76.203.40&port=443&secret=15115115115115115115115115115115` |
| 16 | 157.180.84.199 | 888 | فعال | `tg://proxy?server=157.180.84.199&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 17 | 151.244.42.17 | 85 | فعال | `tg://proxy?server=151.244.42.17&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 18 | 77.238.239.178 | 443 | فعال | `tg://proxy?server=77.238.239.178&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)‌|‌[ایرانسل](https://t.me/proxy?server=212.34.139.251` |
| 19 | 142.132.210.168 | 23 | فعال | `tg://proxy?server=142.132.210.168&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 20 | 62.60.177.162 | 443 | فعال | `tg://proxy?server=62.60.177.162&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 21 | 151.244.85.77 | 343 | فعال | `tg://proxy?server=151.244.85.77&port=343&secret=7td9tD7jch8Py0Ck/2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 22 | 185.121.233.89 | 443 | فعال | `tg://proxy?server=185.121.233.89&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 23 | 157.180.127.223 | 8888 | فعال | `tg://proxy?server=157.180.127.223&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 24 | Berke.Wikimoon.sale | 443 | فعال | `tg://proxy?server=Berke.Wikimoon.sale&port=443&secret=7jK5IN_7UWQwKOL2uHjU6sFkbXl3ZWIuY2xvdWRmcm9udC5uZXQ` |
| 25 | daemi1.fanar.info | 443 | فعال | `tg://proxy?server=daemi1.fanar.info&port=443&secret=FgMBAgABAAH8AwOG4kw63Q==` |
| 26 | 78.46.70.120 | 3784 | فعال | `tg://proxy?server=78.46.70.120&port=3784&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 27 | 176.65.128.50 | 155 | فعال | `tg://proxy?server=176.65.128.50&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d|[پروکسی](tg://proxy?server=176.65.128.51` |
| 28 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info | 777 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info&port=777&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 29 | systemfull.gjesus.info | 443 | فعال | `tg://proxy?server=systemfull.gjesus.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 30 | 87.248.132.19 | 85 | فعال | `tg://proxy?server=87.248.132.19&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D)`` |


> **توجه**: این جدول فقط برای نمایش نمونه‌ست. برای دسترسی به همه پروکسی‌های به‌روز، فایل [proxy.txt](proxy.txt) رو دانلود کنید.

## مشارکت
از مشارکت شما استقبال می‌کنیم! اگه ایده‌ای برای بهبود اسکریپت دارید یا می‌خواید منابع جدیدی اضافه کنید:
1. یه **Issue** تو مخزن باز کنید.
2. یا یه **Pull Request** با تغییرات پیشنهادی بفرستید.

## لایسنس
این پروژه تحت [لایسنس MIT](LICENSE) منتشر شده.

## لینک‌های مفید
- 📄 [لیست پروکسی‌ها](proxy.txt)
- 🚀 [وضعیت GitHub Actions](https://github.com/Poriya58p/telegram-proxy-scraper/actions)
- ⭐ [ما رو ستاره بدید!](https://github.com/Poriya58p/telegram-proxy-scraper)

## Stargazers در گذر زمان
[![Stargazers over time](https://starchart.cc/Poriya58p/telegram-proxy-scraper.svg?variant=adaptive)](https://starchart.cc/Poriya58p/telegram-proxy-scraper)

---

سپاس از استفاده از **Telegram Proxy Scraper**! اگه سؤالی دارید، تو بخش Issues مطرح کنید. 🌟
