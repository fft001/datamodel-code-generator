# generated by datamodel-codegen:
#   filename:  subfolder/type-5.json
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from pydantic import BaseModel, Field
from typing_extensions import Literal


class Type5(BaseModel):
    type_: Literal['e'] = Field(..., const=True, title='Type ')
