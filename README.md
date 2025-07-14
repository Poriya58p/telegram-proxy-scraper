# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 14 July 2025, 06:32 UTC (به وقت ایران: 10:02)

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
| 1 | 93.88.205.28 | 888 | فعال | `tg://proxy?server=93.88.205.28&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | htop.link-a4.ir | 443 | فعال | `tg://proxy?server=htop.link-a4.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 3 | 62.60.176.239 | 443 | فعال | `tg://proxy?server=62.60.176.239&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 4 | 185.222.28.15 | 8443 | فعال | `tg://proxy?server=185.222.28.15&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 5 | 352678f9909af538.bytezs.ir | 443 | فعال | `tg://proxy?server=352678f9909af538.bytezs.ir&port=443&secret=7gcgcgcgcgcgcgcgcgcgcgd0cmFuc2xhdGUuZ29v)__` |
| 6 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 7 | 91.99.160.185 | 443 | فعال | `tg://proxy?server=91.99.160.185&port=443&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0)__` |
| 8 | 1.ebimusic.xyz | 443 | فعال | `tg://proxy?server=1.ebimusic.xyz&port=443&secret=ebb8da4e7c85740279fba316460f7dfb` |
| 9 | 89.110.90.23 | 443 | فعال | `tg://proxy?server=89.110.90.23&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 10 | 91.99.170.107 | 443 | فعال | `tg://proxy?server=91.99.170.107&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 87.248.134.36 | 70 | فعال | `tg://proxy?server=87.248.134.36&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 12 | 195.26.224.171 | 443 | فعال | `tg://proxy?server=195.26.224.171&port=443&secret=eeXifpB2GBv9shh2kvi5lA==` |
| 13 | www.galacticfireworks.pro. | 888 | فعال | `tg://proxy?server=www.galacticfireworks.pro.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d` |
| 14 | 157.180.68.70 | 8888 | فعال | `tg://proxy?server=157.180.68.70&port=8888&secret=FgMBAgABAAH8AwOG4kw63` |
| 15 | 14.102.10.50 | 888 | فعال | `tg://proxy?server=14.102.10.50&port=888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 16 | 356700.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=356700.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | 157.180.43.253 | 8888 | فعال | `tg://proxy?server=157.180.43.253&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 18 | 95.217.77.168 | 443 | فعال | `tg://proxy?server=95.217.77.168&port=443&secret=7HQighJPBNMYVRNB6tdkVw==` |
| 19 | 157.180.120.251 | 23 | فعال | `tg://proxy?server=157.180.120.251&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 20 | rj5583.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=rj5583.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 21 | 46.249.110.245 | 9741 | فعال | `tg://proxy?server=46.249.110.245&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 22 | 62.60.178.2 | 8888 | فعال | `tg://proxy?server=62.60.178.2&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 01111.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=01111.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 24 | 91.99.166.4 | 8888 | فعال | `tg://proxy?server=91.99.166.4&port=8888&secret=7gAA8A8Pd1VV////9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 25 | 87.248.132.53 | 200 | فعال | `tg://proxy?server=87.248.132.53&port=200&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 26 | 157.180.95.196 | 888 | فعال | `tg://proxy?server=157.180.95.196&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 27 | www.sshputty.icu. | 888 | فعال | `tg://proxy?server=www.sshputty.icu.&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d****` |
| 28 | 62.60.176.217 | 9741 | فعال | `tg://proxy?server=62.60.176.217&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 29 | 116.203.81.58 | 8888 | فعال | `tg://proxy?server=116.203.81.58&port=8888&secret=1603010200010001fc030386e24c3add` |
| 30 | 91.99.166.111 | 443 | فعال | `tg://proxy?server=91.99.166.111&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |


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
