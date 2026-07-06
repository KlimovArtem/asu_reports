from pydantic import BaseModel, Field


class SignalsListSubdataSerializer(BaseModel):
    quantity: int
    di_module_type: str
    control: bool
    do_module_type: str
    measurements: bool
    ai_module_type: str


class SignalsListDataSerializer(BaseModel):
    system: str
    supplys: SignalsListSubdataSerializer
    feeders: SignalsListSubdataSerializer