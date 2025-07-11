# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 11 July 2025, 18:28 UTC (به وقت ایران: 21:58)

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
| 1 | bomb.abineirn4.ir | 70 | فعال | `tg://proxy?server=bomb.abineirn4.ir&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 2 | 88.198.201.239 | 155 | فعال | `tg://proxy?server=88.198.201.239&port=155&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d|` |
| 3 | 88.99.103.117 | 443 | فعال | `tg://proxy?server=88.99.103.117&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 4 | 151.244.85.63 | 70 | فعال | `tg://proxy?server=151.244.85.63&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 5 | 103.161.34.230 | 85 | فعال | `tg://proxy?server=103.161.34.230&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 6 | 87.248.132.17 | 343 | فعال | `tg://proxy?server=87.248.132.17&port=343&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)**` |
| 7 | 5.35.70.114 | 443 | فعال | `tg://proxy?server=5.35.70.114&port=443&secret=ee07df7df7df7dfffffdfffffffffffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 8 | 167.235.65.93 | 8888 | فعال | `tg://proxy?server=167.235.65.93&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 9 | qoud.link-a4.ir | 443 | فعال | `tg://proxy?server=qoud.link-a4.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 10 | qavi.cphosting.shop | 443 | فعال | `tg://proxy?server=qavi.cphosting.shop&port=443&secret=7td9tD7jch8Py0Ck/2O1zSdtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | static.238.151.62.46.clients.your-server.de. | 443 | فعال | `tg://proxy?server=static.238.151.62.46.clients.your-server.de.&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 12 | LIVE.irpower-b.ir | 443 | فعال | `tg://proxy?server=LIVE.irpower-b.ir&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 13 | 94.130.131.162 | 2908 | فعال | `tg://proxy?server=94.130.131.162&port=2908&secret=DDBighLLvXrFGRMCBVJdFQRueWVrdGFuZXQuY29t` |
| 14 | 79.172.228.53 | 70 | فعال | `tg://proxy?server=79.172.228.53&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 15 | leveldaemi.fiziotr.info | 443 | فعال | `tg://proxy?server=leveldaemi.fiziotr.info&port=443&secret=7hYDAQIAAQAB_AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 16 | 185.226.116.244 | 443 | فعال | `tg://proxy?server=185.226.116.244&port=443&secret=3b388d6a64d035b887b6491a3e143ae0` |
| 17 | 87.248.132.41 | 443 | فعال | `tg://proxy?server=87.248.132.41&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 18 | 91.99.237.50 | 8888 | فعال | `tg://proxy?server=91.99.237.50&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 19 | 176.65.135.81 | 443 | فعال | `tg://proxy?server=176.65.135.81&port=443&secret=7gAA8A8Pd1VV____9QBuLmlkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 20 | 46.62.138.9 | 8080 | فعال | `tg://proxy?server=46.62.138.9&port=8080&secret=7gAA8A8Pd1VV____9QBuLmktLXd3dy5nby0t` |
| 21 | 45.135.192.253 | 85 | فعال | `tg://proxy?server=45.135.192.253&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 22 | 95.216.22.207 | 443 | فعال | `tg://proxy?server=95.216.22.207&port=443&secret=iORid5lJ237IiBMGYMQMdw` |
| 23 | 157.180.120.251 | 23 | فعال | `tg://proxy?server=157.180.120.251&port=23&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 24 | 87.229.100.230 | 70 | فعال | `tg://proxy?server=87.229.100.230&port=70&secret=ee07df7df7df7dfffffdfffffffffffc07646869646570726F78792E636C6F756466726F6E742E6E6574` |
| 25 | bmw.hezarsh-mashal0.co.vjhkgttrrhks-sdcj.co.uk.pwkxjjrhks-skci.co.uk.pwkxjjrhks-ikcj.co.uk.fskxjjrhks-rkcr.co.uk.mstukxjjrhkss-jscj.co.uk. | 7443 | فعال | `tg://proxy?server=bmw.hezarsh-mashal0.co.vjhkgttrrhks-sdcj.co.uk.pwkxjjrhks-skci.co.uk.pwkxjjrhks-ikcj.co.uk.fskxjjrhks-rkcr.co.uk.mstukxjjrhkss-jscj.co.uk.&port=7443&secret=eeRighJJvXrFGRMCIMJdCQ)**` |
| 26 | 91.99.172.220 | 443 | فعال | `tg://proxy?server=91.99.172.220&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 27 | 91.99.163.152 | 443 | فعال | `tg://proxy?server=91.99.163.152&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 28 | 140.233.187.63 | 8080 | فعال | `tg://proxy?server=140.233.187.63&port=8080&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d` |
| 29 | 142.132.199.239 | 8443 | فعال | `tg://proxy?server=142.132.199.239&port=8443&secret=DDBighLLvXrFGRMCBVJdFQ==` |
| 30 | 1.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store | 8888 | فعال | `tg://proxy?server=1.df.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.brobalair.store&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |


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
