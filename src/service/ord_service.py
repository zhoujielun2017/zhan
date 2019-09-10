from model.ord import Ord
from model.ord_area import OrdArea
from model.ord_product import OrdProduct
from model.ord_save import OrdSave


def all():
    return Ord.objects()


def save(dto: OrdSave):
    ord = Ord()
    Ord.save(ord)
    ord.user_id = dto.user_id
    for pro in dto.pros:
        ord_pro = OrdProduct()
        ord_pro.ord_id = str(ord.id)
        ord_pro.productid = pro.split("_")[0]
        ord_pro.num = pro.split("_")[1]
        OrdProduct.save(ord_pro)
    ord_area = OrdArea()
    ord_area.ord_id = str(ord.id)
    if len(dto.areas) > 0:
        ord_area.area1_id = dto.areas[0].split("_")[0]
        ord_area.area1_name = dto.areas[0].split("_")[1]
    if len(dto.areas) > 1:
        ord_area.area2_id = dto.areas[1].split("_")[0]
        ord_area.area2_name = dto.areas[1].split("_")[1]
    if len(dto.areas) > 2:
        ord_area.area3_id = dto.areas[2].split("_")[0]
        ord_area.area3_name = dto.areas[2].split("_")[1]
    OrdArea.save(ord_area)
    return str(ord.id)
