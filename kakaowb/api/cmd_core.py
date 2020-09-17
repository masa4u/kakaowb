# -*- coding: utf-8 -*-

import base64
import json

from kakaowb.api.api_core import APICore, APIConfig
from kakaowb.api.sub import APICMDUser, APICMDConversations, APICMDMessages

version = 'v1'


class APICMDCore(APICore):
    base_url = f'https://api.kakaowork.com/{version}/'

    def __init__(self, client, config):
        APICore.__init__(self, client, config)

        # user
        self.user = APICMDUser(self.__call__)
        self.conversations = APICMDConversations(self.__call__)
        self.messages = APICMDMessages(self.__call__)

        self.cmd_map = {}
        self.cmd_map.update(self.user.cmd_map)
        self.cmd_map.update(self.conversations.cmd_map)
        self.cmd_map.update(self.messages.cmd_map)

    def gen_postdata(self, data={}):
        payload = {}
        payload.update(data)
        payload['Bearer'] = self.access_token

        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(dumped_json.encode('ascii'))
        return json.dumps(encoded_json.decode())

    async def get_headers(self, payload):
        header = {
            'Content-type': 'application/json;charset=utf-8',
            'Authorization': f'Bearer {self.access_token}',
        }
        return header


if __name__ == '__main__':
    import aiohttp
    import asyncio
    import logging
    from kakaowb.common.log import DEFAULT_FORMAT

    logging.basicConfig(level=logging.DEBUG, format=DEFAULT_FORMAT)

    config = APIConfig('ddddd', False, False)


    async def get_test():
        async with aiohttp.ClientSession() as client:
            api = APICMDCore(client, config)
            print(await api.user.list())
            # print(await api.user.find_by_phone_number('010'))
            # print((await api.find_by_phone_number('01099433536')))
            # print((await api.user_list()))


    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_test())
