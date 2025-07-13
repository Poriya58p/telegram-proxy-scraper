# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 13 July 2025, 01:51 UTC (به وقت ایران: 05:21)

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
| 1 | 142.132.201.236 | 23 | فعال | `tg://proxy?server=142.132.201.236&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | 62.60.178.1 | 8888 | فعال | `tg://proxy?server=62.60.178.1&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 62.60.177.143 | 8443 | فعال | `tg://proxy?server=62.60.177.143&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 4 | 157.180.39.126 | 443 | فعال | `tg://proxy?server=157.180.39.126&port=443&secret=7HQighJPBNMYVRNB6tdkVw` |
| 5 | daem.fsaremi.info | 443 | فعال | `tg://proxy?server=daem.fsaremi.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 195.57.9.lll-lll.ir | 443 | فعال | `tg://proxy?server=195.57.9.lll-lll.ir&port=443&secret=eeXifpB2GBv9shh2kvi5lA==` |
| 7 | 138.201.196.220 | 8443 | فعال | `tg://proxy?server=138.201.196.220&port=8443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 8 | 91.99.155.165 | 343 | فعال | `tg://proxy?server=91.99.155.165&port=343&secret=ee2e90d6ea3a0b17e371520fe2a2a40bd47777772e636c6f7564666c6172652e636f6d` |
| 9 | 37.203.37.16 | 443 | فعال | `tg://proxy?server=37.203.37.16&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 140.233.187.82 | 4030 | فعال | `tg://proxy?server=140.233.187.82&port=4030&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)/[ایرانسل](https://t.me/proxy?server=140.233.187.136` |
| 11 | iran-vatan.magalaiash.info | 443 | فعال | `tg://proxy?server=iran-vatan.magalaiash.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 12 | 91.99.201.44 | 443 | فعال | `tg://proxy?server=91.99.201.44&port=443&secret=eec862057ba49a7ecdf0ad4eb44cd5bb11646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 13 | 89.116.246.201 | 443 | فعال | `tg://proxy?server=89.116.246.201&port=443&secret=ee146231426d22b827d0f764cbe6f619566769746875622e636f6d` |
| 14 | 62.60.178.33 | 443 | فعال | `tg://proxy?server=62.60.178.33&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 15 | 91.99.173.122 | 443 | فعال | `tg://proxy?server=91.99.173.122&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 16 | 45.153.33.47 | 8888 | فعال | `tg://proxy?server=45.153.33.47&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | ir.brobalair.ink | 8888 | فعال | `tg://proxy?server=ir.brobalair.ink&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 18 | 62.60.178.104 | 443 | فعال | `tg://proxy?server=62.60.178.104&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 19 | 140.233.187.90 | 200 | فعال | `tg://proxy?server=140.233.187.90&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)|` |
| 20 | 87.248.132.96 | 200 | فعال | `tg://proxy?server=87.248.132.96&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 21 | 62.60.177.70 | 443 | فعال | `tg://proxy?server=62.60.177.70&port=443&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 22 | 79.172.228.207 | 70 | فعال | `tg://proxy?server=79.172.228.207&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 23 | 62.60.178.104 | 443 | فعال | `tg://proxy?server=62.60.178.104&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 24 | 103.215.221.15 | 8880 | فعال | `tg://proxy?server=103.215.221.15&port=8880&secret=ee6b8f9952c8f9c4e043cc3f24d0ae1bf47a756c612e6972` |
| 25 | 91.99.100.55 | 155 | فعال | `tg://proxy?server=91.99.100.55&port=155&secret=ddec742282124f04d318551341ead76457` |
| 26 | 108.181.71.97 | 465 | فعال | `tg://proxy?server=108.181.71.97&port=465&secret=ee082082082082082082082082082082087a716b746c77697561767676717174347962766776693774796f34686a6c357867667576706466366f746a69796367777162796d327161642e6f6e696f6e**` |
| 27 | 62.60.179.157 | 343 | فعال | `tg://proxy?server=62.60.179.157&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 28 | 66978828877833.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=66978828877833.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 29 | 91.99.195.49 | 443 | فعال | `tg://proxy?server=91.99.195.49&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 30 | 87.229.100.252 | 443 | فعال | `tg://proxy?server=87.229.100.252&port=443&secret=79e462821249bd7ac519130220c25d09` |


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
