from pydantic import BaseModel, Field


class SignalsListSubdataSerializer(BaseModel):
    quantity: int = 0
    di_module_type: str = ""
    control: bool = False
    do_module_type: str= ""
    measurements: bool = False
    ai_module_type: str = ""


class SignalsListDataSerializer(BaseModel):
    system: str
    supplys: SignalsListSubdataSerializer
    feeders: SignalsListSubdataSerializer