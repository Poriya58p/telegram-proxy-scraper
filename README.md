# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 13 July 2025, 18:26 UTC (به وقت ایران: 21:56)

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
| 1 | 79.172.228.70 | 443 | فعال | `tg://proxy?server=79.172.228.70&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 2 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 3 | 46.62.129.6 | 8080 | فعال | `tg://proxy?server=46.62.129.6&port=8080&secret=7gAA8A8Pd1VV____9QBuLmktLXcuZ28tLS0=` |
| 4 | 65.109.214.153 | 2053 | فعال | `tg://proxy?server=65.109.214.153&port=2053&secret=7t57_8BlqwAAAAAAAAAAAABfXy13d3cuZm9fX18tLQ==)__` |
| 5 | 91.99.3.20 | 50836 | فعال | `tg://proxy?server=91.99.3.20&port=50836&secret=7gAAAAAAAAAAAAAAAAAAAABzdGVhbXBvd2VyZWQuY29t` |
| 6 | bmw.hezarsh-mashal0.co.vjhkgttrrhks-sdcj.co.uk.pwkxjjrhks-skci.co.uk.pwkxjjrhks-ikcj.co.uk.fskxjjrhks-rkcr.co.uk.mstukxjjrhkss-jscj.co.uk. | 7443 | فعال | `tg://proxy?server=bmw.hezarsh-mashal0.co.vjhkgttrrhks-sdcj.co.uk.pwkxjjrhks-skci.co.uk.pwkxjjrhks-ikcj.co.uk.fskxjjrhks-rkcr.co.uk.mstukxjjrhkss-jscj.co.uk.&port=7443&secret=eeRighJJvXrFGRMCIMJdCQ)**` |
| 7 | 11899.meli.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=11899.meli.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 65.108.12.153 | 65 | فعال | `tg://proxy?server=65.108.12.153&port=65&secret=1320PuNyHw_LQKT_Y7XNJw==` |
| 9 | 77.239.124.173 | 0443 | فعال | `tg://proxy?server=77.239.124.173&port=0443&secret=EE1603010200010007f0030386e24c3add646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 10 | 185.173.37.48 | 7879 | فعال | `tg://proxy?server=185.173.37.48&port=7879&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 5.199.168.13 | 443 | فعال | `tg://proxy?server=5.199.168.13&port=443&secret=ee603e1269308d7bec64b1e6b040fc76297777772e636c6f7564666c6172652e73686174656c2e6972616e63656c6c2e73616d616e74656c2e7463692e636f6d` |
| 12 | 94.130.48.73 | 8443 | فعال | `tg://proxy?server=94.130.48.73&port=8443&secret=DDBighLLvhhgexxguuuuuuXrFGRMCBVJdFQ==` |
| 13 | 79.172.228.94 | 70 | فعال | `tg://proxy?server=79.172.228.94&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 14 | 91.99.79.125 | 443 | فعال | `tg://proxy?server=91.99.79.125&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 15 | 8.8.8.8.dailygo.ir | 8081 | فعال | `tg://proxy?server=8.8.8.8.dailygo.ir&port=8081&secret=3Y39DPhdV6Lo3JGM1i6-9bE=` |
| 16 | 62.60.177.178 | 8443 | فعال | `tg://proxy?server=62.60.177.178&port=8443&secret=FgMBAgABAAfwAwOG4kw63Q` |
| 17 | 62.60.18.82 | 443 | فعال | `tg://proxy?server=62.60.18.82&port=443&secret=7hYDAQIAADAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3R123456lYW1wb3dlcmVkLmNvbQ` |
| 18 | static.230.165.99.91.clients.your-server.de. | 443 | فعال | `tg://proxy?server=static.230.165.99.91.clients.your-server.de.&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |
| 19 | 91.99.236.93 | 443 | فعال | `tg://proxy?server=91.99.236.93&port=443&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d)__` |
| 20 | oshin.sahihdorostok.info | 443 | فعال | `tg://proxy?server=oshin.sahihdorostok.info&port=443&secret=1603010200010001fc030386e24c3add)[**` |
| 21 | 151.244.85.73 | 70 | فعال | `tg://proxy?server=151.244.85.73&port=70&secret=ee0000f00f0f775555fffffff5006e2e696D656469612E737465616D706F77657265642E636F6D` |
| 22 | fpf027.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=fpf027.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 23 | 87.248.134.14 | 200 | فعال | `tg://proxy?server=87.248.134.14&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ)__` |
| 24 | asd.homayoon19.ir | 155 | فعال | `tg://proxy?server=asd.homayoon19.ir&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 25 | 87.248.132.59 | 155 | فعال | `tg://proxy?server=87.248.132.59&port=155&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 26 | 62.60.178.185 | 9880 | فعال | `tg://proxy?server=62.60.178.185&port=9880&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 27 | www.vsmusic.ir | 888 | فعال | `tg://proxy?server=www.vsmusic.ir&port=888&secret=7gwwYoISy716xRkTAgVSXRVpYS5zdGVhbXBvd2VyZWQuY29t```` |
| 28 | 62.60.179.213 | 9741 | فعال | `tg://proxy?server=62.60.179.213&port=9741&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 29 | 140.233.187.88 | 443 | فعال | `tg://proxy?server=140.233.187.88&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 30 | 62.60.179.156 | 443 | فعال | `tg://proxy?server=62.60.179.156&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ` |


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
