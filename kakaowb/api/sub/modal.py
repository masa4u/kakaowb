"""
# Model

반응형 대화를 진행할 때, 특정 액션이 지정된 버튼을 통해 멤버의 의견을 입력받고,
대화를 이어나갈 때 다음과 같은 API를 사용합니다. 다음의 API를 사용하여 Modal 화면을
구성하는 정보와 멤버의 입력 정보를 전달받을 수 있습니다. Modal을 사용하기 위해서는
Block Kit을 사용하여 조합형 말풍선을 구성할 때, Button Block의 action_type을
call_modal로 설정해야 합니다.
"""
from dataclasses import dataclass
from typing import List
from kakaowb.api.api_core import APISub, PRIVATE, GET, POST
from kakaowb.api.sub.data import Message
from datetime import datetime

part = 'modal'


class APICMDModal(APISub):
    cmd_map = {
        f'{part}.send':
            (PRIVATE, POST, f'{part}.send'),
    }

    async def request_modal(self, type: str, value: str, action_time: str, message: Message)-> str:
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
