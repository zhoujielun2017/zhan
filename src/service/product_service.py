import shortuuid
from mongoengine import DoesNotExist, ValidationError

from model.pagination import Pagination
from model.product import Product
from model.product_save import ProductSave


def all():
    users = Product.objects()
    for user in users:
        print(user.mobile)


def page(page: Pagination):
    users = Product.objects.paginate_field(page.page,
                                           page.page_size)
    return users


def find_by_id(id: str) -> Product:
    try:
        return Product.objects.get(pk=id)
    except DoesNotExist:
        print("does not exist")
        return None
    except ValidationError:
        print("id length is wrong")
        return None


def find_by_code(code: str) -> Product:
    try:
        return Product.objects.get(code=code)
    except DoesNotExist:
        return None


def update(save: ProductSave) -> Product:
    p = find_by_id(save.id)
    dd = save.to_update()
    p.update(**dd)



def save(save: ProductSave) -> Product:
    p = Product()
    p.code = shortuuid.uuid()
    p.title = save.title
    p.content = save.content
    p.price = save.price
    p.main_pic = save.main_pic
    p.pics = save.pics
    p.view_count = 0
    p.stock = 0
    return p.save()
