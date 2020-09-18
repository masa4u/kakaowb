"""
# Model

반응형 대화를 진행할 때, 특정 액션이 지정된 버튼을 통해 멤버의 의견을 입력받고,
대화를 이어나갈 때 다음과 같은 API를 사용합니다. 다음의 API를 사용하여 Modal 화면을
구성하는 정보와 멤버의 입력 정보를 전달받을 수 있습니다. Modal을 사용하기 위해서는
Block Kit을 사용하여 조합형 말풍선을 구성할 때, Button Block의 action_type을
call_modal로 설정해야 합니다.
"""
from kakaowb.api.api_core import APISub, PRIVATE, POST
from kakaowb.api.sub.data import Message, Action

part = 'modal'


class APICMDModal(APISub):
    cmd_map = {
        f'{part}.request_modal': (PRIVATE, POST, f'{part}.request_modal'),
        f'{part}.response_modal': (PRIVATE, POST, f'{part}.response_modal'),
    }

    async def request_modal(self, type: str, value: str, action_time: str, message: Message):
        """
        3rd Party 서버에 Modal 화면을 구성하는 JSON 정보를 요청합니다.

        requests
        type: “request_modal"로 고정
        value: Bot 메시지의 Button Block에 설정한 Value 값
        action_time: 요청 액션이 발생한 카카오워크 서버의 시간 정보
        message: 액션이 발생한 채팅 메시지 원본

        response
        view: Modal 화면을 그리는데 필요한 JSON 데이터
        """
        rlt = await self.__call__('modal.request_modal',
                                  args={'type': type, 'value': value, 'action_time': action_time, 'message': message})

        return rlt

    async def submit_modal(self, type: str, action_time: str, actions: Action, message: Message):
        """
        Modal에서 사용자가 입력한 입력 정보를 모아 3rd Party에게 최종 전달합니다.

        requests
        type: “submission"으로 고정됨
        action_time: 요청 액션이 발생한 카카오워크 서버의 시간 값
        actions: Modal 화면에 사용자가 입력한 정보
        message: 액션이 발생된 채팅 메시지 원본

        response
        body: “submission” 수행에 대한 결과 값
        """
        rlt = await self.__call__('modal.submit_modal',
                                  args={'type': type, 'action_time': action_time, 'actions': actions,
                                        'message': message})

        return rlt
