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

    async def open(self, user_id: str) -> Conversations:
        """
        채팅방 생성

        :param user_id:
        :return: Conversations
        """
        rlt = await self.__call__(f'{part}.open', args={'user_id': user_id})

        return Conversations(**rlt)
