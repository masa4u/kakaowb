from typing import List

from kakaowb.api.api_core import APISub, PRIVATE, POST
from kakaowb.api.sub.data import Message

part = 'messages'


class APICMDMessages(APISub):
    cmd_map = {
        f'{part}.send':
            (PRIVATE, POST, f'{part}.send'),
    }

    async def send(self, conversation_id: str, text: str, blocks: List = []) -> Message:
        """
        지정된 채팅방에 새로운 메시지를 전송합니다.

        $ curl -X POST https://api.kakaowork.com/v1/messages.send \
        -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}" \
        -H "Content-Type: application/json" \
        -d '{ "conversation_id": "{메시지를 보낼 채팅방 ID}", "text": "Hello" }'

        :param user_id:
        :return: Conversations
        """
        rlt = await self.__call__(f'{part}.send',
                                  args={'conversation_id': conversation_id, 'text': text, 'blocks': blocks})

        return Message(**rlt)
