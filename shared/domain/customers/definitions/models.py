from pydantic import BaseModel
from uuid import UUID


class Customer(BaseModel):
    uuid: UUID
    name: str
    display_name: str
    client_id: str
