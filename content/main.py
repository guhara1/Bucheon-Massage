# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 실제 오프라인 매장 주소가 없으므로 LocalBusiness 계열 Schema 대신 Organization 을 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="8dfaacbe9760b878975c3faba743df7c895a75b5" />
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "부천시 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 원미구, 소사구, 오정구와 상동, 중동, 송내동, 역곡동 등 대표 행정동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "부천역이나 상동역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "부천역, 소사역, 상동역, 부천시청역, 부천종합운동장역, 원종역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "심곡1동, 중1동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "심곡1·2·3동은 심곡동, 중1~4동은 중동, 상1~3동은 상동 페이지에서 통합 안내합니다. 같은 생활권을 잘게 나누면 비슷한 내용이 반복되어 이용자에게도 혼란스럽기 때문입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 평일 저녁과 주말, 상동·신중동 상권 주변은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "부천 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스로, 출장마사지와 같은 방문 관리의 한 형태입니다. 코스와 테마에 따라 구성이 달라집니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 부천시 전지역</p>
    <h1>부천 출장마사지 · 부천시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>20개</strong><span>대표 행정동</span></li>
      <li><strong>13개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>부천시에서 출장마사지를 찾는 이유</h2>
<p>부천 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 부천시는 서울 서남권, 인천, 시흥, 광명 생활권과 연결되는 도시라 이동 수요가 꾸준합니다. 원미구는 부천역, 신중동, 상동, 중동처럼 상권과 역세권이 강한 지역이 많고, 소사구는 소사역, 송내역, 옥길동, 범박동처럼 주거지와 교통 접근성이 함께 있는 생활권입니다. 오정구는 원종동, 고강동, 오정동 중심으로 차량 이동 기준과 서해선 역세권을 함께 고려해야 합니다. 이 페이지는 부천시 전체 구조를 설명하는 허브 역할을 하며, 자세한 내용은 지역별·역세권별·테마별 안내에서 확인하실 수 있습니다.</p>
</section>

<section id="districts">
<h2>원미구·소사구·오정구 생활권 차이</h2>
<p>부천시 홈타이 사이트를 만들 때 가장 중요한 부분은 행정구와 대표 행정동 구조를 정확하게 나누는 것입니다. 부천은 원미구, 소사구, 오정구 생활권이 분명하게 나뉘기 때문에 메인페이지 아래에 행정구 페이지를 먼저 두고, 그 아래 대표 행정동 페이지와 지하철역 페이지를 연결하는 방식이 자연스럽습니다. 원미구 페이지는 부천역·신중동역·부천시청역·상동역 생활권을 중심으로, 소사구 페이지는 소사역·송내역·소새울역 생활권을 기준으로, 오정구 페이지는 원종역·고강동·오정동·성곡동 생활권을 중심으로 안내합니다. 이렇게 구성하면 사용자는 본인이 있는 지역을 빠르게 찾을 수 있고, 검색엔진도 사이트 구조를 명확하게 이해할 수 있습니다.</p>
<ul class="card-grid">
<li><a href="/bucheon/wonmi-gu-chuljangmassage/">원미구 출장마사지</a></li>
<li><a href="/bucheon/sosa-gu-chuljangmassage/">소사구 출장마사지</a></li>
<li><a href="/bucheon/ojeong-gu-chuljangmassage/">오정구 출장마사지</a></li>
</ul>
</section>

<section id="coverage">
<h2>부천시 전지역 방문 가능 안내</h2>
<p>부천은 법정동과 행정동이 세분되어 있지만, 이 사이트는 대표 행정동을 중심으로 안내합니다. 번호가 붙은 행정동은 개별 페이지로 만들지 않습니다. 심곡1·2·3동은 심곡동, 원미1·2동은 원미동, 중동과 중1~4동은 중동, 상동과 상1~3동은 상동으로 통합합니다. 소사구도 심곡본1동·심곡본동은 심곡본동, 소사본동·소사본1동은 소사본동, 송내1·2동은 송내동으로 묶습니다. 오정구는 원종1·2동을 원종동, 고강본동·고강1동을 고강동으로 통합합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하기보다, 대표 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하고 중복 콘텐츠 위험도 낮출 수 있기 때문입니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단합니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>대표 행정동 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<p class="area-group-label"><strong>원미구</strong></p>
<ul class="card-grid">
<li><a href="/bucheon/wonmi/simgok-dong-chuljangmassage/">심곡동</a></li>
<li><a href="/bucheon/wonmi/wonmi-dong-chuljangmassage/">원미동</a></li>
<li><a href="/bucheon/wonmi/sosa-dong-chuljangmassage/">소사동</a></li>
<li><a href="/bucheon/wonmi/yeokgok-dong-chuljangmassage/">역곡동</a></li>
<li><a href="/bucheon/wonmi/chunui-dong-chuljangmassage/">춘의동</a></li>
<li><a href="/bucheon/wonmi/dodang-dong-chuljangmassage/">도당동</a></li>
<li><a href="/bucheon/wonmi/yakdae-dong-chuljangmassage/">약대동</a></li>
<li><a href="/bucheon/wonmi/jung-dong-chuljangmassage/">중동</a></li>
<li><a href="/bucheon/wonmi/sang-dong-chuljangmassage/">상동</a></li>
</ul>
<p class="area-group-label"><strong>소사구</strong></p>
<ul class="card-grid">
<li><a href="/bucheon/sosa/simgokbon-dong-chuljangmassage/">심곡본동</a></li>
<li><a href="/bucheon/sosa/sosabon-dong-chuljangmassage/">소사본동</a></li>
<li><a href="/bucheon/sosa/beombak-dong-chuljangmassage/">범박동</a></li>
<li><a href="/bucheon/sosa/okgil-dong-chuljangmassage/">옥길동</a></li>
<li><a href="/bucheon/sosa/goean-dong-chuljangmassage/">괴안동</a></li>
<li><a href="/bucheon/sosa/songnae-dong-chuljangmassage/">송내동</a></li>
</ul>
<p class="area-group-label"><strong>오정구</strong></p>
<ul class="card-grid">
<li><a href="/bucheon/ojeong/seonggok-dong-chuljangmassage/">성곡동</a></li>
<li><a href="/bucheon/ojeong/wonjong-dong-chuljangmassage/">원종동</a></li>
<li><a href="/bucheon/ojeong/gogang-dong-chuljangmassage/">고강동</a></li>
<li><a href="/bucheon/ojeong/ojeong-dong-chuljangmassage/">오정동</a></li>
<li><a href="/bucheon/ojeong/sinheung-dong-chuljangmassage/">신흥동</a></li>
</ul>
<p>부천시 전체 구조가 궁금하시면 <a href="/bucheon/">부천시 전체 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>지하철역별 출장마사지 지역 SEO 구조</h2>
<p>지하철역별 페이지는 부천 지역 SEO에서 중요한 역할을 합니다. 부천역 출장마사지, 소사역 출장마사지, 상동역 출장마사지, 부천시청역 출장마사지, 원종역 출장마사지처럼 실제 검색어와 가까운 제목을 사용하면 검색 의도가 분명해집니다. 다만 같은 역을 노선별로 중복해서 만들지 않습니다. 소사역은 1호선과 서해선 환승역이지만 소사역 페이지 하나만 두고, 부천종합운동장역도 7호선과 서해선 성격을 한 페이지 안에서 설명합니다. 출구별 페이지나 역과 테마를 조합한 페이지도 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/bucheon/bucheon-station-chuljangmassage/">부천역</a></li>
<li><a href="/bucheon/yeokgok-station-chuljangmassage/">역곡역</a></li>
<li><a href="/bucheon/sosa-station-chuljangmassage/">소사역</a></li>
<li><a href="/bucheon/jung-dong-station-chuljangmassage/">중동역</a></li>
<li><a href="/bucheon/songnae-station-chuljangmassage/">송내역</a></li>
<li><a href="/bucheon/sang-dong-station-chuljangmassage/">상동역</a></li>
<li><a href="/bucheon/bucheon-cityhall-station-chuljangmassage/">부천시청역</a></li>
<li><a href="/bucheon/sinjung-dong-station-chuljangmassage/">신중동역</a></li>
<li><a href="/bucheon/chunui-station-chuljangmassage/">춘의역</a></li>
<li><a href="/bucheon/bucheon-stadium-station-chuljangmassage/">부천종합운동장역</a></li>
<li><a href="/bucheon/kkachiul-station-chuljangmassage/">까치울역</a></li>
<li><a href="/bucheon/sosaeul-station-chuljangmassage/">소새울역</a></li>
<li><a href="/bucheon/wonjong-station-chuljangmassage/">원종역</a></li>
</ul>
</section>

<section id="hometai">
<h2>부천 홈타이 예약 전 확인사항</h2>
<p>부천 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 출장마사지와 같은 방문 관리의 한 형태로, 받으실 공간과 시간만 정해지면 이동 없이 편하게 받으실 수 있습니다. 예약 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해 주세요. 부천은 도시 면적이 크지는 않지만 역세권, 주거권, 차량 이동권이 다양하게 섞여 있습니다. 부천역·신중동·상동은 역세권 접근성이 중요하고, 옥길동·고강동·오정동은 차량 이동 기준이 더 중요할 수 있어, 예약 전 위치와 희망 시간을 알려주시면 가능 여부를 정확히 안내해 드립니다.</p>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다. 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 특히 평일 저녁, 출퇴근 시간, 상동·신중동 상권 주변은 이동 상황에 따라 예약 가능 시간이 달라질 수 있으므로 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 숙소나 오피스텔로 방문을 요청하실 때는 건물 출입 안내와 예약 시간대 연락 가능 여부를 함께 알려주세요. 옥길동·고강동·오정동처럼 차량 이동이 기준이 되는 지역은 추가 이동비 여부를 예약 시 함께 확인해 두시면 좋습니다. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 과장된 표현, 허위 후기, 선정적인 문구 없이 이용 가능 지역, 예약 절차, 취소 기준, 개인정보 처리 기준, 고객 유의사항을 분명하게 안내드리며, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 합니다. 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>부천 출장마사지 사이트 이용 가이드</h2>
<div class="faq-item">
<h3>부천시 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 원미구, 소사구, 오정구와 상동, 중동, 송내동, 역곡동 등 대표 행정동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>부천역이나 상동역 근처도 가능한가요?</h3>
<p>부천역, 소사역, 상동역, 부천시청역, 부천종합운동장역, 원종역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>심곡1동, 중1동은 왜 따로 없나요?</h3>
<p>심곡1·2·3동은 심곡동, 중1~4동은 중동, 상1~3동은 상동 페이지에서 통합 안내합니다. 같은 생활권을 잘게 나누면 비슷한 내용이 반복되어 이용자에게도 혼란스럽기 때문입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 평일 저녁과 주말, 상동·신중동 상권 주변은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 어떻게 다른가요?</h3>
<p>부천 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스로, 출장마사지와 같은 방문 관리의 한 형태입니다. 코스와 테마에 따라 구성이 달라집니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>부천시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "부천 출장마사지｜부천시 홈타이 지역별 예약 안내",
    "desc": "부천 출장마사지·홈타이 예약 전 원미구, 소사구, 오정구 정보를 정리했습니다.",
    "h1": "부천 출장마사지 · 부천시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
