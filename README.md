# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 14 July 2025, 01:48 UTC (به وقت ایران: 05:18)

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
| 1 | 185.95.159.231 | 9741 | فعال | `tg://proxy?server=185.95.159.231&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 2 | 44655.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=44655.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 62.60.178.55 | 443 | فعال | `tg://proxy?server=62.60.178.55&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|` |
| 4 | 79.172.228.29 | 70 | فعال | `tg://proxy?server=79.172.228.29&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 5 | 109.104.154.250 | 443 | فعال | `tg://proxy?server=109.104.154.250&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**` |
| 6 | 157.180.125.80 | 8888 | فعال | `tg://proxy?server=157.180.125.80&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 7 | optimal.irpower-f.ir | 443 | فعال | `tg://proxy?server=optimal.irpower-f.ir&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 8 | home.cphosting.shop | 443 | فعال | `tg://proxy?server=home.cphosting.shop&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 213.133.110.151 | 8423 | فعال | `tg://proxy?server=213.133.110.151&port=8423&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 10 | 00600.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=00600.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t**` |
| 11 | 151.244.85.15 | 70 | فعال | `tg://proxy?server=151.244.85.15&port=70&secret=7gffffffff_f_Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 12 | 9494.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=9494.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____` |
| 13 | 45.153.33.47 | 8888 | فعال | `tg://proxy?server=45.153.33.47&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 14 | api.abineirn5.ir | 70 | فعال | `tg://proxy?server=api.abineirn5.ir&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 15 | sibilkoloft.technote.ir | 443 | فعال | `tg://proxy?server=sibilkoloft.technote.ir&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 16 | 62.60.176.10 | 443 | فعال | `tg://proxy?server=62.60.176.10&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)‌|‌[همراه](https://t.me/proxy?server=62.60.179.221` |
| 17 | 157.180.122.194 | 551 | فعال | `tg://proxy?server=157.180.122.194&port=551&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 18 | 93.88.205.2 | 888 | فعال | `tg://proxy?server=93.88.205.2&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 19 | 77.248.132.96 | 200 | فعال | `tg://proxy?server=77.248.132.96&port=200&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 20 | 157.180.67.240 | 443 | فعال | `tg://proxy?server=157.180.67.240&port=443&secret=iORid5lJ237IiBMGYMQMdw==` |
| 21 | 213.176.92.143 | 443 | فعال | `tg://proxy?server=213.176.92.143&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 22 | web.parsa-learning.ir. | 443 | فعال | `tg://proxy?server=web.parsa-learning.ir.&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 78.47.77.74 | 443 | فعال | `tg://proxy?server=78.47.77.74&port=443&secret=0c30628212cbbd7ac519130205525d15` |
| 24 | 01111.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=01111.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 25 | 157.180.46.166 | 8888 | فعال | `tg://proxy?server=157.180.46.166&port=8888&secret=DD1603010200010001fc030386e24c3add` |
| 26 | Focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.info. | 443 | فعال | `tg://proxy?server=Focos-mokos.berlino-landcvixo.yokohama-1borino.eromatic.info.&port=443&secret=iORid5lJ237IiBMGYMQMdw==` |
| 27 | 176.65.128.50 | 155 | فعال | `tg://proxy?server=176.65.128.50&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 28 | 151.244.85.32 | 70 | فعال | `tg://proxy?server=151.244.85.32&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6` |
| 29 | irangodrati.co.uk. | 443 | فعال | `tg://proxy?server=irangodrati.co.uk.&port=443&secret=7s8J5YYVhvOdr-WqHy_58gVtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 30 | 185.222.28.151 | 23 | فعال | `tg://proxy?server=185.222.28.151&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==` |


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
