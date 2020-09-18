from typing import List

from kakaowb.api.api_core import APISub, PRIVATE, POST
from kakaowb.api.sub.data import Message

part = 'messages'


class APICMDMessages(APISub):
    cmd_map = {
        f'{part}.send':
            (PRIVATE, POST, f'{part}.send'),
    }

    async def send(self, conversation_id: str, text: str, blocks: List):
        """
        지정된 채팅방에 새로운 메시지를 전송합니다.

        requests
        conversation_id: 메시지를 전송하고자 하는 채팅방의 ID
        text: 채팅 메시지
          - 일반 텍스트 메시지를 전달할 때 사용
          - 메시지를 text 형식이 아닌 blocks로 정의했을 때, 푸시알림과 채팅방 목록과 같이 조합형 말풍선 메시지가 사용될 수 없는 경우에 활용되는 대체(Fallback) 메시지
        blocks: 조합형 말풍선 메시지를 전달할 때 사용   - Block Kit 구성 및 정책 참고

        response
        message: 전송된 메시지 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('messages.send',
                                  args={'conversation_id': conversation_id,
                                        'text': text,
                                        'blocks': blocks})

        return Message(**rlt)
