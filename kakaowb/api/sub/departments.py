from typing import List

from kakaowb.api.api_core import APISub, PRIVATE, POST
from kakaowb.api.sub.data import Message, Department

part = 'departments'


class APICMDDepartments(APISub):
    cmd_map = {
        f'{part}.list':
            (PRIVATE, POST, f'{part}.list'),
    }

    async def list(self) -> List[Department]:
        """
        워크스페이스에 속한 전체 부서 정보를 조회합니다.

        response
        departments: 부서의 상세 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('departments.list', args={})

        return [Department(**x) for x in rlt]
