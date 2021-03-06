from ma import ma
from models.store import StoreModel
from schemas.item import ItemSchema
from models.item import ItemModel

class StoreSchema(ma.ModelSchema):
    items = ma.Nested(ItemSchema, many=True)
    class Meta:
        model = StoreModel
        dump_only = ("id",)
        include_fk = True

