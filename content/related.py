# 롱테일 내부링크 강화 — 페이지 하단에 맥락에 맞는 내부링크를 칩 형태로 노출한다.
# 새 조합 URL을 만들지 않고, 기존 정규 페이지로만 연결하되 앵커 텍스트를 롱테일로 구성한다.

# 지역(동) 링크 — 앵커는 롱테일, href 는 기존 정규 페이지
_DONG_LINKS = [
    ("상동 출장마사지·홈타이", "/bucheon/wonmi/sang-dong-chuljangmassage/"),
    ("중동 출장마사지·홈타이", "/bucheon/wonmi/jung-dong-chuljangmassage/"),
    ("역곡동 방문 마사지", "/bucheon/wonmi/yeokgok-dong-chuljangmassage/"),
    ("송내동 출장마사지", "/bucheon/sosa/songnae-dong-chuljangmassage/"),
    ("소사본동 홈타이", "/bucheon/sosa/sosabon-dong-chuljangmassage/"),
    ("원종동 방문 관리", "/bucheon/ojeong/wonjong-dong-chuljangmassage/"),
    ("옥길동 출장마사지", "/bucheon/sosa/okgil-dong-chuljangmassage/"),
    ("심곡동 출장마사지", "/bucheon/wonmi/simgok-dong-chuljangmassage/"),
]

# 역세권 링크
_STATION_LINKS = [
    ("부천역 출장마사지", "/bucheon/bucheon-station-chuljangmassage/"),
    ("상동역 출장마사지", "/bucheon/sang-dong-station-chuljangmassage/"),
    ("송내역 출장마사지", "/bucheon/songnae-station-chuljangmassage/"),
    ("신중동역 출장마사지", "/bucheon/sinjung-dong-station-chuljangmassage/"),
    ("소사역 출장마사지", "/bucheon/sosa-station-chuljangmassage/"),
    ("부천시청역 출장마사지", "/bucheon/bucheon-cityhall-station-chuljangmassage/"),
    ("원종역 출장마사지", "/bucheon/wonjong-station-chuljangmassage/"),
    ("역곡역 출장마사지", "/bucheon/yeokgok-station-chuljangmassage/"),
]

# 테마 링크
_THEME_LINKS = [
    ("스웨디시 마사지", "/themes/swedish/"),
    ("타이마사지·홈타이", "/themes/thai/"),
    ("아로마테라피", "/themes/aroma/"),
    ("발마사지", "/themes/foot/"),
    ("커플 마사지", "/themes/couple/"),
    ("24시간 출장마사지", "/themes/24hours/"),
    ("심야·수면 가능 마사지", "/themes/overnight/"),
    ("스포츠·경락 관리", "/themes/sports/"),
]

# 안내·전환 링크
_INFO_LINKS = [
    ("출장마사지 요금·코스 안내", "/courses/#price"),
    ("출장마사지 예약 방법", "/reservation/"),
    ("처음 이용 가이드", "/guide/#first"),
    ("이용 후기 모음", "/reviews/"),
    ("원미구 출장마사지", "/bucheon/wonmi-gu-chuljangmassage/"),
    ("소사구 출장마사지", "/bucheon/sosa-gu-chuljangmassage/"),
    ("오정구 출장마사지", "/bucheon/ojeong-gu-chuljangmassage/"),
]

# 페이지 유형별로 노출 순서를 바꿔 맥락을 맞춘다(중복 노출은 build 단계에서 제거).
_ORDER = {
    "home": _STATION_LINKS + _THEME_LINKS + _DONG_LINKS + _INFO_LINKS,
    "area_hub": _DONG_LINKS + _STATION_LINKS + _THEME_LINKS + _INFO_LINKS,
    "gu": _DONG_LINKS + _STATION_LINKS + _THEME_LINKS + _INFO_LINKS,
    "dong": _STATION_LINKS + _THEME_LINKS + _DONG_LINKS + _INFO_LINKS,
    "station_hub": _STATION_LINKS + _DONG_LINKS + _THEME_LINKS + _INFO_LINKS,
    "station": _DONG_LINKS + _THEME_LINKS + _STATION_LINKS + _INFO_LINKS,
    "theme_hub": _THEME_LINKS + _STATION_LINKS + _DONG_LINKS + _INFO_LINKS,
    "theme": _THEME_LINKS + _DONG_LINKS + _STATION_LINKS + _INFO_LINKS,
    "info": _INFO_LINKS + _STATION_LINKS + _THEME_LINKS + _DONG_LINKS,
    "reviews": _STATION_LINKS + _THEME_LINKS + _DONG_LINKS + _INFO_LINKS,
    "magazine": _THEME_LINKS + _STATION_LINKS + _INFO_LINKS + _DONG_LINKS,
    "about": _INFO_LINKS + _THEME_LINKS + _STATION_LINKS + _DONG_LINKS,
}

_HEADING = {
    "dong": "이 지역에서 함께 많이 찾는 안내",
    "station": "이 역 주변에서 함께 많이 찾는 안내",
    "theme": "함께 보면 좋은 테마와 지역",
    "gu": "이 지역에서 함께 많이 찾는 안내",
}


def related_block(path: str, kind: str, limit: int = 10) -> str:
    """페이지 유형에 맞는 롱테일 내부링크 칩 블록."""
    current = "/" + path
    pool = _ORDER.get(kind, _INFO_LINKS + _STATION_LINKS + _THEME_LINKS)
    seen = set()
    chips = []
    for label, href in pool:
        if href == current or href in seen:
            continue
        seen.add(href)
        chips.append(f'<a class="rel-chip" href="{href}">{label}</a>')
        if len(chips) >= limit:
            break
    if not chips:
        return ""
    heading = _HEADING.get(kind, "함께 많이 찾는 안내")
    return (
        '<nav class="related-links" aria-label="관련 안내">'
        f'<p class="related-title">{heading}</p>'
        f'<div class="rel-chips">{"".join(chips)}</div>'
        '</nav>'
    )
