# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 11 July 2025, 01:43 UTC (به وقت ایران: 05:13)

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
| 1 | 62.60.178.195 | 443 | فعال | `tg://proxy?server=62.60.178.195&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)|` |
| 2 | 3.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store | 8888 | فعال | `tg://proxy?server=3.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 3 | 93.88.205.29 | 888 | فعال | `tg://proxy?server=93.88.205.29&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 4 | 1.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=1.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 176.65.135.55 | 23 | فعال | `tg://proxy?server=176.65.135.55&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 6 | 91.99.105.128 | 8888 | فعال | `tg://proxy?server=91.99.105.128&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 159.69.69.234 | 443 | فعال | `tg://proxy?server=159.69.69.234&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 8 | 88.198.108.29 | 443 | فعال | `tg://proxy?server=88.198.108.29&port=443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 9 | 62.60.179.139 | 443 | فعال | `tg://proxy?server=62.60.179.139&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 10 | 62.60.179.129 | 8080 | فعال | `tg://proxy?server=62.60.179.129&port=8080&secret=7nnjRIGHSb16xRkTAiDCXQltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 91.99.192.115 | 70 | فعال | `tg://proxy?server=91.99.192.115&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=)|` |
| 12 | HAME-netha.soren-mashin.ir. | 9741 | فعال | `tg://proxy?server=HAME-netha.soren-mashin.ir.&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D)__` |
| 13 | 185.222.28.10 | 8443 | فعال | `tg://proxy?server=185.222.28.10&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 14 | 95.217.14.172 | 443 | فعال | `tg://proxy?server=95.217.14.172&port=443&secret=7HQighJPBNMYVRNB6tdkVw` |
| 15 | 14.102.10.171 | 85 | فعال | `tg://proxy?server=14.102.10.171&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 16 | 151.244.42.3 | 85 | فعال | `tg://proxy?server=151.244.42.3&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 17 | 213.145.71.35 | 443 | فعال | `tg://proxy?server=213.145.71.35&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 18 | 62.60.179.28 | 7683 | فعال | `tg://proxy?server=62.60.179.28&port=7683&secret=7gAA8A8Pd1VV////9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 19 | 62.60.176.140 | 9741 | فعال | `tg://proxy?server=62.60.176.140&port=9741&secret=7gAA8A8Pd1VV////9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 151.244.50.27 | 70 | فعال | `tg://proxy?server=151.244.50.27&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 21 | 49.12.115.198 | 443 | فعال | `tg://proxy?server=49.12.115.198&port=443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 22 | halftime.parsintalk.ir | 443 | فعال | `tg://proxy?server=halftime.parsintalk.ir&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 77.238.233.217 | 443 | فعال | `tg://proxy?server=77.238.233.217&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 24 | 157.180.125.80 | 8888 | فعال | `tg://proxy?server=157.180.125.80&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 25 | 116.202.83.133 | 404 | فعال | `tg://proxy?server=116.202.83.133&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 26 | 87.248.132.23 | 70 | فعال | `tg://proxy?server=87.248.132.23&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 27 | 95.169.173.8 | 8443 | فعال | `tg://proxy?server=95.169.173.8&port=8443&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 28 | 46.62.151.238 | 443 | فعال | `tg://proxy?server=46.62.151.238&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 29 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 30 | 157.180.30.251 | 443 | فعال | `tg://proxy?server=157.180.30.251&port=443&secret=iORid5lJ237IiBMGYMQMdw` |


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
