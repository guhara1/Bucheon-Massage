# 지역별 안내 — 부천시 허브 1개 + 행정구 허브 3개(원미구·소사구·오정구).
# 대표 행정동 페이지는 dongs_wonmi / dongs_sosa / dongs_ojeong 모듈에서 정의한다.
# 숫자 행정동(심곡1동, 중1동, 상1동 등) 개별 페이지는 만들지 않는다.
from .site import PHONE, PHONE_DISPLAY
from .pricing import PRICING

_CTA = f"""
<section class="cta">
<h2>예약문의</h2>
<p>방문 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

# ─────────────────────────────────────────── 부천시 전체 허브
_HUB_BODY = """
<p class="lead">부천 방문 관리는 원미구·소사구·오정구 세 행정구와 그 아래 대표 행정동을 기준으로 안내합니다. 거주하시는 행정동이 심곡1동·중3동처럼 숫자로 나뉘어 있어도 아래 대표 동 페이지에서 필요한 정보를 모두 확인하실 수 있습니다.</p>

<section>
<h2>부천시 지역 안내 구성</h2>
<p>경기도 부천시는 서울 서남권과 인천 사이에 자리한 도시로, 면적은 넓지 않지만 원미구·소사구·오정구 세 행정구가 뚜렷한 생활권을 이룹니다. 원미구는 부천역·신중동·상동·중동을 중심으로 부천에서 가장 강한 상권과 역세권을 품고 있고, 소사구는 소사역·송내역·옥길지구를 중심으로 주거지와 교통 접근성이 함께 있는 생활권입니다. 오정구는 원종동·고강동·오정동을 중심으로 서해선 역세권과 차량 이동 기준이 함께 작동하는 지역입니다. 이 사이트는 행정구 페이지를 먼저 두고, 그 아래에 대표 행정동 페이지와 지하철역 페이지를 연결하는 구조로 만들어 이용자가 자기 위치를 빠르게 찾도록 돕습니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단하므로, 대표 동 기준 안내가 실제 이용 흐름과 일치합니다.</p>
</section>

<section>
<h2>행정구별 안내</h2>
<ul class="card-grid">
<li><a href="/bucheon/wonmi-gu-chuljangmassage/">원미구 출장마사지</a></li>
<li><a href="/bucheon/sosa-gu-chuljangmassage/">소사구 출장마사지</a></li>
<li><a href="/bucheon/ojeong-gu-chuljangmassage/">오정구 출장마사지</a></li>
</ul>
<p>원미구는 부천 중심 상권과 신도시 역세권이 모여 있고, 소사구는 소사·송내 생활권과 옥길·범박 주거지가 함께 있으며, 오정구는 원종·고강·오정 생활권과 서해선 축을 중심으로 합니다. 각 행정구 페이지에서 생활권 차이와 대표 동, 가까운 역세권을 자세히 설명합니다.</p>
</section>

<section>
<h2>대표 행정동 20곳</h2>
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
</section>

<section>
<h2>통합 안내 기준</h2>
<p>심곡1동·심곡2동·심곡3동은 심곡동 페이지에서, 원미1동·원미2동은 원미동 페이지에서 함께 안내합니다. 중동과 중1~4동은 중동 페이지로, 상동과 상1~3동은 상동 페이지로 통합됩니다. 소사구의 심곡본1동·심곡본동은 심곡본동으로, 소사본동·소사본1동은 소사본동으로, 송내1동·송내2동은 송내동으로 묶습니다. 오정구의 원종1동·원종2동은 원종동, 고강본동·고강1동은 고강동 페이지로 통합합니다. 숫자 동 단위의 개별 페이지는 만들지 않는 것이 원칙입니다. 행정동 경계는 행정 편의를 위한 구분일 뿐 생활권의 경계가 아니고, 방문 관리에서 중요한 것은 행정동 이름이 아니라 정확한 주소이기 때문입니다.</p>
</section>

<section>
<h2>지역과 역세권을 함께 확인하세요</h2>
<p>부천은 1호선(경인선)·7호선·서해선이 지나는 지역이라 동 기준보다 역 기준이 익숙한 분도 많습니다. <a href="/bucheon/bucheon-station-chuljangmassage/">부천역</a>, <a href="/bucheon/sosa-station-chuljangmassage/">소사역</a>, <a href="/bucheon/sang-dong-station-chuljangmassage/">상동역</a>, <a href="/bucheon/wonjong-station-chuljangmassage/">원종역</a>처럼 역 인근 위치에서 예약하실 때는 <a href="/bucheon/stations/">지하철역별 안내</a>를 함께 확인해 보세요. 역 페이지에서는 해당 역세권의 생활권과 인접 동을 연결해 설명합니다. 다만 역과 동, 테마를 조합한 별도 페이지는 운영하지 않으므로, 원하시는 관리 유형은 <a href="/themes/aroma/">아로마</a>나 <a href="/themes/homecare/">홈케어</a> 같은 테마별 안내에서 따로 확인하시면 됩니다.</p>
</section>

<section>
<h2>예약 전 참고사항</h2>
<p>어느 동이든 예약 절차는 동일합니다. 위치 확인, 시간 확인, 코스·인원 확인, 방문 가능 여부 안내, 예약 확정 순서로 진행되며, 저녁 시간대와 주말은 문의가 몰릴 수 있어 미리 연락 주시는 편이 좋습니다. 아파트 단지는 동·호수와 공동현관 출입 방법을, 오피스텔과 숙소는 건물 출입 안내를 함께 알려주시면 방문이 한층 매끄럽습니다. 옥길동·고강동·오정동처럼 차량 이동이 기준이 되는 지역은 추가 이동비 여부를 함께 확인해 두시면 좋습니다. 부천시 경계와 맞닿은 인천 부평·계양, 서울 강서·구로·양천, 광명·시흥 방면 주소도 위치에 따라 방문이 가능할 수 있으니 전화로 확인해 주세요. 자세한 준비사항은 <a href="/guide/">이용가이드</a>에서, 예약 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>우리 동네 행정동 이름이 안 보여요.</h3>
<p>심곡1동·중3동·상2동처럼 숫자가 붙은 행정동은 모두 대표 동 페이지에 통합되어 있습니다. 예를 들어 중3동은 중동 페이지, 상2동은 상동 페이지를 보시면 됩니다.</p>
</div>
<div class="faq-item">
<h3>행정구 경계가 애매한 위치는 어떻게 하나요?</h3>
<p>경계 지역은 어느 페이지를 보셔도 무방합니다. 실제 방문은 주소 기준으로 진행되므로 예약 전화에서 정확한 도로명 주소만 알려주시면 동일한 기준으로 안내해 드립니다.</p>
</div>
</section>
"""

HUB = {
    "path": "bucheon/",
    "title": "부천 지역별 출장마사지｜원미구·소사구·오정구 안내",
    "desc": "부천 출장마사지·홈타이 예약 전 원미구·소사구·오정구 대표 동을 확인하세요.",
    "h1": "부천 지역별 출장마사지·홈타이 안내",
    "body": _HUB_BODY + _CTA,
    "breadcrumb": [("부천 지역별 안내", None)],
}

# ─────────────────────────────────────────── 원미구
_WONMI_BODY = """
<p class="lead">원미구는 부천역·신중동·상동·중동을 중심으로 부천에서 가장 강한 상권과 역세권이 모인 행정구로, 심곡동·원미동·소사동·역곡동·춘의동·도당동·약대동·중동·상동 아홉 개 대표 동으로 안내합니다.</p>

<section>
<h2>원미구 생활권 특징</h2>
<p>원미구는 부천의 중심부에 해당합니다. 1호선 부천역을 낀 심곡동 원도심 상권부터, 7호선 신중동역·부천시청역을 따라 펼쳐진 중동신도시 상권, 상동역 일대의 상동신도시까지 부천의 핵심 생활권이 대부분 원미구 안에 있습니다. 부천역 일대는 지하상가와 먹자골목, 로데오 거리가 형성된 전통 상권이고, 중동·상동은 대단지 아파트와 백화점·대형마트가 어우러진 신도시 생활권입니다. 동쪽으로는 역곡역을 중심으로 가톨릭대학교와 대학가 상권이 자리하고, 북쪽으로는 춘의동·도당동에 부천테크노파크와 산업 시설이 함께 있습니다. 한 행정구 안에 원도심·신도시·대학가·산업단지가 모두 들어 있어, 출장마사지 방문 수요도 상권 중심의 저녁·심야 예약과 주거 단지 중심의 가족 단위 예약이 고루 나타납니다.</p>
</section>

<section>
<h2>원미구 대표 행정동</h2>
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
<p>심곡동과 원미동은 부천역 중심 상권과 연결되고, 중동과 상동은 신도시 상권과 아파트 단지 수요를 함께 가집니다. 춘의동은 춘의역·부천종합운동장역, 도당동과 약대동은 차량 이동과 주거·업무 생활권을 중심으로 안내합니다. 번호가 붙은 심곡1·2·3동, 원미1·2동, 중1~4동, 상1~3동은 각각 대표 동 페이지에서 통합해 다룹니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>원미구는 1호선과 7호선이 함께 지나는 행정구입니다. <a href="/bucheon/bucheon-station-chuljangmassage/">부천역</a>은 심곡동 원도심 상권의 중심이고, <a href="/bucheon/sinjung-dong-station-chuljangmassage/">신중동역</a>과 <a href="/bucheon/bucheon-cityhall-station-chuljangmassage/">부천시청역</a>은 중동신도시 상권을, <a href="/bucheon/sang-dong-station-chuljangmassage/">상동역</a>은 상동신도시를 담당합니다. 북부의 <a href="/bucheon/chunui-station-chuljangmassage/">춘의역</a>은 춘의동·도당동 생활권으로 이어집니다. 역 인근 위치라면 역 페이지에서 생활권과 방문 팁을 함께 확인하실 수 있습니다.</p>
</section>

<section>
<h2>이런 상황에 많이 이용하십니다</h2>
<p>원미구는 상권과 주거가 함께 있어 수요가 다양합니다. 신중동·상동 상권에서 회식이나 모임 후 피로를 푸는 직장인, 중동·상동 대단지에 거주하는 가족의 정기 관리, 부천역 인근 숙소에 머무는 출장·여행 고객, 역곡 대학가의 1인 가구, 재택근무로 굳은 어깨를 저녁에 푸는 분 등이 대표적입니다. 상권이 활발한 만큼 늦은 시간대 홈타이 문의도 다른 행정구보다 많은 편입니다.</p>
</section>

<section>
<h2>원미구 예약 가능 시간과 홈타이 안내</h2>
<p>원미구는 상권이 활발한 만큼 예약 가능 시간대가 폭넓습니다. 부천역·신중동·상동 상권은 늦은 저녁부터 심야까지 방문 수요가 이어지고, 중동·상동 대단지는 평일 낮과 주말 가족 단위 예약이 고르게 들어옵니다. 부천 홈타이는 자택·오피스텔·숙소 어디서든 예약 가능 여부를 먼저 확인한 뒤 이동 없이 받는 방문형 관리로, 받으실 공간과 시간만 정해지면 됩니다. 평일 저녁 7시부터 11시 사이와 주말은 문의가 몰려 한두 시간 이상 여유를 두고 연락 주시는 편이 좋습니다. 신중동·상동처럼 상권이 밀집한 구역은 저녁 차량 정체로 도착이 늦어질 수 있어, 시간이 확실하면 미리 예약을 걸어 두시는 것이 가장 확실합니다. 비용은 코스와 시간에 따라 예약 확정 단계에서 총액으로 먼저 안내되며, 원미구는 역세권 중심이라 추가 이동비 없이 진행되는 경우가 대부분입니다. 처음이라면 60분 기본 구성으로 시작해 보시고, 누적 피로가 깊다면 90분 이상을 권합니다.</p>
</section>

<section>
<h2>방문 전 확인사항</h2>
<p>원미구는 상가 오피스텔과 대단지 아파트가 섞여 있어 위치별 안내가 다릅니다. 상가·오피스텔은 건물명과 호수, 공동현관 출입 방법을, 아파트는 동·호수와 가까운 출입구를 알려주시면 좋습니다. 신중동·상동 상권 인근은 저녁에 주차가 혼잡하니 가까운 주차장이나 큰길 위치를 함께 일러 주세요. 어울리는 관리 유형은 <a href="/themes/swedish/">스웨디시</a>, <a href="/themes/aroma/">아로마</a>, <a href="/themes/homecare/">홈케어</a> 등에서 고르실 수 있고, 코스 구성은 <a href="/courses/">코스안내</a>를 참고하세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>원미구 소사동과 소사구는 다른가요?</h3>
<p>네. 원미구 소사동과 소사구는 행정 구역이 다릅니다. 원미구 소사동은 <a href="/bucheon/wonmi/sosa-dong-chuljangmassage/">소사동 페이지</a>에서, 소사구 생활권은 <a href="/bucheon/sosa-gu-chuljangmassage/">소사구 페이지</a>에서 안내합니다.</p>
</div>
<div class="faq-item">
<h3>중1동·상2동 같은 행정동은 어디서 보나요?</h3>
<p>중1~4동은 중동 페이지, 상1~3동은 상동 페이지에서 통합 안내합니다. 행정동 구분 없이 동일하게 진행됩니다.</p>
</div>
</section>
"""

WONMI_GU = {
    "path": "bucheon/wonmi-gu-chuljangmassage/",
    "title": "원미구 출장마사지｜부천 중심 상권 홈타이 예약 안내",
    "desc": "원미구 출장마사지·홈타이 예약 전 부천역, 신중동 생활권을 확인하세요.",
    "h1": "원미구 방문 관리 안내",
    "body": _WONMI_BODY + PRICING + _CTA,
    "breadcrumb": [("부천 지역별 안내", "/bucheon/"), ("원미구", None)],
}

# ─────────────────────────────────────────── 소사구
_SOSA_BODY = """
<p class="lead">소사구는 소사역·송내역 생활권과 옥길·범박 주거지를 함께 품은 부천 남부 행정구로, 심곡본동·소사본동·범박동·옥길동·괴안동·송내동 여섯 개 대표 동으로 안내합니다.</p>

<section>
<h2>소사구 생활권 특징</h2>
<p>소사구는 부천 남부에 자리한 행정구로, 1호선 소사역과 송내역, 그리고 서해선 소새울역을 따라 생활권이 형성되어 있습니다. 소사역 일대는 1호선과 서해선이 만나는 환승 거점이고, 송내역은 부천 남부의 관문이자 인천 부평과 맞닿은 상권입니다. 소사본동·심곡본동은 부천 원도심 남부의 주거·상가 혼합 지역이고, 괴안동은 역곡역 남측으로 서울 양천·구로와 가깝습니다. 반면 범박동과 옥길동은 산자락과 택지지구를 따라 들어선 대규모 아파트 단지로, 철도역과는 거리가 있어 차량 이동이 기준이 되는 주거권입니다. 교통 접근성이 좋은 역세권과 정주성이 강한 신축 주거지가 함께 있어, 소사구는 가족 단위 정기 관리 수요와 역 인근 직장인 수요가 고르게 나타나는 행정구입니다.</p>
</section>

<section>
<h2>소사구 대표 행정동</h2>
<ul class="card-grid">
<li><a href="/bucheon/sosa/simgokbon-dong-chuljangmassage/">심곡본동</a></li>
<li><a href="/bucheon/sosa/sosabon-dong-chuljangmassage/">소사본동</a></li>
<li><a href="/bucheon/sosa/beombak-dong-chuljangmassage/">범박동</a></li>
<li><a href="/bucheon/sosa/okgil-dong-chuljangmassage/">옥길동</a></li>
<li><a href="/bucheon/sosa/goean-dong-chuljangmassage/">괴안동</a></li>
<li><a href="/bucheon/sosa/songnae-dong-chuljangmassage/">송내동</a></li>
</ul>
<p>심곡본동과 소사본동은 소사역 주변 생활권을, 송내동은 송내역 중심 상권과 주거지를 함께 안내합니다. 범박동과 옥길동은 대규모 주거지와 차량 이동 기준을 중심으로, 괴안동은 역곡역과 소사 생활권을 함께 연결해 설명합니다. 심곡본1동·소사본1동·송내1·2동 같은 숫자 행정동은 각각 대표 동 페이지에서 통합해 다룹니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>소사구의 중심축은 <a href="/bucheon/sosa-station-chuljangmassage/">소사역</a>입니다. 1호선과 서해선이 환승하는 역으로 소사본동·심곡본동 생활권과 이어집니다. <a href="/bucheon/songnae-station-chuljangmassage/">송내역</a>은 송내동 중심 상권을, 서해선 <a href="/bucheon/sosaeul-station-chuljangmassage/">소새울역</a>은 소사본동 서측을 담당합니다. 동쪽 <a href="/bucheon/yeokgok-station-chuljangmassage/">역곡역</a>은 괴안동 생활권과 가깝습니다. 범박동·옥길동은 철도역과 거리가 있어 차량 이동을 기준으로 방문을 안내합니다.</p>
</section>

<section>
<h2>이런 상황에 많이 이용하십니다</h2>
<p>소사구는 주거 비중이 높아 가족 단위 정기 관리 문의가 꾸준합니다. 옥길지구·범박 대단지에 거주하며 외출이 번거로운 부모님을 위한 예약, 육아로 외출이 어려운 가정의 홈타이, 송내·소사 상권 회식 후 피로 해소, 역곡 인근 직장인의 퇴근 후 어깨·허리 관리 등이 대표적입니다. 신축 단지가 많아 거실 공간이 여유로워 집에서 받는 관리에 적합한 환경도 많습니다.</p>
</section>

<section>
<h2>소사구 예약 가능 시간과 홈타이 안내</h2>
<p>소사구는 주거 비중이 높아 평일 낮부터 저녁, 주말까지 가족 단위 예약이 꾸준합니다. 소사역·송내역 인근은 퇴근 후 직장인 수요가 더해지고, 옥길지구·범박 대단지는 육아 가정과 부모님 정기 관리 문의가 많습니다. 부천 홈타이는 집·숙소·사무실 어디서든 예약 가능 여부를 먼저 확인한 뒤 이동 없이 받는 방문형 관리로, 받으실 공간과 조용한 환경만 준비되면 됩니다. 저녁 시간대와 주말은 문의가 몰릴 수 있어 한두 시간 이상 여유를 두고 연락 주시면 좋습니다. 옥길동·범박동처럼 철도역과 거리가 있는 지역은 차량 이동을 기준으로 안내하므로, 예약 시 정확한 도로명 주소와 함께 추가 이동비 여부를 확인해 두시면 도착과 비용 안내가 한 번에 정리됩니다. 비용은 코스와 시간에 따라 예약 확정 단계에서 총액으로 먼저 안내되고, 방문 후 추가되는 비용은 없습니다.</p>
</section>

<section>
<h2>방문 전 확인사항</h2>
<p>소사구는 대단지 아파트가 많아 동·호수와 가까운 출입구, 방문객 주차 등록 여부를 알려주시면 도착이 빨라집니다. 옥길동·범박동처럼 철도역과 거리가 있는 지역은 차량 이동을 기준으로 안내하므로 정확한 도로명 주소가 특히 중요합니다. 어울리는 관리 유형은 <a href="/themes/aroma/">아로마</a>, <a href="/themes/homecare/">홈케어</a>, <a href="/themes/foot/">발마사지</a> 등에서 고르실 수 있고, 예약 절차는 <a href="/reservation/">예약안내</a>를 참고하세요.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>옥길동·범박동도 방문이 되나요?</h3>
<p>가능합니다. 다만 철도역과 거리가 있어 차량 이동을 기준으로 안내하므로, 정확한 도로명 주소와 단지·동·호수를 알려주시면 가능 여부와 도착 시간을 바로 확인해 드립니다.</p>
</div>
<div class="faq-item">
<h3>심곡본동과 원미구 심곡동은 같은 곳인가요?</h3>
<p>아니요. 소사구 심곡본동과 원미구 심곡동은 다른 행정동입니다. 심곡본동은 <a href="/bucheon/sosa/simgokbon-dong-chuljangmassage/">심곡본동 페이지</a>, 심곡동은 <a href="/bucheon/wonmi/simgok-dong-chuljangmassage/">심곡동 페이지</a>에서 안내합니다.</p>
</div>
</section>
"""

SOSA_GU = {
    "path": "bucheon/sosa-gu-chuljangmassage/",
    "title": "소사구 출장마사지｜소사역·송내역 생활권 홈타이 안내",
    "desc": "소사구 출장마사지·홈타이 이용 전 소사역, 송내역 주변 기준을 확인하세요.",
    "h1": "소사구 방문 관리 안내",
    "body": _SOSA_BODY + PRICING + _CTA,
    "breadcrumb": [("부천 지역별 안내", "/bucheon/"), ("소사구", None)],
}

# ─────────────────────────────────────────── 오정구
_OJEONG_BODY = """
<p class="lead">오정구는 원종·고강·오정 생활권과 서해선 역세권, 그리고 차량 이동 기준이 함께 작동하는 부천 북서부 행정구로, 성곡동·원종동·고강동·오정동·신흥동 다섯 개 대표 동으로 안내합니다.</p>

<section>
<h2>오정구 생활권 특징</h2>
<p>오정구는 부천 북서부에 자리해 서울 강서구와 인천 계양에 맞닿은 행정구입니다. 서해선 원종역이 지나며 원종동·고강동 일대 주거지가 가장 큰 비중을 차지하고, 오정동과 신흥동에는 오정산업단지와 부천테크노파크 같은 공업·업무 시설이 주거지와 섞여 있습니다. 성곡동은 여월지구 신축 아파트와 작동 생활권을 함께 두고 있고, 7호선 까치울역과 부천종합운동장역이 동쪽 경계 가까이 지납니다. 다른 행정구에 비해 철도 접근성이 고르지 않아 고강동·오정동은 차량 이동이 기준이 되는 지역이 많고, 서울 강서권(화곡·까치산)으로의 이동 동선도 함께 고려해야 합니다. 그만큼 오정구 안내에서는 방문 가능 시간, 정확한 주소 확인, 추가 이동비 여부를 다른 지역보다 더 분명하게 짚어 드리는 것이 중요합니다.</p>
</section>

<section>
<h2>오정구 대표 행정동</h2>
<ul class="card-grid">
<li><a href="/bucheon/ojeong/seonggok-dong-chuljangmassage/">성곡동</a></li>
<li><a href="/bucheon/ojeong/wonjong-dong-chuljangmassage/">원종동</a></li>
<li><a href="/bucheon/ojeong/gogang-dong-chuljangmassage/">고강동</a></li>
<li><a href="/bucheon/ojeong/ojeong-dong-chuljangmassage/">오정동</a></li>
<li><a href="/bucheon/ojeong/sinheung-dong-chuljangmassage/">신흥동</a></li>
</ul>
<p>성곡동은 여월동·작동 생활권을 함께 설명하고, 원종동은 서해선 원종역 주변 주거지를 중심으로 안내합니다. 고강동은 서울 강서권과 가까운 이동 동선을, 오정동과 신흥동은 공업·주거가 섞인 생활권을 중심으로 다룹니다. 원종1·2동, 고강본동·고강1동 같은 숫자 행정동은 각각 대표 동 페이지에서 통합해 안내합니다.</p>
</section>

<section>
<h2>가까운 역세권</h2>
<p>오정구의 철도 축은 서해선 <a href="/bucheon/wonjong-station-chuljangmassage/">원종역</a>입니다. 원종동·고강동 생활권의 관문 역할을 하며 검색 수요도 이 역을 중심으로 형성됩니다. 동쪽 경계로는 7호선 <a href="/bucheon/kkachiul-station-chuljangmassage/">까치울역</a>이 작동·성곡동 생활권과 가깝고, <a href="/bucheon/bucheon-stadium-station-chuljangmassage/">부천종합운동장역</a>은 7호선과 서해선이 만나는 환승 거점으로 춘의·여월 방면과 이어집니다. 고강동·오정동 안쪽은 철도역과 거리가 있어 차량 이동을 기준으로 안내합니다.</p>
</section>

<section>
<h2>이런 상황에 많이 이용하십니다</h2>
<p>오정구는 주거와 산업이 섞여 있어 수요가 다양합니다. 여월·원종 대단지에 거주하는 가족의 정기 관리, 서울 강서권으로 출퇴근하는 직장인의 퇴근 후 피로 관리, 오정·신흥 산업단지 인근 숙소·사무실 방문, 육아 가정의 홈타이 등이 대표적입니다. 차량 이동권이 많은 만큼 예약 시 위치와 시간을 먼저 정해 두면 방문이 한층 매끄럽습니다.</p>
</section>

<section>
<h2>오정구 예약 가능 시간과 홈타이 안내</h2>
<p>오정구는 주거와 산업이 섞여 있어 예약 시간대가 다양합니다. 원종·여월 대단지는 평일 저녁과 주말 가족 단위 예약이 많고, 오정·신흥 산업단지 인근은 사무실·숙소 방문과 늦은 시간대 문의가 더해집니다. 부천 홈타이는 자택·숙소·사무실 어디서든 예약 가능 여부를 먼저 확인한 뒤 이동 없이 받는 방문형 관리로, 공간과 시간만 정해지면 됩니다. 오정구는 다른 행정구보다 차량 이동 기준 지역이 많아, 예약 시 방문 가능 시간과 정확한 주소, 추가 이동비 여부를 함께 확인해 두는 것이 특히 중요합니다. 서울 강서권과 가까운 고강동·원종동은 출퇴근 시간대 교통 상황에 따라 도착 시간이 달라질 수 있어, 시간이 확실하면 미리 예약을 잡아 두시는 편이 좋습니다. 비용은 코스와 시간에 따라 예약 확정 단계에서 총액으로 먼저 안내됩니다.</p>
</section>

<section>
<h2>방문 전 확인사항</h2>
<p>오정구는 철도 접근성이 고르지 않아 정확한 도로명 주소가 특히 중요합니다. 단독·빌라가 많은 고강동은 건물 특징을, 대단지가 많은 원종동·성곡동은 동·호수와 가까운 출입구를 알려주세요. 차량 이동이 기준이 되는 위치는 추가 이동비 여부를 예약 시 함께 확인해 두면 좋습니다. 어울리는 관리 유형은 <a href="/themes/swedish/">스웨디시</a>, <a href="/themes/aroma/">아로마</a>, <a href="/themes/homecare/">홈케어</a> 등에서 고르실 수 있습니다.</p>
</section>

<section>
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>고강동·오정동은 지하철역이 멀던데 방문되나요?</h3>
<p>가능합니다. 철도역과 거리가 있어 차량 이동을 기준으로 안내하며, 정확한 도로명 주소를 알려주시면 가능 여부와 추가 이동비 여부를 함께 안내해 드립니다.</p>
</div>
<div class="faq-item">
<h3>원종1동·원종2동은 따로 페이지가 있나요?</h3>
<p>아니요. 원종1동과 원종2동은 모두 원종동 페이지 하나로 통합 안내합니다. 행정동 구분 없이 동일하게 진행됩니다.</p>
</div>
</section>
"""

OJEONG_GU = {
    "path": "bucheon/ojeong-gu-chuljangmassage/",
    "title": "오정구 출장마사지｜원종·고강·오정 생활권 방문 안내",
    "desc": "오정구 출장마사지·홈타이 예약 전 원종, 고강, 오정 생활권을 확인하세요.",
    "h1": "오정구 방문 관리 안내",
    "body": _OJEONG_BODY + PRICING + _CTA,
    "breadcrumb": [("부천 지역별 안내", "/bucheon/"), ("오정구", None)],
}

PAGES = [HUB, WONMI_GU, SOSA_GU, OJEONG_GU]
