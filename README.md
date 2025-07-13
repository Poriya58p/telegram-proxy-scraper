# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 13 July 2025, 06:29 UTC (به وقت ایران: 09:59)

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
| 1 | 185.21.14.158 | 443 | فعال | `tg://proxy?server=185.21.14.158&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 2 | 157.180.31.92 | 443 | فعال | `tg://proxy?server=157.180.31.92&port=443&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 3 | 93.88.205.36 | 85 | فعال | `tg://proxy?server=93.88.205.36&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 4 | 91.99.146.38 | 888 | فعال | `tg://proxy?server=91.99.146.38&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 157.180.93.115 | 443 | فعال | `tg://proxy?server=157.180.93.115&port=443&secret=7HQighJPBNMYVRNB6tdkVw==` |
| 6 | 14.102.10.177 | 85 | فعال | `tg://proxy?server=14.102.10.177&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 157.180.93.68 | 888 | فعال | `tg://proxy?server=157.180.93.68&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 8 | backend.chandplus.com. | 443 | فعال | `tg://proxy?server=backend.chandplus.com.&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5iYWNrZW5kLmNoYW5kcGx1cy5jb20` |
| 9 | 185.222.28.152 | 23 | فعال | `tg://proxy?server=185.222.28.152&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 10 | 94.130.52.104 | 3443 | فعال | `tg://proxy?server=94.130.52.104&port=3443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 11 | bede6.co.uk | 443 | فعال | `tg://proxy?server=bede6.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 87.248.132.55 | 200 | فعال | `tg://proxy?server=87.248.132.55&port=200&secret=79e344818749bd7ac519130220c25d09` |
| 13 | 87.248.132.18 | 85 | فعال | `tg://proxy?server=87.248.132.18&port=85&secret=7gAA8A8Pd1VV____9QBuLmlkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 14 | 87.248.132.188 | 155 | فعال | `tg://proxy?server=87.248.132.188&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ**` |
| 15 | 157.180.68.70 | 8888 | فعال | `tg://proxy?server=157.180.68.70&port=8888&secret=FgMBAgABAAH8AwOG4kw63` |
| 16 | 89.116.246.201 | 443 | فعال | `tg://proxy?server=89.116.246.201&port=443&secret=ee146231426d22b827d0f764cbe6f619566769746875622e636f6d` |
| 17 | 01111.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=01111.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | 87.248.132.96 | 200 | فعال | `tg://proxy?server=87.248.132.96&port=200&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 19 | 14.102.10.177 | 85 | فعال | `tg://proxy?server=14.102.10.177&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 49.13.145.84 | 443 | فعال | `tg://proxy?server=49.13.145.84&port=443&secret=3QAAAAAAAAAAAAAAAAAAAAA=` |
| 21 | 62.60.179.198 | 343 | فعال | `tg://proxy?server=62.60.179.198&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 22 | 79.172.228.239 | 70 | فعال | `tg://proxy?server=79.172.228.239&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 23 | 151.244.85.77 | 343 | فعال | `tg://proxy?server=151.244.85.77&port=343&secret=7td9tD7jch8Py0Ck/2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 24 | 44.201.28.97 | 443 | فعال | `tg://proxy?server=44.201.28.97&port=443&secret=ee858d42d1d9c56191cbe37c75b9568d527777772e636c6f7564666c6172652e636f6d` |
| 25 | 14.102.10.37 | 888 | فعال | `tg://proxy?server=14.102.10.37&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 26 | 91.99.169.201 | 8888 | فعال | `tg://proxy?server=91.99.169.201&port=8888&secret=7gAA8A8Pd1VV` |
| 27 | 151.244.85.66 | 85 | فعال | `tg://proxy?server=151.244.85.66&port=85&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 28 | 95.169.173.11 | 85 | فعال | `tg://proxy?server=95.169.173.11&port=85&secret=7gAA8A8Pd1VV____9QBuLmlmaXJlYmFzZWluc3RhbGxhdGlvbnMuZ29vZ2xlYXBpcy5jb20` |
| 29 | 199.59.243.228 | 443 | فعال | `tg://proxy?server=199.59.243.228&port=443&secret=3dpBFlW2hP6Hq_WOwiNeKBY` |
| 30 | 151.244.42.5 | 85 | فعال | `tg://proxy?server=151.244.42.5&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |


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
