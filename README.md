# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 11 July 2025, 06:31 UTC (به وقت ایران: 10:01)

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
| 1 | 87.248.132.188 | 155 | فعال | `tg://proxy?server=87.248.132.188&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ**` |
| 2 | 91.99.125.184 | 888 | فعال | `tg://proxy?server=91.99.125.184&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 157.180.80.209 | 443 | فعال | `tg://proxy?server=157.180.80.209&port=443&secret=1603010200010001fc030386e24c3add` |
| 4 | 212.34.141.71 | 443 | فعال | `tg://proxy?server=212.34.141.71&port=443&secret=1320PuNyHw_LQKT_Y7XNJw` |
| 5 | 116.202.83.134 | 404 | فعال | `tg://proxy?server=116.202.83.134&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 6 | 195.201.240.32 | 404 | فعال | `tg://proxy?server=195.201.240.32&port=404&secret=eeNEgYdJvXrFGRMCIMJdCQ==` |
| 7 | 91.99.170.203 | 888 | فعال | `tg://proxy?server=91.99.170.203&port=888&secret=ee0c30628212cbbd7ac519130205525d1569612e737465616d706f77657265642e636f6d` |
| 8 | 62.60.178.218 | 8080 | فعال | `tg://proxy?server=62.60.178.218&port=8080&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 9 | Fuck-War.harcibasheokeye.ir | 110 | فعال | `tg://proxy?server=Fuck-War.harcibasheokeye.ir&port=110&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 11.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=11.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 1.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info | 8888 | فعال | `tg://proxy?server=1.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q**` |
| 12 | lock.link-a6.ir | 443 | فعال | `tg://proxy?server=lock.link-a6.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 13 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 14 | 172.99.188.74 | 443 | فعال | `tg://proxy?server=172.99.188.74&port=443&secret=ee1603010200010001fc030386e24c3add64726f70626f782e636f6d` |
| 15 | 79.172.228.82 | 70 | فعال | `tg://proxy?server=79.172.228.82&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D|[پروکسی](https://t.me/proxy?server=79.172.228.201` |
| 16 | 91.99.53.223 | 70 | فعال | `tg://proxy?server=91.99.53.223&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 17 | 62.60.177.75 | 443 | فعال | `tg://proxy?server=62.60.177.75&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 18 | https.link-a1.ir | 443 | فعال | `tg://proxy?server=https.link-a1.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 19 | 91.99.171.213 | 8888 | فعال | `tg://proxy?server=91.99.171.213&port=8888&secret=7gAA8A8Pd1VV` |
| 20 | 151.244.85.52 | 70 | فعال | `tg://proxy?server=151.244.85.52&port=70&secret=ee00ff000fffff00fff5555ffffffffff56D656469612E737465616D706F77657265642E636F6D` |
| 21 | 78.47.77.74 | 443 | فعال | `tg://proxy?server=78.47.77.74&port=443&secret=0c30628212cbbd7ac519130205525d15` |
| 22 | 164.90.237.85 | 80 | فعال | `tg://proxy?server=164.90.237.85&port=80&secret=3V9HEDbXrf_pCKa76RM2stc` |
| 23 | vip.iranroad.info | 443 | فعال | `tg://proxy?server=vip.iranroad.info&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 24 | 79.172.228.201 | 70 | فعال | `tg://proxy?server=79.172.228.201&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 25 | 93.88.205.13 | 888 | فعال | `tg://proxy?server=93.88.205.13&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 26 | 87.248.132.44 | 200 | فعال | `tg://proxy?server=87.248.132.44&port=200&secret=79e344818749bd7ac519130220c25d09` |
| 27 | 91.99.173.122 | 443 | فعال | `tg://proxy?server=91.99.173.122&port=443&secret=7gD_` |
| 28 | 62.60.178.104 | 443 | فعال | `tg://proxy?server=62.60.178.104&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 29 | 87.248.132.23 | 70 | فعال | `tg://proxy?server=87.248.132.23&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 30 | 151.244.85.20 | 70 | فعال | `tg://proxy?server=151.244.85.20&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |


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
