# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 12 July 2025, 12:37 UTC (به وقت ایران: 16:07)

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
| 1 | 93.88.205.14 | 888 | فعال | `tg://proxy?server=93.88.205.14&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 2 | 91.99.144.225 | 888 | فعال | `tg://proxy?server=91.99.144.225&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 185.117.0.115 | 8882 | فعال | `tg://proxy?server=185.117.0.115&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 4 | 14.102.10.50 | 888 | فعال | `tg://proxy?server=14.102.10.50&port=888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 5 | 37.49.224.199 | 8888 | فعال | `tg://proxy?server=37.49.224.199&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 78.46.240.236 | 443 | فعال | `tg://proxy?server=78.46.240.236&port=443&secret=0c30628212cbbd7ac519130205525d15` |
| 7 | www.vsmusic.ir | 888 | فعال | `tg://proxy?server=www.vsmusic.ir&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 103.215.221.15 | 8880 | فعال | `tg://proxy?server=103.215.221.15&port=8880&secret=ee6b8f9952c8f9c4e043cc3f24d0ae1bf47a756c612e6972` |
| 9 | 91.99.169.51 | 8888 | فعال | `tg://proxy?server=91.99.169.51&port=8888&secret=7gAA8A8Pd1VV` |
| 10 | soos-turk.nuremborg-hamborg.dodos-codam.jojo19.ir | 443 | فعال | `tg://proxy?server=soos-turk.nuremborg-hamborg.dodos-codam.jojo19.ir&port=443&secret=7gD_AA___wD_9VVf______VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 11 | 151.244.85.77 | 343 | فعال | `tg://proxy?server=151.244.85.77&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 12 | 5.e7777.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.zban-mas.info | 8888 | فعال | `tg://proxy?server=5.e7777.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.zban-mas.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 13 | web.parsa-learning.ir. | 443 | فعال | `tg://proxy?server=web.parsa-learning.ir.&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 14 | 62.60.178.95 | 9741 | فعال | `tg://proxy?server=62.60.178.95&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d**` |
| 15 | 104.248.26.196 | 443 | فعال | `tg://proxy?server=104.248.26.196&port=443&secret=eec80ff604fa45408f1d152624d3bffcf276616e2e6e616a76612e636f6d**` |
| 16 | 91.99.172.214 | 8888 | فعال | `tg://proxy?server=91.99.172.214&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | 87.248.132.44 | 200 | فعال | `tg://proxy?server=87.248.132.44&port=200&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 18 | 185.117.0.116 | 8882 | فعال | `tg://proxy?server=185.117.0.116&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 19 | 91.99.170.42 | 8888 | فعال | `tg://proxy?server=91.99.170.42&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 157.90.65.125 | 443 | فعال | `tg://proxy?server=157.90.65.125&port=443&secret=7gffffffff` |
| 21 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 22 | 142.132.201.236 | 23 | فعال | `tg://proxy?server=142.132.201.236&port=23&secret=79e344818749bd7ac519130220c25d09` |
| 23 | 157.180.46.166 | 8888 | فعال | `tg://proxy?server=157.180.46.166&port=8888&secret=dd1603010200010001fc030386e24c3add` |
| 24 | 176.65.135.60 | 23 | فعال | `tg://proxy?server=176.65.135.60&port=23&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 25 | 91.99.201.44 | 443 | فعال | `tg://proxy?server=91.99.201.44&port=443&secret=eec862057ba49a7ecdf0ad4eb44cd5bb11646f776e6c6f61642e77696e646f77737570646174652e636f6d)__` |
| 26 | In_Config_Tavasot_Armp_Sakhteh_Shodeh_Kos_Mikham_Please.my.to.my.to | 443 | فعال | `tg://proxy?server=In_Config_Tavasot_Armp_Sakhteh_Shodeh_Kos_Mikham_Please.my.to.my.to&port=443&secret=eec2bc7b595b2330dd2886a0f2447e73167777772e636c6f7564666c6172652e636f6d` |
| 27 | 109.107.165.75 | 443 | فعال | `tg://proxy?server=109.107.165.75&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 28 | 151.244.85.20 | 70 | فعال | `tg://proxy?server=151.244.85.20&port=70&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 29 | 5727.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=5727.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 30 | 62.60.179.56 | 443 | فعال | `tg://proxy?server=62.60.179.56&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |


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
