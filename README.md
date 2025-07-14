# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 14 July 2025, 12:42 UTC (به وقت ایران: 16:12)

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
| 1 | 62.60.176.44 | 443 | فعال | `tg://proxy?server=62.60.176.44&port=443&secret=eeaadff8c1ff3ad6c38e1916853e4e49bb7777772e636c6f7564666c6172652e636f6d` |
| 2 | 157.180.124.237 | 8888 | فعال | `tg://proxy?server=157.180.124.237&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 3 | 5.e7777.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.zban-mas.info | 8888 | فعال | `tg://proxy?server=5.e7777.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.zban-mas.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 4 | 88.99.248.184 | 443 | فعال | `tg://proxy?server=88.99.248.184&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 5 | 87.229.100.230 | 70 | فعال | `tg://proxy?server=87.229.100.230&port=70&secret=ee07df7df7df7dfffffdfffffffffffc07646869646570726F78792E636C6F756466726F6E742E6E6574` |
| 6 | 88.99.251.22 | 443 | فعال | `tg://proxy?server=88.99.251.22&port=443&secret=EERighJJvXrFGRMCIMJdCQ` |
| 7 | 151.244.85.26 | 70 | فعال | `tg://proxy?server=151.244.85.26&port=70&secret=7gffffffff___f_______Adkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ==` |
| 8 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=eed77db43ee3721f0fcb40a4ff6` |
| 9 | 9933.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=9933.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 10 | 91.99.169.51 | 8888 | فعال | `tg://proxy?server=91.99.169.51&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29` |
| 11 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=7td9tD7jch8Py0Ck_2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 79.172.228.86 | 70 | فعال | `tg://proxy?server=79.172.228.86&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 13 | 77.139.140.52 | 4636 | فعال | `tg://proxy?server=77.139.140.52&port=4636&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 14 | namira-paris.nuremborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `tg://proxy?server=namira-paris.nuremborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 15 | 94.130.54.26 | 3443 | فعال | `tg://proxy?server=94.130.54.26&port=3443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 16 | 62.60.177.140 | 343 | فعال | `tg://proxy?server=62.60.177.140&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 17 | 5.255.111.230 | 443 | فعال | `tg://proxy?server=5.255.111.230&port=443&secret=7u0h9W68_BTpDShqHaz086xzMy5hbWF6b25hd3MuY29t` |
| 18 | 62.60.179.92 | 443 | فعال | `tg://proxy?server=62.60.179.92&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 19 | 151.244.42.5 | 85 | فعال | `tg://proxy?server=151.244.42.5&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 20 | 57.129.92.216 | 70 | فعال | `tg://proxy?server=57.129.92.216&port=70&secret=eeb7faf1ae6383bae0bdc3c4289759ce426d656469612e737465616d706f77657265642e636f6d` |
| 21 | Startup-active.custome-tobano.avadox-zhoan.info | 65 | فعال | `tg://proxy?server=Startup-active.custome-tobano.avadox-zhoan.info&port=65&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)**` |
| 22 | 146.103.97.75 | 8888 | فعال | `tg://proxy?server=146.103.97.75&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 95.217.77.168 | 443 | فعال | `tg://proxy?server=95.217.77.168&port=443&secret=iORid5lJ237IiBMGYMQMdw` |
| 24 | 79.172.228.61 | 70 | فعال | `tg://proxy?server=79.172.228.61&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 25 | 45.129.199.227 | 443 | فعال | `tg://proxy?server=45.129.199.227&port=443&secret=EE100404ff0f48064fffffff9001b8696d696d656469612e737465616d706f77657265642e636f6d` |
| 26 | 44655.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=44655.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 27 | 94.130.131.162 | 2908 | فعال | `tg://proxy?server=94.130.131.162&port=2908&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 28 | 62.60.179.82 | 443 | فعال | `tg://proxy?server=62.60.179.82&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 29 | 65.109.190.107 | 2053 | فعال | `tg://proxy?server=65.109.190.107&port=2053&secret=7t57_8BlqwAAAAAAAAAAAABfXy13d3cuZm9fX18tLQ==)__` |
| 30 | 47.81.34.45 | 443 | فعال | `tg://proxy?server=47.81.34.45&port=443&secret=ee9a1b0db3bada2fae31f14782603d42b2617a7572652e6d6963726f736f66742e636f6d` |


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
