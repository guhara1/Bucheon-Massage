# 전체 페이지 목록 집계
from . import (main, areas, dongs_wonmi, dongs_sosa, dongs_ojeong,
               stations, themes, info, magazine, about)

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + dongs_wonmi.PAGES
    + dongs_sosa.PAGES
    + dongs_ojeong.PAGES
    + stations.PAGES
    + themes.PAGES
    + info.PAGES
    + magazine.PAGES
    + [about.PAGE]
)
