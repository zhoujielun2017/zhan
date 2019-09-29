from const import const
from model.pagination import Pagination


# request 工具类
class RequestUtil:
    @staticmethod
    def get_pagination(request) -> Pagination:
        page = request.args.get("page")
        page_size = request.args.get("page_size")
        return Pagination(page, page_size)

    @staticmethod
    def get_user_id(session) -> str:
        user_id = session.get(const.SESSION_USER_ID)
        return user_id
