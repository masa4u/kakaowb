from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class User:
    id: str
    space_id: str
    name: str

    # 여기부터 optional
    nickname: str
    avatar_url: str
    department: str
    position: str
    responsibility: str
    work_start_time: datetime
    work_end_time: datetime
    vacation_end_time: datetime


@dataclass
class Message:
    id: str
    text: str
    user_id: str
    conversation_id: str
    send_time: datetime
    update_time: datetime
    blocks: List  # Optional


@dataclass
class Action:
    pass


@dataclass
class Member:
    id: str
    name: str
    user_count: int


@dataclass
class Department:
    id: str
    space_id: str
    name: str
    code: str
    user_count: int
    # 여기부터 optional
    ancestor: List[Member]
    children: List[Member]
    has_child: bool
    depth: int
    user_ids: List[int]
    leader_ids: List[int]
