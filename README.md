# Telegram Proxy Scraper

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/downloads/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Poriya58p/telegram-proxy-scraper/issues)
[![Proxy Scraper Workflow](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml/badge.svg)](https://github.com/Poriya58p/telegram-proxy-scraper/actions/workflows/scraper.yml)
![GitHub last commit](https://img.shields.io/github/last-commit/Poriya58p/telegram-proxy-scraper)
![GitHub issues](https://img.shields.io/github/issues/Poriya58p/telegram-proxy-scraper)

**آخرین به‌روزرسانی پروکسی‌ها**: 13 July 2025, 12:38 UTC (به وقت ایران: 16:08)

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
| 1 | silvermantain.cinere.info | 443 | فعال | `tg://proxy?server=silvermantain.cinere.info&port=443&secret=ee1603010200010001fc030386e24c3add6d656469612e737465616d706f77657265642e636f6d` |
| 2 | 87.248.132.36 | 70 | فعال | `tg://proxy?server=87.248.132.36&port=70&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D)[**` |
| 3 | 138.201.195.175 | 443 | فعال | `tg://proxy?server=138.201.195.175&port=443&secret=104462821249bd7ac519130220c25d09` |
| 4 | 45.13.226.180 | 8882 | فعال | `tg://proxy?server=45.13.226.180&port=8882&secret=eed700433aba3557d5e83d82beb4ab735873332e616d617a6f6e6177732e636f6d` |
| 5 | 147.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=147.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 6 | 46.62.141.92 | 155 | فعال | `tg://proxy?server=46.62.141.92&port=155&secret=ee07df7df7df7dffdffc07646f776e6c6f61642e77696e646f77737570646174652e636f6d` |
| 7 | 62.60.179.65 | 443 | فعال | `tg://proxy?server=62.60.179.65&port=443&secret=7hAQEP8PSAZT____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 8 | 108.181.70.27 | 3443 | فعال | `tg://proxy?server=108.181.70.27&port=3443&secret=ee082082082082082082082082082082087472616e736c6174652e676f6f**` |
| 9 | 94.103.85.176 | 443 | فعال | `tg://proxy?server=94.103.85.176&port=443&secret=eed77db43ee3721f0fcb40a4ff63b5cd276D656469612E737465616D706F77657265642E636F6D` |
| 10 | Xplor.farda.95.37-68-174.ir | 443 | فعال | `tg://proxy?server=Xplor.farda.95.37-68-174.ir&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 11 | 9933.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=9933.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 12 | 213.109.147.37 | 85 | فعال | `tg://proxy?server=213.109.147.37&port=85&secret=ee0000f00f0f775555fffffff5006e2e69646F776E6C6F61642E77696E646F77737570646174652E636F6D` |
| 13 | vip.oliverpro.sbs | 8090 | فعال | `tg://proxy?server=vip.oliverpro.sbs&port=8090&secret=7twxtqyl4JpeItFZJ3sySvJzMy5hbWF6b25hd3MuY29t` |
| 14 | 49.12.38.200 | 155 | فعال | `tg://proxy?server=49.12.38.200&port=155&secret=dd1603010200010001fc030386e24c3add|[پروکسی](tg://proxy?server=62.60.178.253` |
| 15 | 94.130.54.26 | 3443 | فعال | `tg://proxy?server=94.130.54.26&port=3443&secret=0c30628212cbbd7ac519130205525d15` |
| 16 | 62.60.178.33 | 443 | فعال | `tg://proxy?server=62.60.178.33&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 17 | 193.3.190.53 | 85 | فعال | `tg://proxy?server=193.3.190.53&port=85&secret=ee0000f00f0f775555fffffff5006e2e696d656469612e737465616d706f77657265642e636f6d` |
| 18 | 87.248.132.199 | 200 | فعال | `tg://proxy?server=87.248.132.199&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 19 | 91.107.172.155 | 443 | فعال | `tg://proxy?server=91.107.172.155&port=443&secret=eeNEgYdJvXrFGRMCIMJdCQ` |
| 20 | In_Config_Tavasot_Armp_Sakhteh_Shodeh_Kos_Mikham_Please.my.to.my.to | 443 | فعال | `tg://proxy?server=In_Config_Tavasot_Armp_Sakhteh_Shodeh_Kos_Mikham_Please.my.to.my.to&port=443&secret=eec2bc7b595b2330dd2886a0f2447e73167777772e636c6f7564666c6172652e636f6d` |
| 21 | 91.84.109.244 | 443 | فعال | `tg://proxy?server=91.84.109.244&port=443&secret=ee00ff000fffff00fff5555ffffffffff56d656469612e737465616d706f77657265642e636f6d` |
| 22 | 87.248.132.55 | 200 | فعال | `tg://proxy?server=87.248.132.55&port=200&secret=eeNEgYdJvXrFGRMCIMJdCQ)**` |
| 23 | 109.107.165.75 | 443 | فعال | `tg://proxy?server=109.107.165.75&port=443&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 24 | 151.244.85.48 | 443 | فعال | `tg://proxy?server=151.244.85.48&port=443&secret=eed77db43ee3721f0fcb40a4ff6` |
| 25 | ntp.parsa-learning.ir. | 333 | فعال | `tg://proxy?server=ntp.parsa-learning.ir.&port=333&secret=7hAQEP8PSAZT____9QBuLmlpYS5zdGVhbXBvd2VyZWQuY29t` |
| 26 | 91.99.195.49 | 443 | فعال | `tg://proxy?server=91.99.195.49&port=443&secret=7gD_AA_wD_9VVf____VtZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 27 | 5555.meli.zban-mas.info | 8888 | فعال | `tg://proxy?server=5555.meli.zban-mas.info&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 28 | 176.65.131.221 | 85 | فعال | `tg://proxy?server=176.65.131.221&port=85&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t` |
| 29 | 62.60.178.195 | 443 | فعال | `tg://proxy?server=62.60.178.195&port=443&secret=7hYDAQIAAQAH8AMDhuJMOt1tZWRpYS5zdGVhbXBvd2VyZWQuY29tbWVkaWEuc3RlYW1wb3dlcmVkLmNvbQ)`` |
| 30 | www.nsnick.ir | 8888 | فعال | `tg://proxy?server=www.nsnick.ir&port=8888&secret=7gAA8A8Pd1VV____9QBuLmltZWRpYS5zdGVhbXBvd2VyZWQuY29t)__` |


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
