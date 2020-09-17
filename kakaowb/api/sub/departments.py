from typing import List

from kakaowb.api.api_core import APISub, PRIVATE, POST
from kakaowb.api.sub.data import Message, Department

part = 'departments'


class APICMDDepartments(APISub):
    cmd_map = {
        f'{part}.list':
            (PRIVATE, POST, f'{part}.list'),
    }

    async def list(self, conversation_id: str, text: str, blocks: List = []) -> List[Department]:
        """
        워크스페이스에 속한 전체 부서 정보를 조회합니다.

        $ curl https://api.kakaowork.com/v1/departments.list \
       -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}" \
       -H "Content-Type: application/json;charset=utf-8"

        :param conversation_id
        :param text
        :params blocks
        :return: List[Department]
        """
        rlt = await self.__call__(f'{part}.send',
                                  args={'conversation_id': conversation_id, 'text': text, 'blocks': blocks})

        return [Department(**x) for x in rlt]
