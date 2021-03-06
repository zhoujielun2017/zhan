import logging

from mongoengine import ValidationError, DoesNotExist

from model.ord import Ord
from model.ord_area import OrdArea
from model.ord_gift_card import OrdGiftCard
from model.ord_product import OrdProduct
from model.ord_save import OrdSave
from model.pagination import Pagination


def all():
    return Ord.objects()


def find_by_id(id: str):
    try:
        o = Ord.objects.get(pk=id)
        products = OrdProduct.objects(ord_id=id)
        area = OrdArea.objects(ord_id=id).first()
        gift_card = OrdGiftCard.objects(ord_id=id).first()
        return {"ord": o, "products": products,
                "area": area,
                "gift_card": gift_card}
    except DoesNotExist:
        logging.error("does not exist %s" % id)
        return None
    except ValidationError:
        logging.error("id length is wrong %s" % id)
        return None


def save(dto: OrdSave):
    ord = Ord()
    ord.user_id = dto.user_id
    ord.status = dto.status
    ord.save()
    # 商品
    for pro in dto.pros:
        pro.ord_id = str(ord.id)
        pro.save()
    # 收货地址
    ord_area = OrdArea()
    ord_area.ord_id = str(ord.id)
    ord_area.name = str(dto.name)
    ord_area.mobile = str(dto.mobile)
    ord_area.address = str(dto.address)
    if len(dto.areas) > 0:
        ord_area.area1_id = dto.areas[0].split("_")[0]
        ord_area.area1_name = dto.areas[0].split("_")[1]
    if len(dto.areas) > 1:
        ord_area.area2_id = dto.areas[1].split("_")[0]
        ord_area.area2_name = dto.areas[1].split("_")[1]
    if len(dto.areas) > 2:
        ord_area.area3_id = dto.areas[2].split("_")[0]
        ord_area.area3_name = dto.areas[2].split("_")[1]
    ord_area.save()
    # 礼品卡
    gift = OrdGiftCard()
    gift.gift_card_code = dto.gift_card_code
    gift.gift_card_id = dto.gift_card_id
    gift.ord_id = str(ord.id)
    gift.save()
    return str(ord.id)


def page(page: Pagination, **kwargs):
    page_result = Ord.objects.paginate_field(page.page,
                                             page.page_size, **kwargs)
    page_obj = page_result.to_dict()
    list = []
    for ord in page_obj.get("list"):
        detail = find_by_id(ord.get("id"))
        ps = []
        for item in detail.get("products"):
            ps.append(item.to_dict())
        dict = {"ord": detail.get("ord").to_dict(), "products": ps,
                "area": None if not detail.get("area") else detail.get("area").to_dict(),
                "gift_card": None if not detail.get("gift_card") else detail.get(
                    "gift_card").to_dict()}
        list.append(dict)
    page_obj["list"] = list
    return page_obj


def delete(id: str):
    o = find_by_id(id)
    if o:
        o.get("ord").delete()
        for p in o.get("products"):
            p.delete()
        o.get("area").delete()
        o.get("gift_card").delete()
