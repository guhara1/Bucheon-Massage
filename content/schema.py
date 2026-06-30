# 구조화 데이터(JSON-LD) 중앙 생성기.
# 모든 페이지에 공통으로 업체(HealthAndBeautyBusiness)·빵부스러기(BreadcrumbList)를 넣고,
# 평점 위젯이 노출되는 페이지에는 화면과 동일한 AggregateRating·Review 를 함께 넣는다.
# (구글 리치 결과 정책: 마크업한 평점/후기는 해당 페이지에 실제로 보여야 한다.)
import json

from .site import BASE_URL, BRAND, PHONE
from . import reviews_data as rd

_BASE = BASE_URL.rstrip("/")
_BIZ_ID = f"{_BASE}/#business"
_SITE_ID = f"{_BASE}/#website"


def _business_node(show_rating: bool, reviews):
    node = {
        "@type": "HealthAndBeautyBusiness",
        "@id": _BIZ_ID,
        "name": BRAND,
        "url": f"{_BASE}/",
        "image": f"{_BASE}/assets/og-image.png",
        "logo": f"{_BASE}/assets/icon-512.png",
        "description": "부천시 전지역 방문 출장마사지·홈타이 예약 안내",
        "telephone": PHONE,
        "priceRange": "₩₩",
        "currenciesAccepted": "KRW",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "부천시",
            "addressRegion": "경기도",
            "addressCountry": "KR",
        },
        "areaServed": {"@type": "AdministrativeArea", "name": "경기도 부천시"},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59",
        },
    }
    if show_rating and reviews:
        node["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": rd.RATING_VALUE,
            "reviewCount": rd.RATING_COUNT,
            "bestRating": rd.RATING_BEST,
            "worstRating": rd.RATING_WORST,
        }
        node["review"] = [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": name},
                "datePublished": date,
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": rating,
                    "bestRating": 5,
                    "worstRating": 1,
                },
                "reviewBody": body,
            }
            for name, rating, date, area, theme, body in reviews
        ]
    return node


def _breadcrumb_node(crumbs, canonical):
    items = [{
        "@type": "ListItem",
        "position": 1,
        "name": "홈",
        "item": f"{_BASE}/",
    }]
    pos = 2
    for label, href in crumbs:
        url = (_BASE + href) if href else canonical
        items.append({
            "@type": "ListItem",
            "position": pos,
            "name": label,
            "item": url,
        })
        pos += 1
    return {"@type": "BreadcrumbList", "itemListElement": items}


def _website_node():
    return {
        "@type": "WebSite",
        "@id": _SITE_ID,
        "url": f"{_BASE}/",
        "name": BRAND,
        "inLanguage": "ko",
        "publisher": {"@id": _BIZ_ID},
    }


def build_schema(page: dict, canonical: str, show_rating: bool, reviews,
                 is_home: bool) -> str:
    graph = [_business_node(show_rating, reviews)]
    if is_home:
        graph.append(_website_node())
    crumbs = page.get("breadcrumb") or []
    if crumbs:
        graph.append(_breadcrumb_node(crumbs, canonical))
    data = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, indent=2)
            + "\n</script>\n")
