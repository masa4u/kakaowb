# -*- cofing: utf-8 -*-
import asyncio
from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlencode, urljoin

from aiohttp.client import ClientSession

from kakaowb.api.coach import Coach
from kakaowb.api.httputil import fetch, fetch_post
from kakaowb.common.log import logger
from kakaowb.common.exceptions import error_code_map


class APIType(Enum):
    PUBLIC = 0
    PRIVATE = 1


class APICallType(Enum):
    GET = 0
    POST = 1


@dataclass
class APICommand:
    api_type: APIType
    call_type: APICallType
    url: str


class APIContentsType(Enum):
    json = 'application/json'


@dataclass
class APIConfig:
    access_token: str
    public_coach: bool
    private_coach: bool


PUBLIC = APIType.PUBLIC
PRIVATE = APIType.PRIVATE

GET = APICallType.GET
POST = APICallType.POST


class APICore(object):
    base_url = None
    cmd_map = {
        # 'temp': (APICallType.PRIVATE, 'temp')
    }

    # @property
    # def secret_key(self) -> str:
    #     return self._secret_key

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def client(self) -> ClientSession:
        return self._client

    def __init__(self, client: ClientSession, config):

        self._client = client
        self._access_token = config.access_token
        # self._secret_key = config.secret_key
        # self._nonce = int(time.time() * 1000)

        self.private_coach = None
        self.public_coach = None

        if config.private_coach is True:
            self.private_coach = Coach(config.private_call_frame, config.private_call_limit)
        if config.public_coach is True:
            self.public_coach = Coach(config.public_call_frame, config.public_call_limit)

    # @property
    # def nonce(self):
    #     self._nonce = self._nonce + 41
    #     return self._nonce

    async def __call__(self, cmd, args={}, cmd_map_args={}):
        cmd_type, call_type, _ = self.cmd_map[cmd]

        payload = {
            'cmd': cmd,
            'args': args,
            'cmd_map_args': cmd_map_args,
            'headers': {}
        }
        if cmd_type == APIType.PRIVATE:
            payload['headers'] = await self.get_headers(payload)
        if call_type == POST:
            ret = await asyncio.wait_for(self.call_http_post(**payload), 3)
        else:
            ret = await asyncio.wait_for(self.call_http_get(**payload), 3)

        if not ret['success']:
            code = ret['error']['code']
            msg = ret['error']['message']
            ex_func, _ = error_code_map[code]
            raise ex_func(msg)

        logger.debug('payload=%s' % str(payload))
        logger.debug('rlt=%s' % str(ret))

        return ret

    async def get_headers(self, payload):
        raise Exception('Not imp')

    def get_url(self, cmd, args={}, cmd_map_args={}):
        url = urljoin(self.base_url, self.cmd_map[cmd][2].format(**cmd_map_args))
        if args != {}:
            url = url + '?' + urlencode(args)
        return url

    async def call_http_post(self, cmd: str, args: dict, cmd_map_args: dict, headers: {}):
        url = self.get_url(cmd, cmd_map_args=cmd_map_args)
        if self.private_coach:
            self.private_coach.wait()
        rlt = await fetch_post(self.client, url, args, headers)

        return rlt

    async def call_http_get(self, cmd: str, args: dict, cmd_map_args: dict, headers: dict):
        url = self.get_url(cmd, args, cmd_map_args)

        if self.public_coach:
            self.public_coach.wait()
        rlt = await fetch(self.client, url, headers)
        logger.debug(url)

        return rlt


class APISub(object):
    def __init__(self, call):
        self.__call__ = call
