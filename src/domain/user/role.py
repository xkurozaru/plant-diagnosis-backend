import dataclasses

from src.domain.user import permission, role_type


@dataclasses.dataclass
class Role:
    __type: role_type.RoleType
    __permissions: list[permission.Permission]

    def __init__(self, type: role_type.RoleType, permissions: list[permission.Permission]) -> None:
        self.__type = type
        self.__permissions = permissions

    @property
    def type(self) -> role_type.RoleType:
        return self.__type

    @property
    def permissions(self) -> list[permission.Permission]:
        return self.__permissions


def new_admin_role() -> "Role":
    return Role(
        role_type.RoleType.ADMIN,
        [permission.Permission.READ_MODEL, permission.Permission.WRITE_MODEL, permission.Permission.DELETE_MODEL],
    )


def new_member_role() -> "Role":
    return Role(role_type.RoleType.MEMBER, [permission.Permission.READ_MODEL])


def recreate_role(type: str) -> "Role":
    if type == role_type.RoleType.ADMIN.value:
        return new_admin_role()
    elif type == role_type.RoleType.MEMBER.value:
        return new_member_role()
    else:
        raise Exception(f"Invalid role type {type}")
