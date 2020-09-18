from kakaowb.api.api_core import APISub, PRIVATE, GET
from datetime import datetime


class APICMDUser(APISub):
    cmd_map = {
        'users.find_by_phone_number':
            (PRIVATE, GET, 'users.find_by_phone_number'),
        'users.list':
            (PRIVATE, GET, 'users.list')
    }

    async def info(self, user_id: str):
        """
        워크스페이스에 속한 특정 멤버의 상세 정보를 얻습니다.

        requests
        user_id: 정보를 얻고자 하는 멤버의 ID

        response
        user: 멤버의 상세 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('users.info', args={'user_id': user_id})

        return rlt

    async def find_by_email(self, email: str):
        """
        이메일 주소를 이용하여 특정 워크스페이스에 가입한 멤버의 정보를 조회합니다.
        해당 API 호출 시, 다른 워크스페이스에 속한 멤버는 조회할 수 없습니다.
        이메일의 경우, 해당 멤버가 워크스페이스 가입 시 멤버 인증에 사용한 이메일 주소를
        사용해야 합니다. 프로필 정보에 부가정보로 등록된 이메일을 사용할 경우 멤버 조회가
        되지 않습니다.

        requests
        email: 찾고자 하는 멤버의 이메일 주소

        response
        user: 멤버의 상세 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('users.find_by_email', args={'email': email})

        return rlt

    async def find_by_phone_number(self, phone_number: str):
        """
        전화번호를 이용하여 특정 워크스페이스에 가입한 멤버의 정보를 조회합니다. 해당 API 호출 시, 다른 워크스페이스에 속한 멤버는 찾을 수 없습니다.
전화번호의 경우, 해당 멤버가 워크스페이스 가입 시에 멤버 인증으로 사용된 전화번호 정보를 사용해야 합니다. 프로필에 부가 정보로 등록된 전화번호 사용 시, API 호출이 제대로 동작하지 않을 수 있습니다.

        requests
        phone_number: 찾고자하는 멤버의 전화번호

        response
        user: 멤버의 상세 정보   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('users.find_by_phone_number', args={'phone_number': phone_number})

        return rlt

    async def find_by_phone_number(self, phone_number):
        rlt = await self.__call__('users.find_by_phone_number', args={'phone_number': phone_number})

        return rlt

    async def list(self, limit: str, cursor: str):
        """
        특정 워크스페이스에 속한 전체 멤버의 목록과 각각의 멤버에 대한 상세 정보를 조회합니다.

        requests
        limit: 한 번에 가져올 수 있는 데이터 개수
        cursor: 다음 API 호출 시에 사용할 페이징 커서(Cursor)

        response
        users: 멤버의 상세 정보   - API 호출 성공(true)일 경우 제공
        cursor: 다음 API 호출시에 쓰일 페이징 커서(Cursor)   - API 호출 성공(true)일 경우 제공
        """
        rlt = await self.__call__('users.list', args={'limit': limit, 'cursor': cursor})

        return rlt

    async def set_work_time(self, user_id: str, work_start_time: datetime, work_end_time: datetime):
        """
        특정 멤버의 근무시간을 갱신합니다.

        requests
        user_id: 근무 시간을 변경하고자 하는 멤버의 ID
        work_start_time: 근무 시작 시간(Unix time 값)
        work_end_time: 근무 종료 시간(Unix time 값)

        response

        """
        rlt = await self.__call__('users.set_work_time', args={'user_id': user_id, 'work_start_time': work_start_time,
                                                               'work_end_time': work_end_time})

        return rlt

    async def set_vacation_time(self, user_id: str, vacation_start_time: datetime, vacation_end_time: datetime):
        """
        특정 멤버의 휴가 시간을 갱신합니다.

        requests
        user_id: 휴가 시간을 변경하고자 하는 멤버의 ID
        vacation_start_time: 휴가 시작 시간(Unix Time 값)
        vacation_end_time: 휴가 종료 시간(Unix Time 값)

        response

        """
        rlt = await self.__call__('users.set_vacation_time',
                                  args={'user_id': user_id, 'vacation_start_time': vacation_start_time,
                                        'vacation_end_time': vacation_end_time})

        return rlt
