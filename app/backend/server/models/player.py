from typing import Optional

from pydantic import BaseModel, Field


class PlayerSchema(BaseModel):
    Team: str = Field(...)
    Number: str = Field(..., alias="#")
    Name: str = Field(...)
    Yr: str = Field(...)
    Pos: str = Field(...)
    Matches: str = Field(..., alias="m")
    Sets: str = Field(..., alias="s")
    Kills: str = Field(..., alias="k")
    KillsPerSet: str = Field(..., alias="k/s")
    Errors: str = Field(..., alias="e")
    Attempts: str = Field(..., alias="ta")
    Percentage: str = Field(..., alias="pct")
    Assists: str = Field(..., alias="a")
    AssistsPerSet: str = Field(..., alias="a/s")
    ServiceAces: str = Field(..., alias="sa")
    ServiceAcesPerSet: str = Field(..., alias="sa/s")
    Receptions: str = Field(..., alias="r")
    Digs: str = Field(..., alias="digs")
    DigsPerSet: str = Field(..., alias="d/s")
    BlockSolo: str = Field(..., alias="bs")
    BlockAssists: str = Field(..., alias="ba")
    BlockTotal: str = Field(..., alias="tot")
    BlocksPerSet: str = Field(..., alias="b/s")
    Points: str = Field(..., alias="pts")
    PointsPerSet: str = Field(..., alias="pts/s")

    class Config:
        schema_extra = {
            "example": {
                "_id":{
                    "$oid":"64f22e4d4e56a84650f5fa21"
                },
                "Team":"Metropolis",
                "#":"1",
                "Name":"John Doe",
                "Yr":"Jr",
                "Pos":"S",
                "m":"15",
                "s":"25",
                "k":"10",
                "k/s":"0.40",
                "e":"8",
                "ta":"50",
                "pct":"0.04",
                "a":"5",
                "a/s":"0.20",
                "sa":"1",
                "sa/s":"0.04",
                "r":"9",
                "re":"3",
                "digs":"7",
                "d/s":"0.37",
                "bs":"0",
                "ba":"0",
                "tot":"0",
                "b/s":"0.00",
                "pts":"0.0",
                "pts/s":"0.0"
            }
        }


class UpdatePlayerModel(BaseModel):
    Team: str = Optional[str]
    Number: str = Optional[str]
    Name: str = Optional[str]
    Yr: str = Optional[str]
    Pos: str = Optional[str]
    Matches: str = Optional[str]
    Sets: str = Optional[str]
    Kills: str = Optional[str]
    KillsPerSet: str = Optional[str]
    Errors: str = Optional[str]
    Attempts: str = Optional[str]
    Percentage: str = Optional[str]
    Assists: str = Optional[str]
    AssistsPerSet: str = Optional[str]
    ServiceAces: str = Optional[str]
    ServiceAcesPerSet: str = Optional[str]
    Receptions: str = Optional[str]
    Digs: str = Optional[str]
    DigsPerSet: Optional[str]
    BlockSolo: Optional[str]
    BlockAssists: Optional[str]
    BlockTotal: Optional[str]
    BlocksPerSet: Optional[str]
    Points: Optional[str]
    PointsPerSet: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id":{
                    "$oid":"64f22e4d4e56a84650f5fa21"
                },
                "Team":"Metropolis",
                "#":"1",
                "Name":"John Doe",
                "Yr":"Jr",
                "Pos":"S",
                "m":"15",
                "s":"25",
                "k":"10",
                "k/s":"0.40",
                "e":"8",
                "ta":"50",
                "pct":"0.04",
                "a":"5",
                "a/s":"0.20",
                "sa":"1",
                "sa/s":"0.04",
                "r":"9",
                "re":"3",
                "digs":"7",
                "d/s":"0.37",
                "bs":"0",
                "ba":"0",
                "tot":"0",
                "b/s":"0.00",
                "pts":"0.0",
                "pts/s":"0.0"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
