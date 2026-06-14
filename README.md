# 간다GO — 부천 출장마사지·홈타이 안내 사이트

경기도 부천시(원미구·소사구·오정구) 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, Cloudflare Pages, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`, `feed.xml`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/FAQPage JSON-LD)
  areas.py          # 부천시 허브 + 행정구 허브 3개(원미구·소사구·오정구)
  dongs_wonmi.py    # 원미구 대표 행정동 9개
  dongs_sosa.py     # 소사구 대표 행정동 6개
  dongs_ojeong.py   # 오정구 대표 행정동 5개
  stations.py       # 지하철역별: 허브 + 13개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 허브 + 아티클
  about.py          # 운영자 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
assets/             # CSS, 모바일 내비 JS, 파비콘·OG 이미지
```

## URL 구조

```
/                                                       메인 (부천 출장마사지·홈타이)
/bucheon/                                               지역 허브 (부천시 전체)
/bucheon/{구}-gu-chuljangmassage/                        행정구 3개 (원미구·소사구·오정구)
/bucheon/wonmi/{동}-dong-chuljangmassage/                원미구 대표 행정동 9개
/bucheon/sosa/{동}-dong-chuljangmassage/                 소사구 대표 행정동 6개
/bucheon/ojeong/{동}-dong-chuljangmassage/               오정구 대표 행정동 5개
/bucheon/stations/                                      역 허브
/bucheon/{역}-station-chuljangmassage/                   지하철역 13개
/themes/{테마}/ /courses/ /reservation/ /guide/ /reviews/ /support/ /magazine/ /about/
```

대표 행정동(20):
- **원미구(9)**: 심곡동·원미동·소사동·역곡동·춘의동·도당동·약대동·중동·상동
- **소사구(6)**: 심곡본동·소사본동·범박동·옥길동·괴안동·송내동
- **오정구(5)**: 성곡동·원종동·고강동·오정동·신흥동

역(13): 부천역·역곡역·소사역·중동역·송내역·상동역·부천시청역·신중동역·춘의역·부천종합운동장역·까치울역·소새울역·원종역

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 행정동은 대표 동 단위만 (심곡1·2·3동 → 심곡동, 중1~4동 → 중동, 상1~3동 → 상동 등) — 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(소사역=1호선·서해선, 부천종합운동장역=7호선·서해선)도 URL 하나
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 메타 디스크립션은 **80자 이내** (네이버 기준)
- 실제 오프라인 매장 주소가 없으므로 LocalBusiness 계열 Schema 미사용 — Organization 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. 파비콘 PNG(`assets/favicon-16/32.png`, `apple-touch-icon.png`, `icon-192/512.png`)와
   `assets/og-image.png`를 **간다GO 브랜드(이니셜 G)** 기준으로 재생성
   (현재 `favicon.svg`만 G로 교체되어 있고 PNG·OG는 재생성 필요)
3. 네이버 서치어드바이저 사이트 인증이 필요하면 발급 코드를 `content/main.py`의 `_JSONLD` 상단에
   `<meta name="naver-site-verification" ...>` 형태로 추가 (이전 사이트 인증 코드는 제거되어 있음)
4. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
5. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
