"""Pim product plugin module."""
import json
import logging
import os
from collections.abc import Iterable

from aiohttp import web
from aiohttp.web_exceptions import HTTPInternalServerError
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import AbstractRouteDef

from bumper.utils import utils
from bumper.web import models
from bumper.web.plugins import WebserverPlugin

from . import get_product_iot_map

_LOGGER = logging.getLogger(__name__)


class ProductPlugin(WebserverPlugin):
    """Product plugin."""

    @property
    def routes(self) -> Iterable[AbstractRouteDef]:
        """Plugin routes."""
        return [
            web.route(
                "*",
                "/product/getProductIotMap",
                _handle_get_product_iot_map,
            ),
            web.route(
                "*",
                "/product/getConfignetAll",
                _handle_get_config_net_all,
            ),
            web.route(
                "*",
                "/product/getConfigGroups",
                _handle_get_config_groups,
            ),
            web.route(
                "POST",
                "/product/software/config/batch",
                _handle_config_batch,
            ),
        ]


async def _handle_get_product_iot_map(_: Request) -> Response:
    """Get product iot map."""
    try:
        return web.json_response(
            {
                "code": models.RETURN_API_SUCCESS,
                "data": get_product_iot_map(),
            }
        )
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError


async def _handle_get_config_net_all(_: Request) -> Response:
    """Get config net all."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "configNetAllResponse.json"), encoding="utf-8") as file:
            return web.json_response(json.load(file))
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError


async def _handle_get_config_groups(_: Request) -> Response:
    """Get config groups."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "configGroupsResponse.json"), encoding="utf-8") as file:
            return web.json_response(json.load(file))
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError


async def _handle_config_batch(request: Request) -> Response:
    """Handle product config batch."""
    try:
        with open(os.path.join(os.path.dirname(__file__), "productConfigBatch.json"), encoding="utf-8") as file:
            product_config_batch = json.load(file)

        json_body = json.loads(await request.text())
        data = []
        for pid in json_body.get("pids", []):
            for product_config in product_config_batch:
                if pid == product_config["pid"]:
                    data.append(product_config)
                    continue

            # not found in product_config_batch
            # some devices don't have any product configuration
            data.append({"cfg": {}, "pid": pid})

        return web.json_response({"code": 200, "data": data, "message": "success"})
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError
