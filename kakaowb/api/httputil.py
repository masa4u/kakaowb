from aiohttp.client import ClientSession
from kakaowb.common import exceptions
from kakaowb.common.log import logger

OK_STATUS_CODE = 200


async def fetch(client: ClientSession, url: str, headers=dict(), read_response_func='json'):
    async with client.get(url, headers=headers) as resp:
        if resp.status != OK_STATUS_CODE:
            msg = 'Error getting data for url {0}, status_code: {1}'.format(url, resp.status)
            if resp.status == 429:
                raise exceptions.HTTPTooManyRequestException(msg)
            elif resp.status == 521:
                raise exceptions.HTTPServerDown(msg)
            raise Exception(msg)
        return await getattr(resp, read_response_func)()


async def fetch_post(client: ClientSession, url: str, payload='', headers: dict = dict(),
                     read_response_func='json'):
    async with client.post(url, data=payload, headers=headers) as resp:
        if resp.status != OK_STATUS_CODE:
            msg = 'Error getting data for url {0}, status_code: {1}'.format(url, resp.status)
            if resp.status == 429:
                raise exceptions.HTTPTooManyRequestException
            rlt = await getattr(resp, read_response_func)()
            logger.error(rlt)
            raise Exception(msg)
        return await getattr(resp, read_response_func)()
