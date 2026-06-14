#!/usr/bin/env bash
# 글 발행 후 한 번에: 빌드 + 색인 통보.
#
# 사용법:
#   tools/publish.sh                                  # 빌드 + sitemap 전체 IndexNow 통보
#   tools/publish.sh https://도메인/magazine/새글/      # 빌드 + 해당 URL만 통보(권장)
#
# 구글 Indexing API 도 함께 보내려면 서비스계정 JSON 경로를 환경변수로 지정:
#   GOOGLE_APPLICATION_CREDENTIALS=/path/sa.json tools/publish.sh https://도메인/magazine/새글/
#
# ⚠ IndexNow 는 키 파일(/{KEY}.txt)이 실제 도메인에서 열려야 수락됩니다 — 배포 후 실행하세요.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "▶ 빌드 (sitemap·feed·robots·IndexNow 키파일 갱신)"
python3 build.py >/dev/null

echo "▶ IndexNow 통보 (빙·네이버·얀덱스)"
python3 tools/indexnow.py "$@"

if [ -n "${GOOGLE_APPLICATION_CREDENTIALS:-}" ]; then
  echo "▶ 구글 Indexing API 통보"
  python3 tools/google_indexing.py "$@"
else
  echo "ℹ 구글 Indexing API 는 건너뜀 (GOOGLE_APPLICATION_CREDENTIALS 미설정)."
  echo "  구글은 Search Console 의 sitemap 제출 + URL 검사 색인요청이 가장 확실합니다."
fi

echo "✓ 완료"
