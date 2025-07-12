# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 12 July 2025, 01:45 UTC (به وقت ایران: 05:15)

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
| 1 | dns.parsa-learning.ir. | 333 | فعال | `tg://proxy?server=dns.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 2 | 00900.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=00900.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 3 | 91.84.106.230 | 443 | فعال | `tg://proxy?server=91.84.106.230&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 4 | 99900.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=99900.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 5 | 5.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info | 8888 | فعال | `tg://proxy?server=5.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 6 | 356700.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=356700.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 7 | 9282.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=9282.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 77.139.140.52 | 4636 | فعال | `tg://proxy?server=77.139.140.52&port=4636&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 9 | dns.geohost.ir. | 443 | فعال | `tg://proxy?server=dns.geohost.ir.&port=443&secret=7nlnZpKACGMvBKgv9kq9q-5hcGkua2FyZW5ob3N0Lmly` |
| 10 | 91.99.115.105 | 888 | فعال | `tg://proxy?server=91.99.115.105&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 11 | 91.99.79.124 | 443 | فعال | `tg://proxy?server=91.99.79.124&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 62.60.179.172 | 343 | فعال | `tg://proxy?server=62.60.179.172&port=343&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 13 | 151.244.85.15 | 70 | فعال | `tg://proxy?server=151.244.85.15&port=70&secret=7gffffffff` |
| 14 | 65.109.176.53 | 443 | فعال | `tg://proxy?server=65.109.176.53&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 15 | 188.245.240.175 | 443 | فعال | `tg://proxy?server=188.245.240.175&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276d656469612e737465616d706f77657265642e636f6d)|` |
| 16 | 138.201.195.175 | 443 | فعال | `tg://proxy?server=138.201.195.175&port=443&secret=EERighJJvXrFGRMCIMJdCQ==` |
| 17 | 111.Ir.ir.ir.ir.ir.zban-mas.info | 8888 | فعال | `tg://proxy?server=111.Ir.ir.ir.ir.ir.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 18 | 84.200.125.64 | 155 | فعال | `tg://proxy?server=84.200.125.64&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQtY2RueWVrdGFuZXQuY29tZmFyYWthdi5jb212YW4ubmFqdmEuY29tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA)**` |
| 19 | 62.60.158.137 | 69 | فعال | `tg://proxy?server=62.60.158.137&port=69&secret=7pVZ3VtL_Wuy49KeR-ZTRlBtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 20 | 77711.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=77711.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 21 | 94.130.218.244 | 443 | فعال | `tg://proxy?server=94.130.218.244&port=443&secret=EERighJJvXrFGRMCIMJdCQ` |
| 22 | 176.65.135.71 | 443 | فعال | `tg://proxy?server=176.65.135.71&port=443&secret=7gAA8A8Pd1VV____9QBuLmlkb3dubG9hZC53aW5kb3dzdXBkYXRlLmNvbQ` |
| 23 | 103.161.34.217 | 65 | فعال | `tg://proxy?server=103.161.34.217&port=65&secret=eeNEgYdJvXrFGRMCIMJdCQ**` |
| 24 | 46.249.110.245 | 9741 | فعال | `tg://proxy?server=46.249.110.245&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 25 | mas.a27dh1.sbs | 8888 | فعال | `tg://proxy?server=mas.a27dh1.sbs&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 26 | 103.35.189.118 | 8888 | فعال | `tg://proxy?server=103.35.189.118&port=8888&secret=eed0d6e111bada5511fcce9584deadbeef6170706c652e636f6d` |
| 27 | 6.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info | 8888 | فعال | `tg://proxy?server=6.dfff.cloudflare.com.nokia.com.co.uk.do_yo.want_to.clash_with.this.www.microsoft.com.there_is_no.place_like.localhost.www.bing.com.count_with_me.cyou.net.digikala.com.www.enamad.ir.www.google.com.again_to_fight.everyone.i_am.the_internet.zban-df.info&port=8888&secret=FgMBAgABAAH8AwOG4kw63Q` |
| 28 | 62.60.178.1 | 8888 | فعال | `tg://proxy?server=62.60.178.1&port=8888&secret=7gAA8A8Pd1VV9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t____` |
| 29 | 104.248.84.27 | 443 | فعال | `tg://proxy?server=104.248.84.27&port=443&secret=15115115115115115115115115115115` |
| 30 | 8.215.196.24 | 443 | فعال | `tg://proxy?server=8.215.196.24&port=443&secret=eeb1a24d30c150f2de60fa4d8b1c61ab1d617a7572652e6d6963726f736f66742e636f6d` |


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
