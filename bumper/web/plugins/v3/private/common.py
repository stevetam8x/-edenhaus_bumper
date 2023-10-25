"""Common plugin module."""
from collections.abc import Iterable

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import AbstractRouteDef

from ... import WebserverPlugin, get_success_response
from . import BASE_URL


class CommonPlugin(WebserverPlugin):
    """Common plugin."""

    @property
    def routes(self) -> Iterable[AbstractRouteDef]:
        """Plugin routes."""
        return [
            web.route(
                "*",
                f"{BASE_URL}common/getBottomNavigateInfoList",
                _handle_get_bottom_navigate_info_list,
            ),
        ]


async def _handle_get_bottom_navigate_info_list(_: Request) -> Response:
    """Get bottom navigation info list."""
    url_robot_1 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043812_d63702f64fb128bebc60ec0896f31a79.png"
    url_robot_2 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043819_a87e7cafd5672c16dadbdef81b86fa1a.png"
    url_store_1 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043844_5458a52b4a23448f9964958b741de17d.png"
    url_store_2 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043848_1cb4d24a3771e08b55145c495ed6fa76.png"
    url_mine_1 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043853_4164bc0efa98bc14b7fdb267b3d82bf1.png"
    url_mine_2 = "https://gl-us-pub.ecovacs.com/upload/global/2023/05/06/20230506043857_906efbe84aa46d02b26d357c8f5f074d.png"
    return get_success_response(
        {
            "bgImgUrl": None,
            "navigateInfoResponseList": [
                {
                    "bgImgUrl": None,
                    "defaultImgUrl": url_robot_1,
                    "iconId": "20231013052048_9f112534d439f8459fc77e4427a170e6",
                    "iconName": "Robot",
                    "iconType": "ROBOT",
                    "lightImgUrl": url_robot_2,
                    "lightNameRgb": "#005EB8",
                    "mediaType": None,
                    "mediaUrl": "NULL",
                    "positionType": "Robot",
                    "tabItemActionUrl": None,
                },
                {
                    "bgImgUrl": None,
                    "defaultImgUrl": url_store_1,
                    "iconId": "20231013052048_2220e360740e862d81557f107b13cfd8",
                    "iconName": "Store",
                    "iconType": "MALL",
                    "lightImgUrl": url_store_2,
                    "lightNameRgb": "#005EB8",
                    "mediaType": None,
                    "mediaUrl": "NULL",
                    "positionType": "Store",
                    "tabItemActionUrl": None,
                },
                {
                    "bgImgUrl": None,
                    "defaultImgUrl": url_mine_1,
                    "iconId": "20231013052048_3d5316579f33f9f0982dcd0393f62722",
                    "iconName": "Mine",
                    "iconType": "MINE",
                    "lightImgUrl": url_mine_2,
                    "lightNameRgb": "#005EB8",
                    "mediaType": None,
                    "mediaUrl": "NULL",
                    "positionType": "Mine",
                    "tabItemActionUrl": None,
                },
            ],
        }
    )