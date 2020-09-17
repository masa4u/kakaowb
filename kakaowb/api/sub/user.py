from kakaowb.api.api_core import APISub, PRIVATE, GET


class APICMDUser(APISub):
    cmd_map = {
        'users.find_by_phone_number':
            (PRIVATE, GET, 'users.find_by_phone_number'),
        'users.list':
            (PRIVATE, GET, 'users.list')
    }

    async def find_by_phone_number(self, phone_number):
        rlt = await self.__call__('users.find_by_phone_number', args={'phone_number': phone_number})

        return rlt

    async def list(self):
        return await self.__call__('users.list')
