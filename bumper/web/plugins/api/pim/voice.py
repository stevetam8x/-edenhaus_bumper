"""Voice plugin module."""
# import logging
from collections.abc import Iterable

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import AbstractRouteDef

from bumper.web.plugins import WebserverPlugin
from bumper.web.response_utils import response_success_v3


class VoicePlugin(WebserverPlugin):
    """Voice plugin."""

    @property
    def routes(self) -> Iterable[AbstractRouteDef]:
        """Plugin routes."""
        return [
            web.route(
                "*",
                "/voice/get",
                _handle_get,
            ),
            web.route(
                "*",
                "/voice/getLanuages",
                _handle_get_lanuages,
            ),
        ]


async def _handle_get(request: Request) -> Response:
    """Get voice."""
    voice_lang = request.query.get("voiceLang", "EN").lower()
    language_name: str | list[str] = "English"
    for voice in _get_voice_list():
        if voice.get("voiceLang") == voice_lang:
            language_name = voice.get("languageName", "English")
            break

    return response_success_v3(
        [
            {
                "advertisementPhotoUrl": "",
                "desc": "",
                "downloadTimes": 65,
                "iconUrl": "https://portal-ww.ecouser.net/api/pim/file/get/61a8912cd302838d8898df9b",
                "id": "default",
                "isDefault": True,
                "languageName": language_name,
                "name": language_name,
                "needActive": False,
                "sampleVoiceUrl": "https://portal-ww.ecouser.net/api/pim/file/get/61a8913a72e305f1cac11617",
                "sort": 401,
                "status": "valid",
                "support": ["yiko"],
                "tag": "",
                "voice": "65279265545c5fc089782ab8",  # pragma: allowlist secret
                "voiceLang": voice_lang,
                "voiceMd5": "27a816e229a0e0471703a244a7763f09",  # pragma: allowlist secret
                "voiceSize": 3823807,
                "voiceUrl": "https://portal-ww.ecouser.net/api/pim/voice/download/61a89146d30283475c98df9d",
            }
        ],
        data_key="voices",
    )


async def _handle_get_lanuages(_: Request) -> Response:
    """Get languages."""
    return response_success_v3(_get_voice_list(), data_key="voices")


def _get_voice_list() -> list[dict[str, str | list[str]]]:
    return [
        {"languageName": "English", "support": ["yiko"], "voiceLang": "en"},
        {"languageName": "English(Australian)", "support": ["yiko"], "voiceLang": "en-au"},
        {"languageName": "English(Canadian)", "support": ["yiko"], "voiceLang": "en-ca"},
        {"languageName": "English(United Kingdom)", "support": ["yiko"], "voiceLang": "en-gb"},
        {"languageName": "English(Indian)", "support": ["yiko"], "voiceLang": "en-in"},
        {"languageName": "English(American)", "support": ["yiko"], "voiceLang": "en-us"},
        {"languageName": "한국어", "support": ["yiko"], "voiceLang": "ko"},
        {"languageName": "日本語", "support": ["yiko"], "voiceLang": "ja"},
        {"languageName": "Le français", "support": ["yiko"], "voiceLang": "fr"},
        {"languageName": "國語", "support": ["yiko"], "voiceLang": "tw"},
        {"languageName": "Deutsch", "support": ["yiko"], "voiceLang": "de"},
        {"languageName": "Italiano", "support": ["yiko"], "voiceLang": "it"},
        {"languageName": "Indonesia", "support": ["yiko"], "voiceLang": "id"},
    ]
