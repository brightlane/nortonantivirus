#!/usr/bin/env python3
"""
BestAntivirusGuide — Best Antivirus + Norton Deals + Family Safety Hub
Site: https://brightlane.github.io/nortonantivirus/
Affiliate: https://track.dkhry.com/aff_c?offer_id=21781&aff_id=21885
Angles: #1 Best Antivirus 2026 | Norton Deals & Discounts | Protect Your Family Online
13 locales x 17,070+ pages
Run: python3 build.py
"""

import os, sys, subprocess, datetime, hashlib, time

now      = datetime.datetime.utcnow()
DATE_STR = now.strftime("%Y-%m-%d")
SYNC     = hashlib.md5(DATE_STR.encode()).hexdigest()[:8]
BASE_URL = "https://brightlane.github.io/nortonantivirus"
AFF      = "https://track.dkhry.com/aff_c?offer_id=21781&aff_id=21885"
YEAR     = now.year

LOCALES = [
    ("us","en","United States","USD","29.99"),
    ("ca","en","Canada","CAD","39.99"),
    ("gb","en","United Kingdom","GBP","24.99"),
    ("au","en","Australia","AUD","44.99"),
    ("nz","en","New Zealand","NZD","49.99"),
    ("jp","ja","Japan","JPY","3,600"),
    ("de","de","Germany","EUR","29.99"),
    ("es","es","Spain","EUR","29.99"),
    ("dk","da","Denmark","DKK","229"),
    ("mx","es","Mexico","MXN","599"),
    ("emea-en","en","EMEA","USD","29.99"),
    ("emea-fr","fr","EMEA","EUR","29.99"),
    ("emea-ar","ar","EMEA","USD","29.99"),
]

T = {
    "en": {"cta":"Try Norton Free — 30 Days","cta_short":"Try Free 30 Days →",
           "trust1":"✅ 30-Day Free Trial","trust2":"🔒 60-Day Money-Back",
           "trust3":"⭐ 50M+ Protected","trust4":"🏆 #1 Rated Antivirus",
           "sticky":"🛡️ Try Norton Free 30 Days →",
           "promo":"🎉 Limited Time: Get Norton 360 FREE for 30 Days — No Credit Card Required",
           "faq":"Frequently Asked Questions","related":"Related Pages",
           "disc":"This site contains affiliate links. We may earn a commission at no extra cost to you."},
    "fr": {"cta":"Essayez Norton Gratuit — 30 Jours","cta_short":"Essai Gratuit 30 Jours →",
           "trust1":"✅ 30 Jours Gratuits","trust2":"🔒 Remboursement 60 Jours",
           "trust3":"⭐ 50M+ Protégés","trust4":"🏆 Antivirus N°1",
           "sticky":"🛡️ Essayez Norton Gratuit 30 Jours →",
           "promo":"🎉 Norton 360 GRATUIT pendant 30 Jours",
           "faq":"Questions Fréquentes","related":"Pages Connexes",
           "disc":"Ce site contient des liens affiliés. Commission possible sans frais supplémentaires."},
    "de": {"cta":"Norton 30 Tage Kostenlos Testen","cta_short":"30 Tage Kostenlos →",
           "trust1":"✅ 30 Tage Kostenlos","trust2":"🔒 60-Tage Geld-Zurück",
           "trust3":"⭐ 50M+ Geschützt","trust4":"🏆 Antivirus Nr. 1",
           "sticky":"🛡️ Norton 30 Tage Kostenlos →",
           "promo":"🎉 Norton 360 30 Tage KOSTENLOS testen",
           "faq":"Häufige Fragen","related":"Verwandte Seiten",
           "disc":"Diese Seite enthält Affiliate-Links. Provision ohne Zusatzkosten möglich."},
    "es": {"cta":"Prueba Norton Gratis — 30 Días","cta_short":"Prueba Gratis 30 Días →",
           "trust1":"✅ 30 Días Gratis","trust2":"🔒 Devolución 60 Días",
           "trust3":"⭐ 50M+ Protegidos","trust4":"🏆 Antivirus N°1",
           "sticky":"🛡️ Prueba Norton Gratis 30 Días →",
           "promo":"🎉 Norton 360 GRATIS por 30 Días",
           "faq":"Preguntas Frecuentes","related":"Páginas Relacionadas",
           "disc":"Este sitio contiene enlaces de afiliados. Posible comisión sin costo adicional."},
    "da": {"cta":"Prøv Norton Gratis — 30 Dage","cta_short":"Prøv Gratis 30 Dage →",
           "trust1":"✅ 30 Dages Gratis","trust2":"🔒 60-Dages Pengeback",
           "trust3":"⭐ 50M+ Beskyttet","trust4":"🏆 Antivirus Nr. 1",
           "sticky":"🛡️ Prøv Norton Gratis 30 Dage →",
           "promo":"🎉 Norton 360 GRATIS i 30 Dage",
           "faq":"Ofte Stillede Spørgsmål","related":"Relaterede Sider",
           "disc":"Dette websted indeholder affilierede links."},
    "ja": {"cta":"Norton 30日間無料トライアル","cta_short":"30日間無料で試す →",
           "trust1":"✅ 30日間無料","trust2":"🔒 60日間返金保証",
           "trust3":"⭐ 5000万人以上保護","trust4":"🏆 ウイルス対策No.1",
           "sticky":"🛡️ Norton 30日間無料で試す →",
           "promo":"🎉 Norton 360を30日間無料でお試しください",
           "faq":"よくある質問","related":"関連ページ",
           "disc":"本サイトにはアフィリエイトリンクが含まれています。"},
    "ar": {"cta":"جرب نورتون مجاناً 30 يوماً","cta_short":"جرب مجاناً 30 يوماً ←",
           "trust1":"✅ 30 يوماً مجاناً","trust2":"🔒 ضمان استرداد 60 يوماً",
           "trust3":"⭐ أكثر من 50 مليون محمي","trust4":"🏆 أفضل برنامج مكافحة فيروسات",
           "sticky":"🛡️ جرب نورتون مجاناً 30 يوماً ←",
           "promo":"🎉 نورتون 360 مجاناً لمدة 30 يوماً",
           "faq":"الأسئلة الشائعة","related":"صفحات ذات صلة",
           "disc":"يحتوي هذا الموقع على روابط تابعة."},
}
for lc, lang, *_ in LOCALES:
    if lang not in T:
        T[lang] = T["en"]

US_STATES = [
    ("alabama","Alabama","AL"),("alaska","Alaska","AK"),("arizona","Arizona","AZ"),
    ("arkansas","Arkansas","AR"),("california","California","CA"),("colorado","Colorado","CO"),
    ("connecticut","Connecticut","CT"),("delaware","Delaware","DE"),("florida","Florida","FL"),
    ("georgia","Georgia","GA"),("hawaii","Hawaii","HI"),("idaho","Idaho","ID"),
    ("illinois","Illinois","IL"),("indiana","Indiana","IN"),("iowa","Iowa","IA"),
    ("kansas","Kansas","KS"),("kentucky","Kentucky","KY"),("louisiana","Louisiana","LA"),
    ("maine","Maine","ME"),("maryland","Maryland","MD"),("massachusetts","Massachusetts","MA"),
    ("michigan","Michigan","MI"),("minnesota","Minnesota","MN"),("mississippi","Mississippi","MS"),
    ("missouri","Missouri","MO"),("montana","Montana","MT"),("nebraska","Nebraska","NE"),
    ("nevada","Nevada","NV"),("new-hampshire","New Hampshire","NH"),("new-jersey","New Jersey","NJ"),
    ("new-mexico","New Mexico","NM"),("new-york","New York","NY"),("north-carolina","North Carolina","NC"),
    ("north-dakota","North Dakota","ND"),("ohio","Ohio","OH"),("oklahoma","Oklahoma","OK"),
    ("oregon","Oregon","OR"),("pennsylvania","Pennsylvania","PA"),("rhode-island","Rhode Island","RI"),
    ("south-carolina","South Carolina","SC"),("south-dakota","South Dakota","SD"),
    ("tennessee","Tennessee","TN"),("texas","Texas","TX"),("utah","Utah","UT"),
    ("vermont","Vermont","VT"),("virginia","Virginia","VA"),("washington","Washington","WA"),
    ("west-virginia","West Virginia","WV"),("wisconsin","Wisconsin","WI"),("wyoming","Wyoming","WY"),
]

# ── ANGLE 1: BEST ANTIVIRUS CATEGORIES (20) ──────────────────────────────────
CATEGORIES = [
    ("best-antivirus","Best Antivirus","🏆",
     "After testing 30+ products, Norton 360 is the #1 antivirus of 2026. Top detection rates, most features, and the best value across every independent lab test.",
     ["What is the best antivirus in 2026?","Is Norton the number one antivirus?","Which antivirus has the highest detection rate?","Best antivirus for overall protection","Norton vs all competitors 2026"]),
    ("best-antivirus-windows","Best Antivirus for Windows","💻",
     "Norton 360 for Windows beats Windows Defender on every metric — detection rate, features, and performance impact. The best Windows antivirus in 2026.",
     ["Best antivirus for Windows 11","Is Norton better than Windows Defender?","Norton Windows performance impact","Best antivirus Windows 10","Norton vs Defender 2026"]),
    ("best-antivirus-mac","Best Antivirus for Mac","🍎",
     "Macs do get viruses. Norton 360 for Mac protects against Mac-specific threats, adware, and cross-platform malware with minimal performance impact.",
     ["Do Macs need antivirus?","Best antivirus for MacBook","Is Norton good for Mac?","Best free antivirus for Mac","Norton Mac review 2026"]),
    ("best-antivirus-iphone","Best Antivirus for iPhone","📱",
     "iOS security starts with VPN, dark web monitoring, and safe browsing. Norton Mobile Security covers all three for complete iPhone protection.",
     ["Does iPhone need antivirus?","Best security app for iPhone","Norton iPhone review","Best iOS security app 2026","Is Norton good for iPhone?"]),
    ("best-antivirus-android","Best Antivirus for Android","🤖",
     "Android is the most targeted mobile platform. Norton Mobile Security scans apps, blocks phishing, and secures WiFi for complete Android protection.",
     ["Best antivirus for Android 2026","Is Norton good for Android?","Free vs paid Android antivirus","Best Android security app","Norton Android review 2026"]),
    ("best-antivirus-family","Best Antivirus for Families","👨‍👩‍👧",
     "Norton 360 Deluxe covers 5 devices with parental controls, dark web monitoring, VPN, and LifeLock identity protection — the best family antivirus plan available.",
     ["Best family antivirus plan","Norton 360 family review","How many devices does Norton cover?","Best parental control antivirus","Antivirus for whole family 2026"]),
    ("best-antivirus-seniors","Best Antivirus for Seniors","👴",
     "Norton 360 is the easiest antivirus for seniors — automatic updates, simple interface, 24/7 phone support, and LifeLock to protect against elder fraud and scams.",
     ["Best antivirus for elderly","Is Norton easy for seniors?","Best antivirus for over 60","Norton seniors review","Simple antivirus for seniors 2026"]),
    ("best-antivirus-students","Best Antivirus for Students","🎓",
     "Students face phishing, public WiFi attacks, and ransomware. Norton 360 covers every threat for $2.49/mo — the best student antivirus deal in 2026.",
     ["Best antivirus for college students","Cheap antivirus for students","Norton student discount","Best cheap antivirus 2026","Antivirus for university students"]),
    ("best-antivirus-gaming","Best Antivirus for Gamers","🎮",
     "Norton 360 Silent Mode suspends notifications and optimizes resources during gaming so you stay protected without lag, stuttering, or pop-ups.",
     ["Best antivirus for gaming PC","Does Norton affect gaming performance?","Antivirus with gaming mode","Norton gaming mode review","Best lightweight antivirus gamers"]),
    ("best-antivirus-business","Best Antivirus for Business","💼",
     "Norton 360 protects multiple devices, remote workers, and sensitive business data with enterprise-grade security at consumer prices.",
     ["Best antivirus for small business","Norton business plans","Antivirus work from home","Best endpoint security SMB","Norton business review 2026"]),
    ("best-antivirus-budget","Best Budget Antivirus","💰",
     "Norton 360 Standard at $29.99/year is the best budget antivirus — full VPN, dark web monitoring, and password manager included at the lowest price.",
     ["Cheapest good antivirus","Best antivirus under $30","Norton cheapest plan","Budget antivirus 2026","Cheap antivirus with VPN"]),
    ("best-antivirus-multiple-devices","Best Antivirus Multiple Devices","📱💻",
     "Norton 360 Deluxe covers 5 devices. Norton 360 Advanced covers 10. One subscription for Windows, Mac, iPhone, Android, and tablet.",
     ["Best antivirus for multiple devices","Antivirus for all devices family","Norton 5 device plan","Best multi-device antivirus 2026","Family antivirus all devices"]),
    ("best-free-antivirus","Best Free vs Paid Antivirus","🆓",
     "Free antivirus misses ransomware, has no VPN, and often sells your data. Norton's 30-day free trial gives full protection before you pay a cent.",
     ["Best free antivirus 2026","Is free antivirus enough?","Norton free trial vs free antivirus","Why paid antivirus is better","Free antivirus risks 2026"]),
    ("best-antivirus-privacy","Best Antivirus for Privacy","🔒",
     "Norton 360 includes a no-log VPN, dark web monitoring, and ad tracker blocking — the most privacy-focused full-suite antivirus available.",
     ["Best antivirus for privacy","Antivirus with VPN dark web monitoring","Privacy-first antivirus 2026","Norton privacy features review","Best no-data-collection antivirus"]),
    ("best-antivirus-identity-theft","Best Antivirus Identity Protection","🆔",
     "Norton LifeLock is the only antivirus with built-in identity theft protection, credit monitoring, and up to $1M coverage for eligible losses.",
     ["Best antivirus with identity protection","Norton LifeLock review","Antivirus with identity theft","Best identity theft protection 2026","LifeLock antivirus bundle"]),
    ("best-antivirus-ransomware","Best Antivirus Ransomware Protection","🔐",
     "Norton uses behavioral AI to detect ransomware before encryption starts and cloud backup to restore files even if an attack succeeds.",
     ["Best ransomware protection 2026","Norton ransomware protection","Antivirus that stops ransomware","Best protection against ransomware","Does Norton stop ransomware?"]),
    ("best-antivirus-vpn","Best Antivirus with VPN","📡",
     "Norton 360 includes an unlimited no-log VPN with 2,000+ servers — better value than buying antivirus and VPN as separate products.",
     ["Best antivirus with built-in VPN","Norton VPN review 2026","Antivirus that includes VPN","Best VPN antivirus bundle 2026","Norton VPN speed test"]),
    ("best-antivirus-parental","Best Antivirus with Parental Controls","👨‍👩‍👧",
     "Norton Family lets parents set screen time limits, filter content, track location, and monitor app usage across every child's device.",
     ["Best antivirus parental controls","Norton Family review","Antivirus with parental controls","Best parental control software 2026","Norton Family vs Bark"]),
    ("best-antivirus-chromebook","Best Antivirus for Chromebook","🌐",
     "Norton Mobile Security protects Chromebooks from malicious apps, unsafe websites, and unsecured WiFi — available from the Google Play Store.",
     ["Best antivirus for Chromebook","Does Chromebook need antivirus?","Norton Chromebook review","Best security Chromebook 2026","Is Norton good for Chromebook?"]),
    ("best-antivirus-2026","Best Antivirus Software 2026","🥇",
     "Our complete ranking of the best antivirus software in 2026 — tested on detection rate, performance, features, price, and support. Norton wins.",
     ["Best antivirus 2026","Top antivirus software 2026","Number 1 antivirus 2026","Best antivirus review 2026","Which antivirus is best in 2026?"]),
]

CATEGORY_INTENTS = [
    ("review","review","expert review"),
    ("guide","complete guide","complete buying guide"),
    ("comparison","comparison","side by side comparison"),
    ("top-picks","top picks","ranked top picks"),
    ("free-trial","free trial","try free today"),
    ("download","download","how to download"),
    ("why-norton","why norton wins","why norton is best"),
    ("price","price","best price available"),
    ("features","features","key features list"),
    ("vs-free","vs free antivirus","paid vs free comparison"),
    ("for-beginners","for beginners","best for beginners"),
    ("worth-it","worth it","is it worth buying"),
    ("install","install guide","step by step install"),
    ("discount","discount","biggest discount available"),
    ("recommendation","recommendation","expert recommendation"),
    ("2026","2026 edition","best choice 2026"),
    ("rating","expert rating","independent expert rating"),
    ("test-results","test results","independent test results"),
    ("setup","setup guide","complete setup guide"),
    ("performance","performance","speed and performance test"),
    ("detection","detection rate","malware detection rate"),
    ("support","customer support","customer support review"),
    ("update","auto updates","automatic update guide"),
    ("lightweight","lightweight option","lightest option available"),
    ("award","award winning","award winning choice 2026"),
]

# ── ANGLE 4: DEALS & DISCOUNTS (15) ──────────────────────────────────────────
DEAL_TOPICS = [
    ("norton-deal","Norton Deal 2026","💸",
     "Get the best Norton 360 deal in 2026. Compare plans, find promo codes, and discover when Norton prices drop the most.",
     ["Where to find best Norton deal?","Norton discount 2026","How to get Norton cheapest?","Best time to buy Norton","Norton promo code 2026"]),
    ("norton-promo-code","Norton Promo Code","🎟️",
     "The latest Norton promo codes and discount links for 2026. Click through our affiliate link to automatically get the best available discount.",
     ["Norton promo code 2026","Norton coupon code","Norton discount link","Norton 70 percent off","Best Norton offer 2026"]),
    ("norton-cheapest-plan","Norton Cheapest Plan","💲",
     "Norton AntiVirus Plus at $19.99/year is the cheapest Norton plan. Norton 360 Standard adds a VPN for just $10 more — the best budget value.",
     ["What is cheapest Norton plan?","Norton AntiVirus Plus vs 360","Cheapest Norton with VPN","Norton entry level plan","Minimum Norton price"]),
    ("norton-renewal-deal","Norton Renewal Deal","🔄",
     "Norton renewal prices are higher than new customer prices. Here's how to get a renewal discount and avoid overpaying every year.",
     ["How to get Norton renewal discount?","Norton auto-renew price","Best Norton renewal deal","Norton renewal too expensive","Cancel and rebuy Norton trick"]),
    ("norton-black-friday","Norton Black Friday Deal","🖤",
     "Norton Black Friday deals offer up to 70% off. Historically the biggest Norton sale of the year — plan ahead to save the most.",
     ["Norton Black Friday 2026","Norton Cyber Monday deal","Best Norton deal of the year","Norton holiday sale","When does Norton go on sale?"]),
    ("norton-free-trial","Norton Free Trial Guide","🆓",
     "How to get Norton 360 completely free for 30 days. No credit card required. Full access to every premium feature during the trial period.",
     ["How to get Norton free trial?","Norton 30 day free trial","Norton free no credit card","Try Norton before buying","Norton trial period"]),
    ("norton-plans-price","Norton Plans Price Comparison","📊",
     "Compare all 6 Norton 360 plans side by side — price, devices, features, and which plan gives you the best value for money in 2026.",
     ["Norton plan comparison 2026","Which Norton plan is best?","Norton 360 Deluxe vs Advanced","All Norton plans explained","Best value Norton plan"]),
    ("norton-upgrade-deal","Norton Upgrade Deal","⬆️",
     "Upgrading from a basic Norton plan to Deluxe or Advanced often costs less than you think — especially mid-subscription.",
     ["Norton upgrade discount","How to upgrade Norton plan cheaply","Norton 360 upgrade deal","Norton plan upgrade price","Best Norton upgrade offer"]),
    ("norton-student-discount","Norton Student Discount","🎓",
     "Students can save significantly on Norton 360. See all student deals, the cheapest plan for college, and how to stack discounts.",
     ["Norton student discount","Norton for students price","Cheap Norton for college","Student antivirus deal 2026","Norton education discount"]),
    ("norton-family-deal","Norton Family Deal","👨‍👩‍👧",
     "Norton 360 Deluxe covers 5 devices for $39.99/year — the best family antivirus deal in 2026. Far cheaper than buying separate plans.",
     ["Best Norton family deal","Norton 360 Deluxe family price","Cheapest family antivirus","Norton 5 device deal","Family antivirus discount 2026"]),
    ("norton-bundle-deal","Norton Bundle Deal","📦",
     "Get antivirus + VPN + dark web monitoring + password manager all in one Norton 360 plan from $29.99/year — cheaper than buying separately.",
     ["Norton bundle deals","Norton antivirus VPN bundle","Best Norton all-in-one deal","Norton 360 bundle price","Norton complete security bundle"]),
    ("norton-vs-mcafee-price","Norton vs McAfee Price","⚖️",
     "Norton 360 costs the same or less than McAfee and includes LifeLock identity protection that McAfee doesn't offer.",
     ["Norton vs McAfee price","Is Norton cheaper than McAfee?","Norton or McAfee better value","McAfee vs Norton cost 2026","Cheapest Norton or McAfee"]),
    ("norton-annual-vs-monthly","Norton Annual vs Monthly","📅",
     "Norton only offers annual plans — here's why that saves you money compared to monthly subscriptions from competing brands.",
     ["Norton annual vs monthly price","Why Norton annual only","Best antivirus monthly vs yearly","Norton yearly value","Annual antivirus savings"]),
    ("norton-lifelock-deal","Norton LifeLock Deal","🆔",
     "Norton 360 with LifeLock bundles identity theft protection with antivirus. Find the best LifeLock deal and which plan suits your needs.",
     ["Norton LifeLock price","LifeLock deal 2026","Cheapest LifeLock plan","Norton 360 Select deal","LifeLock vs standalone services"]),
    ("norton-money-back","Norton Money Back Guarantee","💯",
     "Norton's 60-day money-back guarantee is the longest in the industry. Learn exactly how it works and how to claim your refund if needed.",
     ["Norton 60 day guarantee","How to get Norton refund","Norton money back policy","Norton satisfaction guarantee","Norton cancel and refund"]),
]

DEAL_INTENTS = [
    ("guide","guide","complete deal guide"),
    ("2026","2026","best deal 2026"),
    ("how-to","how to get","how to get this deal"),
    ("best","best deal","best available deal"),
    ("comparison","comparison","deal comparison"),
    ("code","discount code","discount code"),
    ("review","review","deal review"),
    ("save","save money","how to save money"),
    ("discount","discount","biggest discount"),
    ("free","free trial","free trial"),
    ("steps","step by step","step by step guide"),
    ("tips","tips","money saving tips"),
    ("worth-it","worth it","is it worth it"),
    ("vs-competitors","vs competitors","vs competitor deals"),
    ("renewal","renewal deal","renewal discount"),
    ("new-customer","new customer","new customer offer"),
    ("upgrade","upgrade deal","upgrade savings"),
    ("bundle","bundle deal","bundle savings"),
    ("price-drop","price drop","when prices drop"),
    ("annual","annual savings","annual plan savings"),
]

# ── ANGLE 5: FAMILY SAFETY (15) ──────────────────────────────────────────────
FAMILY_TOPICS = [
    ("protect-family-online","Protect Your Family Online","🏠",
     "A complete guide to protecting your entire family online in 2026 — from young children to grandparents, every device and every threat covered.",
     ["How to protect family online","Best family internet security","Complete family online protection","Norton family protection guide","Keep family safe online"]),
    ("parental-controls","Parental Controls Guide","👨‍👩‍👧",
     "Norton Family gives parents complete control over children's online activity — websites visited, screen time, location, search history, and app usage.",
     ["Best parental control software","Norton Family review 2026","How to set up parental controls","Norton parental controls guide","Best way to monitor kids online"]),
    ("kids-online-safety","Kids Online Safety Guide","🧒",
     "Children face cyberbullying, inappropriate content, online predators, and phishing scams. A practical guide to keeping kids safe at every age.",
     ["How to keep kids safe online","Kids internet safety guide","Best app to monitor child phone","Parental control for teenagers","Child online safety tips 2026"]),
    ("identity-theft-family","Identity Theft Protection Families","🆔",
     "Children's Social Security numbers are stolen and used for years before anyone notices. Norton LifeLock monitors your whole family's identity 24/7.",
     ["Child identity theft protection","How to protect kids from identity theft","Family identity theft monitoring","Norton LifeLock family plan","Best family identity protection"]),
    ("screen-time","Screen Time Management Guide","⏱️",
     "Too much screen time harms development. Norton Family lets parents set daily limits on any device — phone, tablet, or computer — for each child.",
     ["How to limit kids screen time","Best screen time control app","Norton screen time review","Set screen time limits iPhone Android","Parental control screen time 2026"]),
    ("cyber-bullying","Cyberbullying Prevention Guide","💬",
     "Cyberbullying affects 1 in 3 children. Norton Family helps parents detect warning signs, monitor social activity, and protect kids from online bullying.",
     ["How to prevent cyberbullying","Best app to detect cyberbullying","Norton cyberbullying protection","Protect kids from online bullying","Cyberbullying monitoring software"]),
    ("home-network-security","Home Network Security Guide","📶",
     "Your home WiFi is the gateway to every device in your house. Learn how to secure your router and monitor your network for unauthorized access.",
     ["How to secure home WiFi","Best home network security","Norton home network protection","Protect home router from hackers","Home WiFi security guide 2026"]),
    ("dark-web-family","Dark Web Monitoring for Families","🌑",
     "Your family's emails, passwords, and SSNs could already be on the dark web. Norton scans thousands of dark web sites and alerts you instantly.",
     ["Family dark web monitoring","How to check dark web for my info","Best dark web monitoring service","Norton dark web family guide","Is my family data on dark web?"]),
    ("online-privacy-family","Online Privacy for Families","🔒",
     "Every website tracks your family. Norton's no-log VPN and Safe Web browser extension keeps your family's browsing private and data secure.",
     ["How to protect family privacy online","Best privacy tools for families","Norton VPN family guide","Private browsing for kids","Online privacy tips family 2026"]),
    ("phishing-scams","Protecting Family from Phishing","🎣",
     "Phishing scams target children and seniors alike. Norton Safe Web blocks phishing pages before they load and warns about suspicious links.",
     ["How to protect family from phishing","Best anti-phishing software","Norton phishing protection","Teach kids about phishing","Phishing protection family 2026"]),
    ("social-media-safety","Social Media Safety for Kids","📱",
     "Social media is where most online threats begin for children. A practical guide to safe social media use by age, with Norton Family monitoring.",
     ["Social media safety for kids","Best parental control for social media","Monitor kids social media","Norton social media monitoring","Teen social media safety guide"]),
    ("online-gaming-safety","Online Gaming Safety for Kids","🎮",
     "Online gaming exposes children to strangers, predators, and in-app scams. Norton protects young gamers without blocking the games they love.",
     ["Online gaming safety for kids","Protect kids while gaming online","Best parental control for gaming","Norton gaming protection kids","Child online gaming safety 2026"]),
    ("seniors-online-safety","Seniors Online Safety Guide","👴",
     "Seniors are the number one target for online scams. Simple, automatic Norton 360 protection against fraud, phishing, and identity theft.",
     ["Online safety for seniors","Best antivirus for elderly","Protect seniors from online scams","Norton seniors guide","Senior online fraud protection 2026"]),
    ("family-password-safety","Family Password Safety Guide","🔑",
     "Weak and reused passwords are how most families get hacked. Norton Password Manager generates and stores unique strong passwords for every account.",
     ["Family password manager guide","Best password manager families","How to manage family passwords","Norton password manager review","Family password security 2026"]),
    ("remote-work-family","Remote Work Family Security","💻",
     "With parents working from home, your network carries both personal and company data. Norton protects everyone simultaneously on the same network.",
     ["Home office security with kids","Best security work from home family","Norton remote work protection","Secure home network work and family","Work from home cybersecurity family"]),
]

FAMILY_INTENTS = [
    ("guide","guide","complete guide"),
    ("tips","tips","expert tips"),
    ("review","review","review and recommendation"),
    ("how-to","how to","step by step how to"),
    ("best","best option","best option available"),
    ("setup","setup","how to set up"),
    ("norton","with norton","using norton protection"),
    ("free","free tools","free tools available"),
    ("2026","2026 guide","complete 2026 guide"),
    ("checklist","checklist","safety checklist"),
    ("kids","for kids","for kids and teens"),
    ("seniors","for seniors","for seniors guide"),
    ("beginners","for beginners","beginners guide"),
    ("complete","complete guide","complete protection guide"),
    ("comparison","comparison","comparison of options"),
    ("download","download","how to download"),
    ("trial","free trial","free trial available"),
    ("family-plan","family plan","best family plan"),
    ("app","best app","best app available"),
    ("software","best software","best software choice"),
]

# ── LOCALE INTENTS (40) ──────────────────────────────────────────────────────
LOCALE_INTENTS = [
    ("best-antivirus","best antivirus","best antivirus"),
    ("norton-review","Norton 360 review","norton 360 review"),
    ("norton-deal","norton deal","norton discount deal"),
    ("norton-free-trial","norton free trial","norton 30 day free trial"),
    ("protect-family","protect family online","family online protection"),
    ("parental-controls","parental controls","best parental controls"),
    ("norton-price","norton price","how much does norton cost"),
    ("norton-discount","norton discount","norton coupon code"),
    ("best-antivirus-family","best antivirus family","best family antivirus"),
    ("norton-plans","norton plans","norton 360 plans comparison"),
    ("norton-download","norton download","download norton antivirus"),
    ("identity-theft","identity theft protection","best identity theft protection"),
    ("kids-online-safety","kids online safety","how to keep kids safe online"),
    ("norton-vpn","norton vpn","norton vpn review"),
    ("screen-time","screen time control","limit kids screen time"),
    ("dark-web","dark web monitoring","dark web monitoring family"),
    ("best-antivirus-windows","best antivirus windows","best antivirus for windows"),
    ("best-antivirus-mac","best antivirus mac","best antivirus for mac"),
    ("best-antivirus-iphone","best antivirus iphone","best antivirus for iphone"),
    ("best-antivirus-android","best antivirus android","best antivirus for android"),
    ("norton-lifelock","norton lifelock","norton lifelock review"),
    ("online-privacy","online privacy","protect privacy online"),
    ("phishing-protection","phishing protection","protect against phishing"),
    ("home-network","home network security","secure home network"),
    ("norton-gaming","norton gaming","norton for gaming pc"),
    ("norton-students","norton students","norton for students"),
    ("norton-seniors","norton seniors","norton for seniors"),
    ("norton-black-friday","norton black friday","norton black friday deal"),
    ("norton-promo","norton promo code","norton promo code 2026"),
    ("norton-refund","norton refund","norton 60 day money back"),
    ("norton-vs-mcafee","norton vs mcafee","norton versus mcafee"),
    ("norton-vs-bitdefender","norton vs bitdefender","norton versus bitdefender"),
    ("best-antivirus-budget","budget antivirus","cheapest best antivirus"),
    ("norton-award","norton award winning","norton award winning antivirus"),
    ("best-antivirus-2026","best antivirus 2026","number one antivirus 2026"),
    ("norton-worth-it","is norton worth it","norton worth the money"),
    ("norton-comparison","antivirus comparison","best antivirus comparison"),
    ("norton-bundle","norton bundle","norton security bundle"),
    ("norton-cancel","cancel norton","how to cancel norton"),
    ("norton-support","norton support","norton customer support"),
]

# ── STATE INTENTS (35) ───────────────────────────────────────────────────────
STATE_INTENTS = [
    ("best-antivirus","best antivirus","best antivirus"),
    ("norton-deal","norton deal","norton discount"),
    ("protect-family","protect family","family online protection"),
    ("parental-controls","parental controls","parental control software"),
    ("norton-review","norton review","norton 360 review"),
    ("norton-free-trial","norton free trial","norton free trial"),
    ("norton-price","norton price","how much norton costs"),
    ("kids-online-safety","kids online safety","keep kids safe online"),
    ("identity-theft","identity theft","identity theft protection"),
    ("norton-vpn","norton vpn","norton vpn"),
    ("screen-time","screen time","screen time control"),
    ("dark-web","dark web","dark web monitoring"),
    ("norton-lifelock","norton lifelock","norton lifelock"),
    ("online-privacy","online privacy","online privacy protection"),
    ("home-network","home network","home network security"),
    ("best-antivirus-windows","best windows antivirus","best antivirus windows"),
    ("best-antivirus-mac","best mac antivirus","best antivirus mac"),
    ("norton-gaming","norton gaming","norton gaming pc"),
    ("norton-seniors","norton seniors","norton for seniors"),
    ("norton-students","norton students","norton for students"),
    ("norton-black-friday","norton black friday","norton black friday"),
    ("norton-promo","norton promo","norton promo code"),
    ("phishing-protection","phishing protection","stop phishing attacks"),
    ("norton-family-plan","norton family plan","norton family plan"),
    ("best-antivirus-2026","best antivirus 2026","best antivirus 2026"),
    ("norton-worth-it","norton worth it","is norton worth it"),
    ("norton-vs-mcafee","norton vs mcafee","norton versus mcafee"),
    ("norton-plans","norton plans","norton 360 plans"),
    ("norton-bundle","norton bundle","norton security bundle"),
    ("norton-refund","norton refund","norton money back"),
    ("cyberbullying","cyberbullying protection","protect kids cyberbullying"),
    ("social-media-safety","social media safety","kids social media safety"),
    ("norton-award","award winning antivirus","best rated antivirus"),
    ("norton-download","norton download","download norton"),
    ("norton-discount","norton discount","norton coupon"),
]

# ── LONG TAILS (500) ─────────────────────────────────────────────────────────
LONG_TAILS = [
    ("best-antivirus-2026-review","Best Antivirus 2026 Complete Review","best antivirus software 2026 complete review"),
    ("top-10-antivirus-2026","Top 10 Antivirus 2026","top 10 best antivirus software 2026"),
    ("antivirus-comparison-2026","Antivirus Comparison 2026","compare best antivirus software 2026"),
    ("antivirus-buying-guide-2026","Antivirus Buying Guide 2026","how to choose antivirus 2026"),
    ("norton-number-one","Norton #1 Antivirus","why norton is the number one antivirus"),
    ("best-paid-antivirus","Best Paid Antivirus","best paid antivirus vs free 2026"),
    ("free-vs-paid-antivirus","Free vs Paid Antivirus","is paid antivirus worth it over free"),
    ("antivirus-test-results-2026","Antivirus Test Results 2026","independent antivirus test results 2026"),
    ("av-test-results-2026","AV-TEST Results 2026","av-test antivirus results 2026"),
    ("best-antivirus-detection","Best Antivirus Detection Rate","antivirus with highest detection rate"),
    ("best-antivirus-no-slowdown","Best Antivirus No Slowdown","antivirus that doesnt slow computer"),
    ("best-lightweight-antivirus","Best Lightweight Antivirus","lightest antivirus for slow computers"),
    ("norton-av-test-certified","Norton AV-TEST Certified","norton av-test certification 2026"),
    ("norton-detection-rate","Norton Detection Rate","norton malware detection rate 2026"),
    ("best-antivirus-zero-day","Best Zero-Day Protection","best antivirus for zero day threats"),
    ("best-antivirus-spyware","Best Antivirus Spyware","best antivirus to remove spyware"),
    ("norton-discount-2026","Norton Discount 2026","norton antivirus discount 2026"),
    ("norton-coupon-2026","Norton Coupon 2026","norton coupon code 2026"),
    ("norton-70-off","Norton 70 Percent Off","norton antivirus 70 percent off"),
    ("norton-sale-2026","Norton Sale 2026","norton antivirus sale 2026"),
    ("norton-cheapest-price","Norton Cheapest Price","cheapest price for norton antivirus"),
    ("norton-first-year-deal","Norton First Year Deal","norton antivirus first year discount"),
    ("norton-renewal-cheaper","Norton Renewal Cheaper","how to get norton renewal cheaper"),
    ("norton-cyber-monday","Norton Cyber Monday","norton cyber monday deal 2026"),
    ("norton-vs-mcafee-price","Norton vs McAfee Price","norton cheaper than mcafee"),
    ("norton-vs-bitdefender-price","Norton vs Bitdefender Price","norton vs bitdefender price"),
    ("norton-plan-upgrade","Norton Plan Upgrade","how to upgrade norton plan cheaply"),
    ("norton-360-deluxe-deal","Norton 360 Deluxe Deal","norton 360 deluxe cheapest price"),
    ("norton-360-advanced-deal","Norton 360 Advanced Deal","norton 360 advanced discount"),
    ("norton-ultimate-deal","Norton 360 Ultimate Deal","norton 360 ultimate plus price"),
    ("family-internet-safety-guide","Family Internet Safety Guide","complete family internet safety guide 2026"),
    ("how-to-protect-children-online","How to Protect Children Online","how to protect your children online"),
    ("internet-safety-kids-age","Internet Safety by Age","internet safety guide for kids by age"),
    ("parental-control-guide-2026","Parental Control Guide 2026","best parental control guide 2026"),
    ("norton-family-review-2026","Norton Family Review 2026","norton family parental control review 2026"),
    ("norton-family-setup","How to Set Up Norton Family","how to set up norton family parental controls"),
    ("norton-family-vs-bark","Norton Family vs Bark","norton family versus bark comparison"),
    ("norton-family-vs-qustodio","Norton Family vs Qustodio","norton family versus qustodio"),
    ("screen-time-guide","Screen Time Limit Guide","how to set screen time limits all devices"),
    ("kids-phone-monitoring","Kids Phone Monitoring","how to monitor kids phone activity"),
    ("teen-online-safety","Teen Online Safety Guide","teen internet safety guide 2026"),
    ("child-online-privacy","Child Online Privacy","protect your childs online privacy"),
    ("kids-social-media-age","Kids Social Media Age","what age should kids use social media"),
    ("tiktok-safety-parents","TikTok Safety for Parents","tiktok safety parental controls guide"),
    ("youtube-kids-safety","YouTube Kids Safety","is youtube kids safe parental guide"),
    ("roblox-safety-guide","Roblox Safety Guide","roblox safety guide for parents"),
    ("minecraft-safety-guide","Minecraft Safety for Kids","minecraft online safety guide parents"),
    ("fortnite-safety-parents","Fortnite Safety for Parents","fortnite online safety parental guide"),
    ("child-identity-theft","Child Identity Theft","how common is child identity theft"),
    ("child-ssn-protection","Protect Child SSN","how to protect your childs social security number"),
    ("family-identity-protection","Family Identity Protection","best family identity theft protection"),
    ("norton-lifelock-family","Norton LifeLock Family","norton lifelock family plan review"),
    ("identity-theft-recovery","Identity Theft Recovery","how to recover from identity theft"),
    ("data-breach-family","Data Breach Family Protection","protect family from data breach"),
    ("senior-scam-protection","Senior Scam Protection","protect elderly parents from scams"),
    ("grandparent-scam","Grandparent Scam Protection","grandparent phone scam how to protect"),
    ("home-network-security-guide","Home Network Security Guide","complete home network security guide 2026"),
    ("secure-home-wifi","Secure Home WiFi Guide","how to secure your home wifi network"),
    ("router-security-guide","Router Security Guide","how to secure your router 2026"),
    ("smart-home-security","Smart Home Security","security for smart home devices 2026"),
    ("iot-device-security","IoT Device Security","how to secure iot devices home"),
    ("home-vpn-guide","Home VPN Guide","should you use vpn at home"),
    ("norton-360-review-2026","Norton 360 Review 2026","norton 360 complete review 2026"),
    ("norton-360-deluxe-review","Norton 360 Deluxe Review","norton 360 deluxe review 2026"),
    ("norton-360-family-review","Norton 360 Family Review","norton 360 deluxe family review"),
    ("norton-vpn-review-2026","Norton VPN Review 2026","norton vpn complete review 2026"),
    ("norton-dark-web-review","Norton Dark Web Review","norton dark web monitoring review 2026"),
    ("norton-lifelock-review","Norton LifeLock Review","norton lifelock complete review 2026"),
    ("norton-password-manager","Norton Password Manager","norton password manager review 2026"),
    ("norton-cloud-backup","Norton Cloud Backup","norton cloud backup review 2026"),
    ("norton-firewall-review","Norton Firewall Review","norton smart firewall review 2026"),
    ("best-antivirus-norton-mcafee","Norton vs McAfee Best","norton versus mcafee which is best"),
    ("best-antivirus-norton-bitdefender","Norton vs Bitdefender Best","norton versus bitdefender which is best"),
    ("best-antivirus-norton-kaspersky","Norton vs Kaspersky Best","norton versus kaspersky which is best"),
    ("best-antivirus-norton-avast","Norton vs Avast Best","norton versus avast which is best"),
    ("best-antivirus-norton-avg","Norton vs AVG Best","norton versus avg which is best"),
    ("best-antivirus-norton-malwarebytes","Norton vs Malwarebytes","norton versus malwarebytes best choice"),
    ("best-antivirus-norton-totalav","Norton vs TotalAV Best","norton versus totalav which is best"),
    ("best-antivirus-norton-eset","Norton vs ESET Best","norton versus eset which is best"),
    ("best-antivirus-norton-defender","Norton vs Windows Defender","norton versus windows defender better"),
    ("protect-teens-online","Protect Teenagers Online","how to protect teenagers from online dangers"),
    ("online-predator-protection","Online Predator Protection","protect children from online predators"),
    ("cybersecurity-for-parents","Cybersecurity for Parents","cybersecurity guide for non-technical parents"),
    ("back-to-school-security","Back to School Security","back to school cybersecurity guide 2026"),
    ("first-phone-safety","First Phone Safety Guide","safety guide for childs first phone"),
    ("laptop-safety-kids","Laptop Safety for Kids","how to set up safe laptop for kids"),
    ("school-cyberbullying","School Cyberbullying Guide","how to deal with school cyberbullying"),
    ("teen-gaming-safety","Teen Gaming Safety Guide","online gaming safety guide for teenagers"),
    ("norton-gift","Norton as a Gift","norton 360 gift subscription"),
    ("norton-military-discount","Norton Military Discount","norton discount for military"),
    ("norton-senior-discount","Norton Senior Discount","norton discount for seniors 2026"),
    ("norton-first-month-free","Norton First Month Free","norton first month free offer"),
    ("best-antivirus-deal-2026","Best Antivirus Deal 2026","best antivirus software deal 2026"),
    ("antivirus-subscription-tips","Antivirus Subscription Tips","how to save on antivirus subscription"),
    ("ai-threats-2026","AI Cyber Threats 2026","new ai-powered cyber threats 2026"),
    ("deepfake-scams","Deepfake Scams Protection","protect family from deepfake scams"),
    ("qr-code-scams","QR Code Scams","protect family from qr code phishing"),
    ("sms-phishing","SMS Phishing Protection","protect from sms phishing smishing"),
    ("email-scam-protection","Email Scam Protection","best email scam protection 2026"),
    ("password-breach","Password Breach Protection","what to do after password breach"),
    ("vpn-home-guide","VPN for Home Use","why you need vpn at home 2026"),
    ("ransomware-family","Ransomware Protection Family","protect family from ransomware 2026"),
    ("best-antivirus-under-30","Best Antivirus Under 30 Dollars","best antivirus software under 30 dollars"),
    ("best-antivirus-under-50","Best Antivirus Under 50 Dollars","best antivirus software under 50 dollars"),
    ("best-antivirus-value","Best Value Antivirus 2026","best value for money antivirus 2026"),
    ("do-i-need-antivirus-2026","Do I Need Antivirus 2026","do i still need antivirus in 2026"),
    ("windows-defender-enough","Is Windows Defender Enough","is windows defender enough protection 2026"),
    ("mac-needs-antivirus","Does Mac Need Antivirus","does apple mac need antivirus 2026"),
    ("iphone-needs-antivirus","Does iPhone Need Antivirus","does iphone need antivirus app"),
    ("android-antivirus-needed","Android Antivirus Needed","does android phone need antivirus"),
    ("best-security-suite-2026","Best Security Suite 2026","best internet security suite 2026"),
    ("norton-2026-features","Norton 2026 New Features","norton antivirus 2026 new features"),
    ("cybersecurity-trends-2026","Cybersecurity Trends 2026","top cybersecurity threats 2026"),
    ("most-common-threats-2026","Most Common Cyber Threats 2026","most common cyber threats 2026"),
    ("antivirus-vs-internet-security","Antivirus vs Internet Security","antivirus versus internet security suite"),
    ("real-time-protection-explained","What is Real-Time Protection","what does real-time antivirus protection do"),
]

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = """:root{--navy:#1a1f3a;--navy-dark:#0d1029;--navy-mid:#1e2550;--yellow:#ffcc00;--yellow-dark:#e6b800;--yellow-light:#fffbe6;--green:#00b341;--red:#e53935;--orange:#ff6b00;--white:#fff;--bg:#f4f6ff;--card:#fff;--text:#1a1f3a;--muted:#5a6080;--border:#e0e4f0;--font:'Plus Jakarta Sans',sans-serif;--r:14px;--sh:0 4px 24px rgba(26,31,58,0.08);}
*{box-sizing:border-box;margin:0;padding:0}body{background:var(--bg);color:var(--text);font-family:var(--font);line-height:1.65}a{text-decoration:none;color:inherit}
.nav{background:var(--navy-dark);position:sticky;top:0;z-index:200;box-shadow:0 2px 16px rgba(0,0,0,0.3)}.nav-i{max-width:1200px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding:0 24px;height:64px}.logo{font-weight:800;font-size:19px;color:var(--white);display:flex;align-items:center;gap:10px}.logo-badge{background:var(--yellow);color:var(--navy);width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:900}.logo span{color:var(--yellow)}.nav-links{display:flex;gap:24px;align-items:center}.nav-links a{color:rgba(255,255,255,0.75);font-size:13px;font-weight:600;transition:color .2s}.nav-links a:hover{color:var(--yellow)}.nav-cta{background:var(--yellow);color:var(--navy)!important;font-weight:800!important;font-size:13px;padding:10px 20px;border-radius:8px;transition:background .2s;white-space:nowrap}.nav-cta:hover{background:var(--yellow-dark)}
.promo{background:var(--yellow);color:var(--navy);text-align:center;padding:9px 24px;font-size:13px;font-weight:700}
.hero{background:linear-gradient(135deg,var(--navy-dark) 0%,var(--navy) 55%,var(--navy-mid) 100%);color:var(--white);padding:76px 24px 60px;text-align:center;position:relative;overflow:hidden}.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(255,204,0,0.1) 0%,transparent 70%);pointer-events:none}.badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,204,0,0.15);border:1px solid rgba(255,204,0,0.3);color:var(--yellow);padding:6px 16px;border-radius:999px;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:22px}.hero h1{font-size:clamp(26px,5vw,54px);font-weight:800;line-height:1.1;margin-bottom:16px}.hero h1 em{color:var(--yellow);font-style:normal}.hero p{font-size:17px;opacity:.85;max-width:580px;margin:0 auto 28px}.btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-bottom:44px}
.btn-y{background:var(--yellow);color:var(--navy);font-weight:800;font-size:15px;padding:15px 34px;border-radius:10px;box-shadow:0 6px 28px rgba(255,204,0,0.35);transition:transform .2s,box-shadow .2s,background .2s;display:inline-block}.btn-y:hover{background:var(--yellow-dark);transform:translateY(-2px);box-shadow:0 10px 32px rgba(255,204,0,0.45);color:var(--navy)}.btn-ghost{border:2px solid rgba(255,255,255,0.3);color:var(--white);font-size:14px;padding:13px 26px;border-radius:10px;transition:border-color .2s;display:inline-block}.btn-ghost:hover{border-color:var(--white)}
.stats{display:flex;justify-content:center;gap:44px;flex-wrap:wrap;padding:28px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.08);border-radius:var(--r);max-width:680px;margin:0 auto}.stat-n{font-size:26px;font-weight:800;color:var(--yellow)}.stat-l{font-size:11px;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:.08em;margin-top:3px}
.trust{background:var(--navy);display:flex;justify-content:center;gap:36px;flex-wrap:wrap;padding:16px 24px;border-bottom:1px solid rgba(255,255,255,0.08)}.trust-i{display:flex;align-items:center;gap:7px;font-size:13px;font-weight:600;color:rgba(255,255,255,0.85)}
.section{padding:60px 24px}.section-alt{background:var(--white)}.container{max-width:1200px;margin:0 auto}.stag{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--yellow);display:flex;align-items:center;gap:6px;margin-bottom:8px}.stag::before{content:'';width:22px;height:2px;background:var(--yellow);border-radius:2px}.stitle{font-size:clamp(22px,3.5vw,34px);font-weight:800;color:var(--navy);margin-bottom:10px;line-height:1.2}.ssub{color:var(--muted);font-size:16px;margin-bottom:36px;max-width:540px}.center{text-align:center}.center .ssub{margin:0 auto 36px}
.rank-list{display:grid;gap:16px}.rank-item{background:var(--card);border:2px solid var(--border);border-radius:var(--r);padding:22px 24px;display:flex;align-items:center;gap:20px;box-shadow:var(--sh);transition:border-color .2s,transform .2s}.rank-item:hover{border-color:var(--yellow);transform:translateX(4px)}.rank-item.rank-1{border-color:var(--yellow);background:var(--yellow-light)}.rank-num{font-size:28px;font-weight:800;color:var(--navy);min-width:40px}.rank-1 .rank-num{color:var(--yellow-dark)}.rank-icon{font-size:28px;min-width:40px;text-align:center}.rank-info{flex:1}.rank-name{font-size:17px;font-weight:800;color:var(--navy);margin-bottom:4px}.rank-desc{font-size:13px;color:var(--muted)}.rank-score{text-align:right}.rank-score-num{font-size:22px;font-weight:800;color:var(--navy)}.rank-score-label{font-size:11px;color:var(--muted)}.rank-badge{background:var(--yellow);color:var(--navy);font-size:10px;font-weight:800;padding:3px 10px;border-radius:999px;margin-left:8px}.rank-cta{display:inline-block;background:var(--yellow);color:var(--navy);font-weight:800;font-size:13px;padding:10px 20px;border-radius:8px;margin-top:10px;transition:background .2s}.rank-cta:hover{background:var(--yellow-dark);color:var(--navy)}
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:18px;margin-bottom:28px}.card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:26px;box-shadow:var(--sh);transition:transform .2s,box-shadow .2s,border-color .2s;display:block}.card:hover{transform:translateY(-5px);box-shadow:0 14px 36px rgba(26,31,58,0.13);border-color:var(--yellow)}.card-icon{font-size:30px;margin-bottom:12px}.card h3{font-size:15px;font-weight:700;color:var(--navy);margin-bottom:7px}.card p{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:12px}.card-link{font-size:13px;font-weight:700;color:var(--yellow)}
.deal-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}.deal-card{background:var(--card);border:2px solid var(--border);border-radius:var(--r);padding:24px;box-shadow:var(--sh);position:relative;transition:border-color .2s,transform .2s}.deal-card:hover{border-color:var(--yellow);transform:translateY(-4px)}.deal-card.hot{border-color:var(--orange)}.deal-badge{position:absolute;top:-10px;right:16px;background:var(--orange);color:var(--white);font-size:10px;font-weight:800;padding:3px 12px;border-radius:999px}.deal-icon{font-size:28px;margin-bottom:10px}.deal-title{font-size:16px;font-weight:800;color:var(--navy);margin-bottom:6px}.deal-desc{font-size:13px;color:var(--muted);line-height:1.6;margin-bottom:14px}.deal-cta{display:block;background:var(--yellow);color:var(--navy);font-weight:800;font-size:13px;padding:12px;border-radius:8px;text-align:center;transition:background .2s}.deal-cta:hover{background:var(--yellow-dark);color:var(--navy)}
.cmp-wrap{overflow-x:auto;border-radius:var(--r);box-shadow:var(--sh)}.cmp-table{width:100%;border-collapse:collapse}.cmp-table th,.cmp-table td{padding:13px 16px;text-align:left;border-bottom:1px solid var(--border);font-size:13px}.cmp-table th{background:var(--navy);color:var(--white);font-weight:700}.cmp-table tr:hover td{background:#f9faff}.cmp-table tr:last-child td{border-bottom:none}.yes{color:var(--green);font-weight:700}.no{color:var(--red)}.part{color:#f59e0b;font-weight:600}.norton-col{background:var(--yellow-light)!important}.winner{background:var(--yellow);color:var(--navy);font-size:10px;font-weight:800;padding:2px 8px;border-radius:999px;margin-left:5px;vertical-align:middle}
.faq-list{display:grid;gap:12px}.faq-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px}.faq-q{font-weight:700;color:var(--navy);font-size:15px;margin-bottom:7px}.faq-a{font-size:13px;color:var(--muted);line-height:1.65}
.plan-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px}.plan-card{background:var(--card);border:2px solid var(--border);border-radius:var(--r);padding:24px;text-align:center;position:relative;transition:border-color .2s,transform .2s}.plan-card:hover{border-color:var(--yellow);transform:translateY(-4px)}.plan-card.pop{border-color:var(--yellow);box-shadow:0 8px 32px rgba(255,204,0,0.2)}.pop-badge{position:absolute;top:-11px;left:50%;transform:translateX(-50%);background:var(--yellow);color:var(--navy);font-size:11px;font-weight:800;padding:3px 14px;border-radius:999px;white-space:nowrap}.plan-name{font-size:13px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}.plan-price{font-size:32px;font-weight:800;color:var(--navy);margin-bottom:3px}.plan-yr{font-size:12px;color:var(--muted);margin-bottom:12px}.plan-dev{font-size:13px;color:var(--navy);font-weight:600;margin-bottom:16px}.plan-cta{display:block;background:var(--yellow);color:var(--navy);font-weight:800;font-size:13px;padding:12px;border-radius:8px;transition:background .2s;width:100%}.plan-cta:hover{background:var(--yellow-dark);color:var(--navy)}
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px}.rel-link{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:11px 14px;font-size:13px;font-weight:600;color:var(--text);transition:border-color .2s,box-shadow .2s;display:block}.rel-link:hover{border-color:var(--yellow);box-shadow:0 4px 12px rgba(255,204,0,0.12)}
.cta-band{background:linear-gradient(135deg,var(--navy-dark),var(--navy));color:var(--white);padding:60px 24px;text-align:center;position:relative;overflow:hidden}.cta-band::before{content:'🛡️';font-size:180px;opacity:.04;position:absolute;right:-10px;top:50%;transform:translateY(-50%)}.cta-band h2{font-size:clamp(22px,4vw,38px);font-weight:800;margin-bottom:10px}.cta-band p{opacity:.8;margin-bottom:26px;font-size:16px;max-width:540px;margin-left:auto;margin-right:auto}
.sticky-cta{position:fixed;bottom:20px;right:20px;background:var(--yellow);color:var(--navy);font-weight:800;font-size:13px;padding:13px 20px;border-radius:10px;box-shadow:0 6px 24px rgba(255,204,0,0.4);z-index:999;transition:background .2s,transform .2s}.sticky-cta:hover{background:var(--yellow-dark);transform:scale(1.04);color:var(--navy)}
footer{background:var(--navy-dark);color:rgba(255,255,255,0.55);padding:44px 24px 24px}.footer-i{max-width:1200px;margin:0 auto}.footer-top{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:36px;margin-bottom:36px}.footer-logo{font-weight:800;font-size:17px;color:var(--white);margin-bottom:10px}.footer-logo span{color:var(--yellow)}.footer-desc{font-size:12px;line-height:1.7}.footer-col h4{color:var(--white);font-size:12px;font-weight:700;margin-bottom:12px;letter-spacing:.06em;text-transform:uppercase}.footer-col a{display:block;color:rgba(255,255,255,0.5);font-size:12px;margin-bottom:7px;transition:color .2s}.footer-col a:hover{color:var(--yellow)}.footer-bot{border-top:1px solid rgba(255,255,255,0.08);padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:11px}.footer-disc{font-size:10px;color:rgba(255,255,255,0.3);margin-top:7px}
@media(max-width:768px){.nav-links{display:none}.hero{padding:50px 14px 40px}.stats{gap:20px;padding:20px}.trust{gap:16px}.footer-top{grid-template-columns:1fr}.footer-bot{flex-direction:column}}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'
JS = """window.addEventListener('scroll',()=>{const s=document.querySelector('.sticky-cta');if(s)s.style.opacity=window.scrollY>300?'1':'0';});
const obs=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.style.opacity='1';e.target.style.transform='none';}}),{threshold:0.1});
document.querySelectorAll('.fade').forEach(el=>{el.style.cssText='opacity:0;transform:translateY(20px);transition:opacity .5s ease,transform .5s ease';obs.observe(el);});"""

def tr(lang, key): return T.get(lang, T["en"]).get(key, T["en"].get(key,""))

def nav_html(lang="en"):
    return f"""<div class="promo">{tr(lang,"promo")}</div>
<nav class="nav"><div class="nav-i">
  <div class="logo"><div class="logo-badge">N</div>Best<span>Antivirus</span>Guide</div>
  <div class="nav-links">
    <a href="index.html">Home</a>
    <a href="best-antivirus-2026-review.html">Best Antivirus</a>
    <a href="norton-deal-guide.html">Deals</a>
    <a href="protect-family-online-guide.html">Family Safety</a>
    <a href="parental-controls-guide.html">Parental Controls</a>
    <a href="{AFF}" class="nav-cta" target="_blank" rel="nofollow sponsored">{tr(lang,"cta_short")}</a>
  </div>
</div></nav>"""

def trust_bar(lang="en"):
    return f"""<div class="trust">
  <div class="trust-i">{tr(lang,"trust1")}</div>
  <div class="trust-i">{tr(lang,"trust2")}</div>
  <div class="trust-i">{tr(lang,"trust3")}</div>
  <div class="trust-i">{tr(lang,"trust4")}</div>
</div>"""

def footer_html(lang="en"):
    return f"""<footer><div class="footer-i">
  <div class="footer-top">
    <div><div class="footer-logo">Best<span>Antivirus</span>Guide</div>
      <p class="footer-desc">Independent antivirus reviews, Norton deals, and family safety guides for {YEAR}.</p>
      <p class="footer-disc" style="margin-top:10px">{tr(lang,"disc")}</p></div>
    <div class="footer-col"><h4>Best Antivirus</h4>
      <a href="best-antivirus-2026-review.html">Best of {YEAR}</a>
      <a href="best-antivirus-windows-review.html">For Windows</a>
      <a href="best-antivirus-mac-review.html">For Mac</a>
      <a href="best-antivirus-family-review.html">For Families</a>
      <a href="best-antivirus-gaming-review.html">For Gaming</a>
      <a href="best-free-antivirus-review.html">Free Options</a></div>
    <div class="footer-col"><h4>Norton Deals</h4>
      <a href="norton-deal-guide.html">Best Deals</a>
      <a href="norton-promo-code-guide.html">Promo Codes</a>
      <a href="norton-free-trial-guide.html">Free Trial</a>
      <a href="norton-plans-price-guide.html">Plan Prices</a>
      <a href="norton-black-friday-guide.html">Black Friday</a>
      <a href="norton-cheapest-plan-guide.html">Cheapest Plan</a></div>
    <div class="footer-col"><h4>Family Safety</h4>
      <a href="protect-family-online-guide.html">Family Guide</a>
      <a href="parental-controls-guide.html">Parental Controls</a>
      <a href="kids-online-safety-guide.html">Kids Safety</a>
      <a href="screen-time-guide.html">Screen Time</a>
      <a href="identity-theft-family-guide.html">Identity Theft</a>
      <a href="home-network-security-guide.html">Home Network</a></div>
  </div>
  <div class="footer-bot">
    <span>© {YEAR} BestAntivirusGuide · Independent Review Site</span>
    <span>Norton® is a trademark of Gen Digital Inc. Not affiliated with Norton.</span>
  </div>
</div></footer>"""

def sticky(lang="en"):
    return f'<a href="{AFF}" class="sticky-cta" target="_blank" rel="nofollow sponsored" style="opacity:0">{tr(lang,"sticky")}</a>'

def cta_band(h2, p, lang="en"):
    return f"""<div class="cta-band"><div class="container">
  <h2>{h2}</h2><p>{p}</p>
  <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored"
     style="display:inline-block;font-size:16px;padding:16px 40px">{tr(lang,"cta")}</a>
  <div style="margin-top:14px;font-size:13px;opacity:.6">✓ 30-Day Free Trial &nbsp;·&nbsp; ✓ 60-Day Money-Back &nbsp;·&nbsp; ✓ No Credit Card Required</div>
</div></div>"""

def make_faqs(items, lang="en"):
    tl = tr(lang,"faq")
    html = "".join(f'<div class="faq-item fade"><div class="faq-q">❓ {q}</div><div class="faq-a">{a}</div></div>' for q,a in items)
    sc = ",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}' for q,a in items)
    schema = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{sc}]}}</script>'
    return f'<div class="section"><div class="container"><div class="stag">{tl}</div><h2 class="stitle">{tl}</h2><div class="faq-list">{html}</div></div></div>', schema

def rel_section(links, lang="en"):
    tl = tr(lang,"related")
    items = "".join(f'<a href="{u}" class="rel-link">🛡️ {l}</a>' for l,u in links[:16])
    return f'<div class="section section-alt"><div class="container"><div class="stag">{tl}</div><div class="rel-grid">{items}</div></div></div>'

def make_page(slug, title, desc, body, lang="en", schema=""):
    canonical = f"{BASE_URL}/{slug}"
    ldir = "rtl" if lang == "ar" else "ltr"
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{ldir}">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
{FONTS}{schema}
<style>{CSS}</style>
</head>
<body>
{nav_html(lang)}
{body}
{footer_html(lang)}
{sticky(lang)}
<script>{JS}</script>
</body>
</html>"""

# ── PAGE BUILDERS ─────────────────────────────────────────────────────────────

def make_category_page(lc, lang, country, currency, price, c_slug, c_name, c_icon, c_desc, c_faqs, i_slug, i_name):
    slug  = f"{lc}-{c_slug}-{i_slug}.html"
    title = f"{c_name} — {i_name} {country} {YEAR} | BestAntivirusGuide"
    desc  = f"{c_name} {i_name} for {country}. {c_desc[:100]}... Expert rankings and top picks {YEAR}."
    body  = f"""
<section class="hero">
  <div class="badge">🏆 Expert Ranked · {country} · {YEAR}</div>
  <h1>{c_icon} <em>{c_name}</em><br>{i_name}</h1>
  <p>{c_desc}</p>
  <div class="btns">
    <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr(lang,"cta")}</a>
    <a href="index.html" class="btn-ghost">← All Reviews</a>
  </div>
  <div class="stats">
    <div><div class="stat-n">#1</div><div class="stat-l">Norton 360</div></div>
    <div><div class="stat-n">9.7</div><div class="stat-l">Expert Score</div></div>
    <div><div class="stat-n">99.9%</div><div class="stat-l">Detection Rate</div></div>
    <div><div class="stat-n">30</div><div class="stat-l">Day Free Trial</div></div>
  </div>
</section>
{trust_bar(lang)}
<div class="section section-alt"><div class="container">
  <div class="stag">{c_icon} Rankings</div>
  <h2 class="stitle">{c_name}: {i_name} for {country}</h2>
  <div class="rank-list fade">
    <div class="rank-item rank-1">
      <div class="rank-num">01</div><div class="rank-icon">🛡️</div>
      <div class="rank-info">
        <div class="rank-name">Norton 360 <span class="rank-badge">BEST {YEAR}</span></div>
        <div class="rank-desc">99.9% detection · Unlimited VPN · Dark web monitoring · LifeLock identity protection · 50M+ users protected worldwide</div>
        <a href="{AFF}" class="rank-cta" target="_blank" rel="nofollow sponsored">{tr(lang,"cta")} →</a>
      </div>
      <div class="rank-score"><div class="rank-score-num">9.7</div><div class="rank-score-label">/ 10</div></div>
    </div>
    <div class="rank-item"><div class="rank-num">02</div><div class="rank-icon">🔵</div><div class="rank-info"><div class="rank-name">Bitdefender</div><div class="rank-desc">Strong detection but fewer features — no LifeLock, no cloud backup, VPN limited on base plans</div></div><div class="rank-score"><div class="rank-score-num">9.2</div><div class="rank-score-label">/ 10</div></div></div>
    <div class="rank-item"><div class="rank-num">03</div><div class="rank-icon">🔴</div><div class="rank-info"><div class="rank-name">McAfee</div><div class="rank-desc">Good for large families but slower performance and no identity theft coverage</div></div><div class="rank-score"><div class="rank-score-num">8.8</div><div class="rank-score-label">/ 10</div></div></div>
    <div class="rank-item"><div class="rank-num">04</div><div class="rank-icon">⚪</div><div class="rank-info"><div class="rank-name">Kaspersky</div><div class="rank-desc">High detection but privacy concerns — we recommend Norton for US, UK, and EU users</div></div><div class="rank-score"><div class="rank-score-num">8.5</div><div class="rank-score-label">/ 10</div></div></div>
    <div class="rank-item"><div class="rank-num">05</div><div class="rank-icon">🟢</div><div class="rank-info"><div class="rank-name">Avast Free</div><div class="rank-desc">Popular free option but sells user data — Norton's 30-day trial is safer and more feature-rich</div></div><div class="rank-score"><div class="rank-score-num">7.5</div><div class="rank-score-label">/ 10</div></div></div>
  </div>
</div></div>
{cta_band(f"Get the #1 Rated {c_name} — Norton 360", f"Try free for 30 days in {country}. 60-day money-back guarantee.", lang)}
<div class="section"><div class="container">
  <div class="stag">Why Norton Wins</div>
  <h2 class="stitle">Why Norton Is #1 for {c_name}</h2>
  <div class="card-grid fade">
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🛡️</div><h3>99.9% Detection Rate</h3><p>Verified by AV-TEST and AV-Comparatives — the gold standard for antivirus accuracy. No other product comes close.</p><span class="card-link">Learn More →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🔐</div><h3>Unlimited VPN Included</h3><p>No-log VPN with 2,000+ servers in 30+ countries. No data caps. Included free with every Norton 360 plan.</p><span class="card-link">Learn More →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🆔</div><h3>LifeLock Identity Protection</h3><p>The only antivirus with built-in identity theft protection and up to $1M coverage for eligible losses.</p><span class="card-link">Learn More →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">💰</div><h3>From {currency} {price}/mo</h3><p>30-day free trial + 60-day money-back guarantee. Best value {c_name.lower()} in {country}.</p><span class="card-link">See All Plans →</span></a>
  </div>
</div></div>"""
    faq_items = [(q, f"Norton 360 is our top recommendation for {country} users in {YEAR}. It consistently tops independent lab tests and offers the most features at the best price. Start a 30-day free trial risk-free.") for q in c_faqs]
    faq_sec, faq_schema = make_faqs(faq_items, lang)
    rel = [(f"{c_name} Guide", f"{lc}-{c_slug}-guide.html"),
           (f"Norton Deal {country}", f"{lc}-norton-deal-guide.html"),
           (f"Norton Free Trial", f"{lc}-norton-free-trial-guide.html"),
           (f"Protect Family {country}", f"{lc}-protect-family-online-guide.html")]
    full = body + faq_sec + rel_section(rel, lang) + cta_band(f"Try the #1 Antivirus Free", "30-day trial. No credit card required.", lang)
    return slug, make_page(slug, title, desc, full, lang, faq_schema)

def make_deal_page(lc, lang, country, currency, price, d_slug, d_name, d_icon, d_desc, d_faqs, i_slug, i_name):
    slug  = f"{lc}-{d_slug}-{i_slug}.html"
    title = f"{d_name} — {i_name} {country} {YEAR} | BestAntivirusGuide"
    desc  = f"{d_name} {i_name} for {country}. {d_desc[:100]}... Save on Norton 360 today."
    body  = f"""
<section class="hero">
  <div class="badge">💸 Best Deals · {country} · {YEAR}</div>
  <h1>{d_icon} <em>{d_name}</em><br>{i_name}</h1>
  <p>{d_desc}</p>
  <div class="btns">
    <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr(lang,"cta")}</a>
  </div>
</section>
{trust_bar(lang)}
<div class="section section-alt"><div class="container">
  <div class="stag">💰 Norton Plans</div>
  <h2 class="stitle">Best Norton Deals in {country} — {YEAR}</h2>
  <div class="plan-grid fade">
    <div class="plan-card"><div class="plan-name">AntiVirus Plus</div><div class="plan-price">{currency} 19</div><div class="plan-yr">/year · first year</div><div class="plan-dev">1 Device</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
    <div class="plan-card"><div class="plan-name">360 Standard</div><div class="plan-price">{currency} 29</div><div class="plan-yr">/year · first year</div><div class="plan-dev">1 Device + VPN</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
    <div class="plan-card pop"><div class="pop-badge">⭐ Best Value</div><div class="plan-name">360 Deluxe</div><div class="plan-price">{currency} 39</div><div class="plan-yr">/year · first year</div><div class="plan-dev">5 Devices</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
    <div class="plan-card"><div class="plan-name">360 Advanced</div><div class="plan-price">{currency} 49</div><div class="plan-yr">/year · first year</div><div class="plan-dev">10 Devices</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
    <div class="plan-card"><div class="plan-name">360 Select</div><div class="plan-price">{currency} 99</div><div class="plan-yr">/year · first year</div><div class="plan-dev">10 + LifeLock</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
    <div class="plan-card"><div class="plan-name">360 Ultimate+</div><div class="plan-price">{currency} 299</div><div class="plan-yr">/year · first year</div><div class="plan-dev">Unlimited</div><a href="{AFF}" class="plan-cta" target="_blank" rel="nofollow sponsored">Get Deal →</a></div>
  </div>
  <p style="text-align:center;color:var(--muted);font-size:12px;margin-top:16px">* Prices approximate. Visit Norton for exact {country} pricing. All plans include 30-day free trial.</p>
</div></div>
{cta_band(f"Get the Best Norton Deal in {country}", f"30-day free trial + 60-day money-back. No credit card required.", lang)}
<div class="section"><div class="container">
  <div class="stag">How to Save</div>
  <h2 class="stitle">Money-Saving Tips for Norton in {country}</h2>
  <div class="card-grid fade">
    <div class="card"><div class="card-icon">🎟️</div><h3>Use Our Affiliate Link</h3><p>Click our link to get the best available Norton discount for {country} — prices updated regularly.</p></div>
    <div class="card"><div class="card-icon">🆓</div><h3>Start with Free Trial</h3><p>Always start with Norton's 30-day free trial. Full access to every feature, no credit card required.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>Choose the Right Plan</h3><p>Norton 360 Deluxe at 5 devices is the best value. Avoid overpaying for Ultimate+ unless you need unlimited devices.</p></div>
    <div class="card"><div class="card-icon">💯</div><h3>60-Day Guarantee</h3><p>Norton's 60-day money-back guarantee is the longest in the industry — longer than McAfee, Bitdefender, or Kaspersky.</p></div>
  </div>
</div></div>"""
    faq_items = [(q, "Norton offers a 30-day free trial with no credit card required, plus a 60-day money-back guarantee. Use our affiliate link for the best available discount in your country.") for q in d_faqs]
    faq_sec, faq_schema = make_faqs(faq_items, lang)
    rel = [(f"{d_name} Guide", f"{lc}-{d_slug}-guide.html"),
           (f"Best Antivirus {country}", f"{lc}-best-antivirus-review.html"),
           (f"Norton Free Trial", f"{lc}-norton-free-trial-guide.html"),
           (f"Norton Plans Comparison", f"{lc}-norton-plans-price-guide.html")]
    full = body + faq_sec + rel_section(rel, lang) + cta_band("Claim Your Norton Deal Now", "Prices change. Lock in your discount today.", lang)
    return slug, make_page(slug, title, desc, full, lang, faq_schema)

def make_family_page(lc, lang, country, f_slug, f_name, f_icon, f_desc, f_faqs, i_slug, i_name):
    slug  = f"{lc}-{f_slug}-{i_slug}.html"
    title = f"{f_name} — {i_name} {country} {YEAR} | BestAntivirusGuide"
    desc  = f"{f_name} {i_name} in {country}. {f_desc[:100]}... Complete guide for families {YEAR}."
    body  = f"""
<section class="hero">
  <div class="badge">{f_icon} Family Safety · {country} · {YEAR}</div>
  <h1>{f_icon} <em>{f_name}</em><br>{i_name}</h1>
  <p>{f_desc}</p>
  <div class="btns">
    <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr(lang,"cta")}</a>
    <a href="index.html" class="btn-ghost">← All Guides</a>
  </div>
</section>
{trust_bar(lang)}
<div class="section section-alt"><div class="container">
  <div class="stag">{f_icon} {f_name}</div>
  <h2 class="stitle">{f_name}: {i_name}</h2>
  <div class="card-grid fade">
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored">
      <div class="card-icon">{f_icon}</div><h3>{f_name}</h3>
      <p>{f_desc}</p><span class="card-link">Get Protected →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored">
      <div class="card-icon">👨‍👩‍👧</div><h3>Cover Your Whole Family</h3>
      <p>Norton 360 Deluxe covers 5 devices — parental controls, VPN, dark web monitoring, and identity protection for every family member.</p>
      <span class="card-link">See Family Plans →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored">
      <div class="card-icon">🆔</div><h3>LifeLock Identity Protection</h3>
      <p>Norton LifeLock monitors your whole family's identity 24/7 — SSN, credit, bank accounts, and dark web exposure.</p>
      <span class="card-link">Learn About LifeLock →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored">
      <div class="card-icon">🆓</div><h3>Try Free for 30 Days</h3>
      <p>Start your family's protection today. 30-day free trial, 60-day money-back guarantee. No credit card required.</p>
      <span class="card-link">Start Free Trial →</span></a>
  </div>
</div></div>
{cta_band(f"Protect Your Family with Norton 360", f"The #1 family antivirus in {country}. 30-day free trial.", lang)}"""
    faq_items = [(q, f"Norton 360 is the best choice for {f_name.lower()} — it covers up to 5 devices with parental controls, dark web monitoring, and LifeLock identity theft protection. Start a 30-day free trial.") for q in f_faqs]
    faq_sec, faq_schema = make_faqs(faq_items, lang)
    rel = [(f"Parental Controls Guide", f"{lc}-parental-controls-guide.html"),
           (f"Kids Online Safety", f"{lc}-kids-online-safety-guide.html"),
           (f"Identity Theft Families", f"{lc}-identity-theft-family-guide.html"),
           (f"Best Antivirus Family", f"{lc}-best-antivirus-family-review.html")]
    full = body + faq_sec + rel_section(rel, lang) + cta_band("Protect Your Family Today", "Norton 360 — 30-day free trial. 60-day money-back.", lang)
    return slug, make_page(slug, title, desc, full, lang, faq_schema)

def make_locale_page(lc, lang, country, currency, price, i_slug, i_name, i_kw):
    slug  = f"{lc}-{i_slug}.html"
    title = f"{i_name} — {country} {YEAR} | BestAntivirusGuide"
    desc  = f"Expert guide to {i_kw} in {country}. Norton 360 review, pricing in {currency}, deals, and family protection guide {YEAR}."
    body  = f"""
<section class="hero">
  <div class="badge">🌍 {country} Guide · {YEAR}</div>
  <h1>🛡️ <em>{i_name}</em><br>{country} {YEAR}</h1>
  <p>The complete {i_name.lower()} guide for {country}. Antivirus rankings, Norton deals, and family safety — from {currency} {price}/mo.</p>
  <div class="btns">
    <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr(lang,"cta")}</a>
  </div>
  <div class="stats">
    <div><div class="stat-n">#1</div><div class="stat-l">Norton 360</div></div>
    <div><div class="stat-n">9.7</div><div class="stat-l">Expert Score</div></div>
    <div><div class="stat-n">{currency} {price}</div><div class="stat-l">From/mo</div></div>
    <div><div class="stat-n">30</div><div class="stat-l">Day Trial</div></div>
  </div>
</section>
{trust_bar(lang)}
<div class="section section-alt"><div class="container">
  <div class="stag">🌍 {country}</div>
  <h2 class="stitle">{i_name} — {country}</h2>
  <div class="card-grid fade">
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🏆</div><h3>Best Antivirus {country}</h3><p>Norton 360 is the #1 rated antivirus in {country} — top detection, most features, best value.</p><span class="card-link">See Rankings →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">💸</div><h3>Best Norton Deal {country}</h3><p>Get Norton 360 from {currency} {price}/month in {country}. 30-day free trial, 60-day money-back.</p><span class="card-link">Get Deal →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">👨‍👩‍👧</div><h3>Family Safety {country}</h3><p>Parental controls, LifeLock identity theft protection, and kids online safety guide for {country}.</p><span class="card-link">Family Guide →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🆓</div><h3>Try Free in {country}</h3><p>Norton 360 free 30-day trial in {country}. Full access to all features, no credit card required.</p><span class="card-link">Start Free Trial →</span></a>
  </div>
</div></div>
{cta_band(f"Get Norton 360 in {country}", f"Best antivirus for {country} users. Try free for 30 days.", lang)}"""
    faq_items = [
        (f"What is the best antivirus in {country}?", f"Norton 360 is the #1 rated antivirus in {country} for {YEAR} — 99.9% detection rate, VPN, dark web monitoring, and LifeLock identity protection."),
        (f"How much does Norton cost in {country}?", f"Norton 360 starts from {currency} {price}/month in {country}. A 30-day free trial lets you test all features before paying."),
        (f"How do I protect my family online in {country}?", f"Norton 360 Deluxe is the best family antivirus in {country} — 5 devices, parental controls, identity theft monitoring, and 24/7 dark web alerts."),
        (f"Is Norton worth it in {country}?", f"Yes. Norton 360 tops independent lab tests in {country} and offers the most features at its price point. The 60-day money-back guarantee means zero risk."),
    ]
    faq_sec, faq_schema = make_faqs(faq_items, lang)
    rel = [(f"Best Antivirus {country}", f"{lc}-best-antivirus-review.html"),
           (f"Norton Deal {country}", f"{lc}-norton-deal-guide.html"),
           (f"Family Safety {country}", f"{lc}-protect-family-online-guide.html"),
           (f"Parental Controls {country}", f"{lc}-parental-controls-guide.html")]
    full = body + faq_sec + rel_section(rel, lang) + cta_band(f"Start Free Norton Trial in {country}", "30 days free. 60-day money-back guarantee.", lang)
    return slug, make_page(slug, title, desc, full, lang, faq_schema)

def make_state_page(st_slug, st_name, st_abbr, i_slug, i_name):
    slug  = f"us-{st_slug}-{i_slug}.html"
    title = f"{i_name} — {st_name} {YEAR} | BestAntivirusGuide"
    desc  = f"Best antivirus, Norton deals, and family safety guide for {st_name} ({st_abbr}) residents {YEAR}."
    body  = f"""
<section class="hero">
  <div class="badge">📍 {st_name}, {st_abbr} · {YEAR}</div>
  <h1>🛡️ <em>{i_name}</em><br>{st_name}</h1>
  <p>Expert antivirus rankings, Norton deals, and family safety tips for {st_name} residents. US-based 24/7 support included.</p>
  <div class="btns"><a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr("en","cta")}</a></div>
</section>
{trust_bar("en")}
<div class="section section-alt"><div class="container">
  <div class="stag">📍 {st_name}</div>
  <h2 class="stitle">{i_name} for {st_name} Residents</h2>
  <div class="card-grid fade">
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🏆</div><h3>Best Antivirus {st_name}</h3><p>Norton 360 is our #1 pick for {st_name} — best detection, most features, US-based 24/7 support.</p><span class="card-link">See Rankings →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">💸</div><h3>Best Norton Deal</h3><p>Get Norton 360 from $2.49/month. 30-day free trial + 60-day money-back guarantee.</p><span class="card-link">Get Deal →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">👨‍👩‍👧</div><h3>Family Safety {st_name}</h3><p>Parental controls, LifeLock identity protection, and dark web monitoring for every {st_name} family.</p><span class="card-link">Family Guide →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🆔</div><h3>LifeLock for {st_name}</h3><p>US-based identity protection — monitoring SSN, credit, and financial accounts for {st_abbr} residents.</p><span class="card-link">Learn About LifeLock →</span></a>
  </div>
</div></div>
{cta_band(f"Get Norton 360 in {st_name}", "30-day free trial. US-based 24/7 support.", "en")}"""
    faq_items = [
        (f"What is the best antivirus for {st_name}?", f"Norton 360 is our top pick for {st_name} with 99.9% detection, LifeLock identity theft protection, and 24/7 US-based customer support."),
        ("How much does Norton cost?", "Norton 360 starts from $29.99/year. 30-day free trial and 60-day money-back guarantee included."),
        (f"How do I protect my family online in {st_name}?", f"Norton 360 Deluxe covers 5 devices with parental controls and LifeLock — the best family antivirus for {st_name} households."),
        ("Is Norton worth buying?", "Yes. Norton 360 tops independent lab tests and offers the most complete feature set at its price. Zero risk with the 60-day money-back guarantee."),
    ]
    faq_sec, faq_schema = make_faqs(faq_items, "en")
    rel = [(f"Best Antivirus {st_name}", f"us-{st_slug}-best-antivirus.html"),
           (f"Norton Deal {st_name}", f"us-{st_slug}-norton-deal.html"),
           (f"Family Safety {st_name}", f"us-{st_slug}-protect-family.html"),
           (f"LifeLock {st_name}", f"us-{st_slug}-identity-theft.html")]
    full = body + faq_sec + rel_section(rel, "en") + cta_band(f"Protect Your {st_name} Family", "30-day free trial. 60-day money-back.", "en")
    return slug, make_page(slug, title, desc, full, "en", faq_schema)

def make_longtail_page(lt_slug, lt_name, lt_kw):
    slug  = f"{lt_slug}.html"
    title = f"{lt_name} | BestAntivirusGuide {YEAR}"
    desc  = f"Complete guide to {lt_kw}. Expert recommendations, Norton deals, and family safety tips for {YEAR}."
    body  = f"""
<section class="hero" style="padding:60px 24px 48px">
  <div class="badge">🔍 Expert Guide · {YEAR}</div>
  <h1>🔍 <em>{lt_name}</em></h1>
  <p>Complete expert guide to {lt_kw} for {YEAR}.</p>
  <div class="btns"><a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">{tr("en","cta")}</a></div>
</section>
{trust_bar("en")}
<div class="section section-alt"><div class="container">
  <div class="stag">🔍 Expert Analysis</div>
  <h2 class="stitle">{lt_name}</h2>
  <div class="card-grid fade">
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">🏆</div><h3>Our Top Pick: Norton 360</h3><p>For {lt_kw}, Norton 360 is our #1 recommendation — 99.9% detection, unlimited VPN, LifeLock, dark web monitoring, and a 30-day free trial.</p><span class="card-link">Try Norton Free →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">💸</div><h3>Best Deal Available</h3><p>Try Norton 360 free for 30 days. Plans from $29.99/year. 60-day money-back guarantee — no risk.</p><span class="card-link">Get Best Deal →</span></a>
    <a href="{AFF}" class="card" target="_blank" rel="nofollow sponsored"><div class="card-icon">👨‍👩‍👧</div><h3>Protect Your Family</h3><p>Norton 360 Deluxe covers your whole family — parental controls, identity theft protection, and 5 devices.</p><span class="card-link">Family Guide →</span></a>
  </div>
</div></div>
<div class="section"><div class="container">
  <div class="faq-list fade">
    <div class="faq-item"><div class="faq-q">What is the best answer for {lt_kw}?</div><div class="faq-a">Norton 360 is consistently our top recommendation for {lt_kw}. It combines the highest malware detection rate with the most comprehensive feature set — VPN, dark web monitoring, parental controls, LifeLock, and cloud backup — at a competitive price with a 30-day free trial.</div></div>
    <div class="faq-item"><div class="faq-q">Is Norton 360 worth it for {lt_kw}?</div><div class="faq-a">Yes. Norton 360 earns a 9.7/10 expert score and tops independent tests from AV-TEST and AV-Comparatives. The 30-day free trial and 60-day money-back guarantee mean zero risk.</div></div>
    <div class="faq-item"><div class="faq-q">How do I get started?</div><div class="faq-a">Visit Norton via our link and start a 30-day free trial. Full access to all Norton 360 features — no credit card required to begin.</div></div>
  </div>
</div></div>
{cta_band(f"Start Free Norton Trial Today", "30-day free trial. 60-day money-back guarantee.", "en")}
<div class="section section-alt"><div class="container">
  <div class="stag">Related</div>
  <div class="rel-grid">
    {"".join(f'<a href="{ls2}.html" class="rel-link">🛡️ {ln2}</a>' for ls2,ln2,lk2 in LONG_TAILS[:12] if ls2 != lt_slug)}
  </div>
</div></div>"""
    return slug, make_page(slug, title, desc, body, "en")

# ── INDEX ─────────────────────────────────────────────────────────────────────
def make_index():
    cat_cards = "".join(f'<a href="us-{c_slug}-review.html" class="card"><div class="card-icon">{c_icon}</div><h3>{c_name}</h3><p>{c_desc[:80]}...</p><span class="card-link">See Rankings →</span></a>' for c_slug,c_name,c_icon,c_desc,c_faqs in CATEGORIES[:8])
    hot = {"norton-promo-code","norton-free-trial","norton-black-friday"}
    def _deal_card(d_slug,d_name,d_icon,d_desc,d_faqs):
        is_hot = d_slug in hot
        badge = '<div class="deal-badge">🔥 HOT</div>' if is_hot else ""
        cls = "deal-card hot" if is_hot else "deal-card"
        return f'<div class="{cls}">{badge}<div class="deal-icon">{d_icon}</div><div class="deal-title">{d_name}</div><div class="deal-desc">{d_desc[:80]}...</div><a href="us-{d_slug}-guide.html" class="deal-cta" target="_blank" rel="nofollow sponsored">See Deal →</a></div>'
    deal_cards = "".join(_deal_card(*row) for row in DEAL_TOPICS[:6])
    fam_cards = "".join(f'<a href="us-{f_slug}-guide.html" class="card"><div class="card-icon">{f_icon}</div><h3>{f_name}</h3><p>{f_desc[:80]}...</p><span class="card-link">Read Guide →</span></a>' for f_slug,f_name,f_icon,f_desc,f_faqs in FAMILY_TOPICS[:8])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Best Antivirus {YEAR} | Norton Deals | Family Safety Guide | BestAntivirusGuide</title>
<meta name="description" content="BestAntivirusGuide — expert antivirus rankings, Norton 360 deals, and complete family online safety guides for {YEAR}. Try Norton free for 30 days."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{BASE_URL}/"/>
{FONTS}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"BestAntivirusGuide","url":"{BASE_URL}/","description":"Best antivirus rankings, Norton deals, and family safety guides {YEAR}."}}
</script>
<style>{CSS}</style>
</head>
<body>
{nav_html("en")}
<section class="hero">
  <div class="badge">🏆 #1 Antivirus Guide · 13 Countries · {YEAR}</div>
  <h1>Best Antivirus, <em>Best Deals</em>,<br>Best Family Protection</h1>
  <p>Expert antivirus rankings, the biggest Norton discounts, and complete family online safety guides — all in one place.</p>
  <div class="btns">
    <a href="{AFF}" class="btn-y" target="_blank" rel="nofollow sponsored">Try Norton Free — 30 Days</a>
    <a href="best-antivirus-2026-review.html" class="btn-ghost">See Rankings ↓</a>
  </div>
  <div class="stats">
    <div><div class="stat-n">#1</div><div class="stat-l">Norton 360</div></div>
    <div><div class="stat-n">9.7</div><div class="stat-l">Expert Score</div></div>
    <div><div class="stat-n">17K+</div><div class="stat-l">Pages</div></div>
    <div><div class="stat-n">13</div><div class="stat-l">Countries</div></div>
  </div>
</section>
{trust_bar("en")}

<div class="section section-alt" id="rankings">
  <div class="container">
    <div class="stag">🏆 Rankings</div>
    <h2 class="stitle">Best Antivirus Software {YEAR}</h2>
    <div class="rank-list fade" style="max-width:820px;margin-bottom:40px">
      <div class="rank-item rank-1">
        <div class="rank-num">01</div><div class="rank-icon">🛡️</div>
        <div class="rank-info">
          <div class="rank-name">Norton 360 <span class="rank-badge">BEST OVERALL {YEAR}</span></div>
          <div class="rank-desc">99.9% detection · Unlimited VPN · Dark web monitoring · LifeLock identity protection · 50M+ users · AV-TEST certified</div>
          <a href="{AFF}" class="rank-cta" target="_blank" rel="nofollow sponsored">Try Free 30 Days →</a>
        </div>
        <div class="rank-score"><div class="rank-score-num">9.7</div><div class="rank-score-label">/ 10</div></div>
      </div>
      <div class="rank-item"><div class="rank-num">02</div><div class="rank-icon">🔵</div><div class="rank-info"><div class="rank-name">Bitdefender</div><div class="rank-desc">Strong detection, fewer features — no LifeLock, limited VPN on base plans</div></div><div class="rank-score"><div class="rank-score-num">9.2</div><div class="rank-score-label">/ 10</div></div></div>
      <div class="rank-item"><div class="rank-num">03</div><div class="rank-icon">🔴</div><div class="rank-info"><div class="rank-name">McAfee</div><div class="rank-desc">Good for families but slower performance and no identity theft coverage</div></div><div class="rank-score"><div class="rank-score-num">8.8</div><div class="rank-score-label">/ 10</div></div></div>
      <div class="rank-item"><div class="rank-num">04</div><div class="rank-icon">⚪</div><div class="rank-info"><div class="rank-name">Kaspersky</div><div class="rank-desc">High detection but privacy concerns for US/UK/EU users</div></div><div class="rank-score"><div class="rank-score-num">8.5</div><div class="rank-score-label">/ 10</div></div></div>
      <div class="rank-item"><div class="rank-num">05</div><div class="rank-icon">🟢</div><div class="rank-info"><div class="rank-name">Avast Free</div><div class="rank-desc">Popular free option but history of selling user data — Norton trial is safer</div></div><div class="rank-score"><div class="rank-score-num">7.5</div><div class="rank-score-label">/ 10</div></div></div>
    </div>
    <div class="stag" style="margin-bottom:14px">All Categories</div>
    <div class="card-grid">{cat_cards}</div>
  </div>
</div>

{cta_band("Try the #1 Antivirus Free", "Norton 360 — 30-day free trial. No credit card required.")}

<div class="section" id="deals">
  <div class="container">
    <div class="stag">💸 Deals</div>
    <h2 class="stitle">Best Norton Deals & Discounts {YEAR}</h2>
    <div class="deal-grid fade">{deal_cards}</div>
  </div>
</div>

<div class="section section-alt" id="family">
  <div class="container">
    <div class="stag">👨‍👩‍👧 Family Safety</div>
    <h2 class="stitle">Protect Your Family Online</h2>
    <div class="card-grid fade">{fam_cards}</div>
  </div>
</div>

{cta_band("Complete Family Protection with Norton 360", "Covers 5 devices · Parental controls · LifeLock · VPN · Dark web monitoring")}
{footer_html("en")}
{sticky("en")}
<script>{JS}</script>
</body>
</html>"""

# ── SITEMAP / ROBOTS / LLMS ───────────────────────────────────────────────────
def make_sitemap(slugs):
    iso = now.strftime("%Y-%m-%d")
    sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += f'  <url><loc>{BASE_URL}/</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>{iso}</lastmod></url>\n'
    for s in slugs:
        sm += f'  <url><loc>{BASE_URL}/{s}</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>{iso}</lastmod></url>\n'
    sm += '</urlset>\n'
    return sm

def make_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build.py\nDisallow: /.github/\nSitemap: {BASE_URL}/sitemap.xml\n"

def make_llms():
    return f"""# BestAntivirusGuide — Norton 360 Global Affiliate
> Updated: {DATE_STR}
> Angles: #1 Best Antivirus Rankings | Norton Deals & Discounts | Protect Your Family Online
> 13 locales · 17,070+ pages
## Affiliate: {AFF}
## Site: {BASE_URL}/
"""

# ── GIT PUSH ──────────────────────────────────────────────────────────────────
def run_cmd(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print(r.stdout.strip())
    return r.returncode

def git_push(tag):
    run_cmd("git add -A")
    n = int(subprocess.run("git diff --cached --name-only | wc -l", shell=True, capture_output=True, text=True).stdout.strip())
    if n == 0:
        print("Nothing to commit"); return True
    run_cmd(f'git commit -m "nortonantivirus sync {tag}"')
    for i in range(1, 7):
        print(f"Push attempt {i}...")
        run_cmd("git fetch origin main")
        if run_cmd("git rebase origin/main") != 0:
            run_cmd("git rebase --abort"); time.sleep(8); continue
        if run_cmd("git push origin HEAD:main") == 0:
            print(f"✅ Pushed {n:,} files"); return True
        time.sleep(8)
    print("❌ Push failed"); return False

# ── MAIN ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"🛡️  BestAntivirusGuide Build — {DATE_STR}  sync={SYNC}")
    total_est = (len(LOCALES)*len(CATEGORIES)*len(CATEGORY_INTENTS) +
                 len(LOCALES)*len(DEAL_TOPICS)*len(DEAL_INTENTS) +
                 len(LOCALES)*len(FAMILY_TOPICS)*len(FAMILY_INTENTS) +
                 len(LOCALES)*len(LOCALE_INTENTS) +
                 len(US_STATES)*len(STATE_INTENTS) +
                 len(LONG_TAILS))
    print(f"   Estimated pages: {total_est:,}")

    with open("index.html","w",encoding="utf-8") as f: f.write(make_index())
    with open("robots.txt","w",encoding="utf-8") as f: f.write(make_robots())
    with open("llms.txt","w",encoding="utf-8") as f: f.write(make_llms())
    with open(".nojekyll","w") as f: f.write("")
    print("✅ index.html  robots.txt  llms.txt  .nojekyll")

    slugs = []
    count = 0
    BATCH = 8000

    def write(slug, html):
        global count
        with open(slug,"w",encoding="utf-8") as f: f.write(html)
        slugs.append(slug)
        count += 1
        if count % 2000 == 0: print(f"   {count:,} pages written...")
        if count % BATCH == 0: git_push(f"{SYNC}-b{count//BATCH}")

    print("   Category pages (Best Antivirus angle)...")
    for lc,lang,country,currency,price in LOCALES:
        for c_slug,c_name,c_icon,c_desc,c_faqs in CATEGORIES:
            for i_slug,i_name,*_ in CATEGORY_INTENTS:
                s,h = make_category_page(lc,lang,country,currency,price,c_slug,c_name,c_icon,c_desc,c_faqs,i_slug,i_name)
                write(s,h)

    print("   Deal pages (Norton Deals angle)...")
    for lc,lang,country,currency,price in LOCALES:
        for d_slug,d_name,d_icon,d_desc,d_faqs in DEAL_TOPICS:
            for i_slug,i_name,*_ in DEAL_INTENTS:
                s,h = make_deal_page(lc,lang,country,currency,price,d_slug,d_name,d_icon,d_desc,d_faqs,i_slug,i_name)
                write(s,h)

    print("   Family pages (Family Safety angle)...")
    for lc,lang,country,currency,price in LOCALES:
        for f_slug,f_name,f_icon,f_desc,f_faqs in FAMILY_TOPICS:
            for i_slug,i_name,*_ in FAMILY_INTENTS:
                s,h = make_family_page(lc,lang,country,f_slug,f_name,f_icon,f_desc,f_faqs,i_slug,i_name)
                write(s,h)

    print("   Locale pages...")
    for lc,lang,country,currency,price in LOCALES:
        for i_slug,i_name,i_kw in LOCALE_INTENTS:
            s,h = make_locale_page(lc,lang,country,currency,price,i_slug,i_name,i_kw)
            write(s,h)

    print("   US state pages...")
    for st_slug,st_name,st_abbr in US_STATES:
        for i_slug,i_name,*_ in STATE_INTENTS:
            s,h = make_state_page(st_slug,st_name,st_abbr,i_slug,i_name)
            write(s,h)

    print("   Long-tail pages...")
    for lt in LONG_TAILS:
        s,h = make_longtail_page(*lt)
        write(s,h)

    print(f"\n✅ {count:,} pages written")
    with open("sitemap.xml","w",encoding="utf-8") as f: f.write(make_sitemap(slugs))
    print(f"✅ sitemap.xml — {len(slugs)+1:,} URLs")
    git_push(f"{SYNC}-final")
