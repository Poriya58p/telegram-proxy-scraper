# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 12 July 2025, 06:28 UTC (به وقت ایران: 09:58)

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
| 1 | 95.169.173.12 | 85 | فعال | `tg://proxy?server=95.169.173.12&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 2 | 62.60.178.1 | 8888 | فعال | `tg://proxy?server=62.60.178.1&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____` |
| 3 | 49.12.38.200 | 155 | فعال | `tg://proxy?server=49.12.38.200&port=155&secret=dd1603010200010001fc030386e24c3add` |
| 4 | bede6.co.uk | 443 | فعال | `tg://proxy?server=bede6.co.uk&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | darknamikonina.beramaqhyou.cyou | 443 | فعال | `tg://proxy?server=darknamikonina.beramaqhyou.cyou&port=443&secret=eee6607B90889CC60719D2170CB2851962737465616D706F77657265642E636F6D)__` |
| 6 | 108.181.121.217 | 333 | فعال | `tg://proxy?server=108.181.121.217&port=333&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 91.220.113.78 | 65531 | فعال | `tg://proxy?server=91.220.113.78&port=65531&secret=dda4669a2bc220c8898111725adf3833e2` |
| 8 | rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info | 777 | فعال | `tg://proxy?server=rightel.irancell.irib.snapp.digikala.cloud.iranian.irib.ahmadp206.namakdarya.info&port=777&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | 103.35.189.118 | 8888 | فعال | `tg://proxy?server=103.35.189.118&port=8888&secret=eed0d6e111bada5511fcce9584deadbeef6170706c652e636f6d**` |
| 10 | 176.65.135.57 | 220 | فعال | `tg://proxy?server=176.65.135.57&port=220&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 11 | 93.88.205.25 | 888 | فعال | `tg://proxy?server=93.88.205.25&port=888&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 12 | 62.60.179.156 | 443 | فعال | `tg://proxy?server=62.60.179.156&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |
| 13 | 62.60.179.176 | 343 | فعال | `tg://proxy?server=62.60.179.176&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 14 | 1199.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=1199.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 8443.iropt-f.ir | 443 | فعال | `tg://proxy?server=8443.iropt-f.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 16 | 14.102.10.171 | 85 | فعال | `tg://proxy?server=14.102.10.171&port=85&secret=7gAA8A8Pd1VV__9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 17 | 14.102.10.154 | 8443 | فعال | `tg://proxy?server=14.102.10.154&port=8443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 18 | lock.link-a6.ir | 443 | فعال | `tg://proxy?server=lock.link-a6.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 19 | 87.248.132.33 | 200 | فعال | `tg://proxy?server=87.248.132.33&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 20 | www.vsmusic.ir | 888 | فعال | `tg://proxy?server=www.vsmusic.ir&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t```` |
| 21 | 91.99.172.152 | 8888 | فعال | `tg://proxy?server=91.99.172.152&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29` |
| 22 | 177.159.164.159 | 2717 | فعال | `tg://proxy?server=177.159.164.159&port=2717&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 136.243.146.237 | 443 | فعال | `tg://proxy?server=136.243.146.237&port=443&secret=EERighJJvXrFGRMCIMJdCQ` |
| 24 | 79.172.228.10 | 700 | فعال | `tg://proxy?server=79.172.228.10&port=700&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 25 | 103.161.34.217 | 65 | فعال | `tg://proxy?server=103.161.34.217&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 26 | 91.99.100.55 | 155 | فعال | `tg://proxy?server=91.99.100.55&port=155&secret=ddec742282124f04d318551341ead76457` |
| 27 | 5.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info | 8888 | فعال | `tg://proxy?server=5.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 28 | 46.62.144.121 | 70 | فعال | `tg://proxy?server=46.62.144.121&port=70&secret=7gAA8A8Pd1VV____9QBuLmktLXd-Z28tLS0=` |
| 29 | 47.242.139.194 | 443 | فعال | `tg://proxy?server=47.242.139.194&port=443&secret=eed3cdd752709154ebbcecb6be4b5ed4f2617a7572652e6d6963726f736f66742e636f6d` |
| 30 | 8.213.228.13 | 443 | فعال | `tg://proxy?server=8.213.228.13&port=443&secret=eef2cbc7ed088c732f9858b39443e181a3617a7572652e6d6963726f736f66742e636f6d` |


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
