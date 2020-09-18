from kakaowb.api.api_core import APISub, PRIVATE, GET


class APICMDSpace(APISub):
    cmd_map = {
        'spaces.info':
            (PRIVATE, GET, 'spaces.info'),
    }

    async def info(self):
        """
        워크스페이의 정보를 조회합니다.

        response
        space: 부서의 상세 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('spaces.info', args={})

        return rlt
