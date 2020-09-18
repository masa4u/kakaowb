from dataclasses import dataclass
from kakaowb.api.api_core import APISub, PRIVATE, GET, POST

part = 'conversations'


@dataclass
class Conversations:
    pass


class APICMDConversations(APISub):
    cmd_map = {
        f'{part}.open':
            (PRIVATE, POST, f'{part}.open'),
    }

    async def open(self, user_id: str):
        """
        Bot과 멤버 간 1:1 채팅방을 생성합니다. 이미 채팅방이 개설되어 있는 경우, 채팅방을 새로 시작하지 않고 해당 채팅방 정보를 반환합니다.

        requests
        user_id: 멤버 ID

        response
        conversation: 개설된 채팅방 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('conversations.open', args={'user_id': user_id})

        return rlt
