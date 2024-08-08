from app.core.schema import BaseSchema


class GetLocationLocationClientDTO(BaseSchema):
    apikey: str
    q: str
    language: str = "en-us"
    details: bool = False
    toplevel: bool = False
