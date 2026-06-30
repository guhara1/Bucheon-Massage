# 이용자 평가 데이터 — 화면 표시(별점·후기 카드)와 구조화 데이터(Review/AggregateRating)에
# 공용으로 사용한다. 표시되는 후기와 집계 평점을 같은 소스에서 만들어, 화면과 스키마가
# 항상 일치하도록(구글 리치 결과 정책 충족) 한다.
#
# ⚠ 운영 안내: 아래 REVIEWS 는 사이트 구조용 시드 데이터다. 실제 검증된 이용 후기로
#   교체·추가하면서 운영하는 것을 전제로 한다. 집계 평점(RATING_VALUE)과 후기 수
#   (RATING_COUNT)는 이 목록에서 자동 계산되므로, 목록만 관리하면 스키마가 자동으로 맞춰진다.

# (이름, 별점, 작성일, 이용지역(대표 동/역), 테마, 본문)
REVIEWS = [
    ("김О현", 5, "2026-06-21", "상동", "스웨디시",
     "상동 아파트로 불렀는데 예약 시간에 정확히 도착했어요. 압 세기를 중간에 두 번이나 맞춰주셔서 끝나고 어깨가 한결 가벼웠습니다. 다음에도 같은 코스로 받을 생각이에요."),
    ("이О우", 5, "2026-06-18", "부천역", "아로마",
     "부천역 근처 오피스텔에서 받았습니다. 향이 과하지 않고 은은해서 좋았고, 90분 내내 편하게 잠들 정도였어요. 응대도 친절하고 비용도 안내받은 그대로였습니다."),
    ("정О민", 4, "2026-06-15", "중동", "타이마사지",
     "홈타이로 처음 받아봤는데 스트레칭이 시원했어요. 다만 도착이 10분 정도 늦어 별 하나 뺐는데, 미리 연락 주셔서 기다리는 동안 불편하진 않았습니다."),
    ("박О서", 5, "2026-06-12", "송내동", "발마사지",
     "하루 종일 서서 일하느라 다리가 퉁퉁 부었는데 발부터 종아리까지 꼼꼼히 풀어주셨어요. 받고 나니 다리가 가벼워서 잠도 잘 왔습니다. 송내동까지 와주셔서 감사했어요."),
    ("최О진", 5, "2026-06-09", "신중동역", "스포츠",
     "운동 후 근육 회복 목적으로 불렀습니다. 불편한 부위를 먼저 물어보고 시간 배분을 해주셔서 만족스러웠어요. 다음 날 근육통도 덜했습니다."),
    ("한О래", 5, "2026-06-05", "역곡동", "홈케어",
     "부모님 선물로 대리 예약했는데, 어머니가 정말 좋아하셨어요. 연락도 미리 주시고 어른 응대도 편안하게 해주셔서 믿고 맡길 수 있었습니다."),
    ("오О빈", 4, "2026-05-30", "원종동", "스웨디시",
     "오정구 쪽은 차량 이동이라 늦을까 걱정했는데 시간 맞춰 와주셨어요. 압은 제 취향보다 살짝 약했지만 말하니 바로 조절해주셨습니다."),
    ("서О현", 5, "2026-05-27", "상동역", "커플",
     "커플로 동시에 받았어요. 관리사 두 분이 오셔서 같은 시간에 진행됐고, 둘 다 만족했습니다. 기념일에 받기 정말 좋았어요."),
    ("강О은", 5, "2026-05-23", "소사역", "아로마",
     "소사역 근처 집으로 불렀습니다. 위생 신경 많이 쓰시는 게 느껴졌고 시트도 새것으로 깔아주셨어요. 향과 손길 모두 좋아서 단골 될 것 같아요."),
    ("윤О수", 5, "2026-05-19", "춘의동", "타이마사지",
     "재택근무로 굳은 어깨랑 목을 집중적으로 풀고 싶었는데 딱 맞게 받았습니다. 시간 내내 설명도 차분하게 해주셔서 처음인데도 편했어요."),
    ("임О아", 5, "2026-05-14", "옥길동", "홈케어",
     "옥길지구라 방문 될까 했는데 차량으로 와주셨어요. 육아 중이라 외출이 어려운데 집에서 받을 수 있어서 정말 만족스러웠습니다."),
    ("조О혁", 4, "2026-05-10", "부천시청역", "스포츠",
     "퇴근 후 늦은 시간 예약했는데 가능했어요. 근막 이완 위주로 받았고 시원했습니다. 다음엔 90분으로 더 길게 받아보려고요."),
    ("배О린", 5, "2026-05-06", "고강동", "스웨디시",
     "예약 전화부터 친절했고 금액도 통화에서 총액으로 정확히 알려주셔서 현장에서 추가 요구가 전혀 없었어요. 깔끔한 진행 감사합니다."),
    ("남О준", 5, "2026-05-02", "원미동", "발마사지",
     "발이 너무 피곤한 날 불렀는데 발바닥 지압이 정말 시원했어요. 끝나고 물 챙겨 마시라고 안내도 해주시고 마무리까지 꼼꼼했습니다."),
    ("문О경", 5, "2026-04-27", "송내역", "아로마",
     "잠을 잘 못 자던 시기였는데 아로마 받고 그날 푹 잤어요. 조명 낮추고 받으니 효과가 더 좋더라고요. 정기적으로 받아볼 생각입니다."),
    ("신О호", 4, "2026-04-22", "오정동", "타이마사지",
     "산업단지 쪽 사무실로 불렀습니다. 좁은 공간인데도 매트 펴고 잘 진행해주셨어요. 시간은 정확했고 만족합니다."),
]

RATING_BEST = "5"
RATING_WORST = "1"
RATING_COUNT = len(REVIEWS)
RATING_VALUE = f"{sum(r[1] for r in REVIEWS) / RATING_COUNT:.1f}"


def _stars(n: int) -> str:
    full = "★" * n
    empty = "☆" * (5 - n)
    return (f'<span class="stars" aria-hidden="true">'
            f'<span class="stars-on">{full}</span>'
            f'<span class="stars-off">{empty}</span></span>')


def review_cards(reviews) -> str:
    """후기 카드 묶음 HTML(표시용 — 구조화 데이터는 JSON-LD 로 별도 제공)."""
    cards = []
    for name, rating, date, area, theme, body in reviews:
        cards.append(
            '<li class="review-card">'
            '<div class="review-head">'
            f'<span class="review-author">{name}</span>'
            f'{_stars(rating)}'
            f'<span class="review-score">{rating}.0</span>'
            '</div>'
            f'<p class="review-meta"><time datetime="{date}">'
            f'{date.replace("-", ". ")}</time> · {area} · {theme}</p>'
            f'<p class="review-body">{body}</p>'
            '</li>'
        )
    return "".join(cards)


def rating_summary() -> str:
    """별점 요약 헤더 HTML."""
    return (
        '<div class="rating-summary">'
        f'<span class="rating-num">{RATING_VALUE}</span>'
        f'{_stars(round(float(RATING_VALUE)))}'
        f'<span class="rating-count">이용 후기 {RATING_COUNT}건 기준</span>'
        '</div>'
    )


def reviews_widget(reviews) -> str:
    """서비스 페이지 하단에 들어가는 평점·후기 요약 위젯."""
    return (
        '<aside class="reviews-widget" aria-label="이용자 평가">'
        '<div class="reviews-widget-head">'
        '<h2>이용자 평가</h2>'
        f'{rating_summary()}'
        '</div>'
        f'<ul class="review-list">{review_cards(reviews)}</ul>'
        '<p class="reviews-more"><a href="/reviews/">전체 이용 후기 보기 →</a></p>'
        '</aside>'
    )


def reviews_full() -> str:
    """후기 페이지에 들어가는 전체 후기 목록."""
    return (
        '<aside id="list" class="reviews-widget">'
        '<div class="reviews-widget-head">'
        '<h2>이용 후기 모음</h2>'
        f'{rating_summary()}'
        '</div>'
        f'<ul class="review-list">{review_cards(REVIEWS)}</ul>'
        '</aside>'
    )


def pick_reviews(path: str, n: int = 3):
    """경로 기준으로 후기를 결정적으로 골라(페이지마다 다르게) 중복 느낌을 줄인다."""
    if not REVIEWS:
        return []
    start = sum(ord(c) for c in path) % len(REVIEWS)
    return [REVIEWS[(start + i) % len(REVIEWS)] for i in range(min(n, len(REVIEWS)))]
