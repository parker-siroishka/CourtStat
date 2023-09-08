from typing import Optional, List, Dict

from pydantic import BaseModel, Field


class StatisticsModel(BaseModel):
    currentTotal: float  # Current total for the statistic
    historical: List[float]  # List of historical values

class PlayerSchema(BaseModel):
    Team: str = Field(...)
    Number: str = Field(..., alias="#")
    Name: str = Field(...)
    Yr: str = Field(...)
    Pos: str = Field(...)
    Statistics: Dict[str, StatisticsModel]  # Use a dictionary to store the statistics

    class Config:
        json_schema_extra = {
            "example": {
                "_id":{
                    "$oid":"64f22e4d4e56a84650f5fa21"
                },
                "Team":"Metropolis",
                "#":"1",
                "Name":"John Doe",
                "Yr":"Jr",
                "Pos":"S",
                "Statistics": {
                    "m": {
                        "currentTotal": 15,
                        "historical": [15, 14, 16]
                    },
                    "s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "k": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "k/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "e": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "ta": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pct": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "a": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "a/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "sa": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "sa/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "r": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "re": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "digs": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "d/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "bs": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "ba": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "tot": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "b/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pts": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pts/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                }
            }
        }


class UpdatePlayerModel(BaseModel):
    Team: Optional[str]
    Number: Optional[str]
    Name: Optional[str]
    Yr: Optional[str]
    Pos: Optional[str]
    Statistics: Dict[str, StatisticsModel]  # Use a dictionary to store the statistics

    class Config:
        json_schema_extra = {
            "example": {
                "_id":{
                    "$oid":"64f22e4d4e56a84650f5fa21"
                },
                "Team":"Metropolis",
                "#":"1",
                "Name":"John Doe",
                "Yr":"Jr",
                "Pos":"S",
                "Statistics": {
                    "m": {
                        "currentTotal": 15,
                        "historical": [15, 14, 16]
                    },
                    "s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "k": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "k/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "e": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "ta": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pct": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "a": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "a/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "sa": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "sa/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "r": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "re": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "digs": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "d/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "bs": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "ba": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "tot": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "b/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pts": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                    "pts/s": {
                        "currentTotal": 25,
                        "historical": [25, 24, 26]
                    },
                }
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
