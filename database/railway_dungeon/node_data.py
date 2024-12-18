from pydantic import BaseModel
from typing import List, Optional
from database.client import db
from limbus.formats import (
    RailwayNodeDataFormat,
    RailwayEGOStockFormat,
    RailwayUnitStatusFormat,
    RailwayStatisticsDataFormat,
    SaveDataForRailwayDungeon,
)

railway_node_collection = db["railway_node_data"]

class RailwayNodeDataFormatWithUID(BaseModel):
    uid: int
    nodeid: int
    egostocks: List[RailwayEGOStockFormat] = []
    status: List[RailwayUnitStatusFormat] = []
    clearturn: int
    playturn: int
    statistics: List[RailwayStatisticsDataFormat] = []
    enemy: SaveDataForRailwayDungeon
    nodestate: int


def insert_railway_node_data(uid: int) -> None:
    try:
        node_data_format = RailwayNodeDataFormat()

        node_data_with_uid = RailwayNodeDataFormatWithUID(
            uid=uid,
            nodeid=node_data_format.nodeid,
            egostocks=node_data_format.egostocks,
            status=node_data_format.status,
            clearturn=node_data_format.clearturn,
            playturn=node_data_format.playturn,
            statistics=node_data_format.statistics,
            enemy=node_data_format.enemy,
            nodestate=node_data_format.nodestate,
        )

        railway_node_collection.insert_one(node_data_with_uid.dict())
    except Exception as e:
        print("WARN:     " + str(e))


def get_railway_node_data(
    uid: int, nodeid: int
) -> Optional[RailwayNodeDataFormat]:
    try:
        doc = railway_node_collection.find_one({"uid": uid, "nodeid": nodeid})

        if doc:
            return RailwayNodeDataFormat(
                nodeid=doc["nodeid"],
                egostocks=doc["egostocks"],
                status=doc["status"],
                clearturn=doc["clearturn"],
                playturn=doc["playturn"],
                statistics=doc["statistics"],
                enemy=doc["enemy"],
                nodestate=doc["nodestate"],
            )

        return None

    except Exception as e:
        print(f"WARN:     {str(e)}")
        return None


def update_railway_node_data(
    uid: int,
    nodeid: int,
    egostocks: Optional[List[RailwayEGOStockFormat]] = None,
    status: Optional[List[RailwayUnitStatusFormat]] = None,
    clearturn: Optional[int] = None,
    playturn: Optional[int] = None,
    statistics: Optional[List[RailwayStatisticsDataFormat]] = None,
    enemy: Optional[SaveDataForRailwayDungeon] = None,
    nodestate: Optional[int] = None,
) -> bool:
    try:
        update_fields = {}
        if egostocks is not None:
            update_fields["egostocks"] = [es.dict() for es in egostocks]
        if status is not None:
            update_fields["status"] = [s.dict() for s in status]
        if clearturn is not None:
            update_fields["clearturn"] = clearturn
        if playturn is not None:
            update_fields["playturn"] = playturn
        if statistics is not None:
            update_fields["statistics"] = [st.dict() for st in statistics]
        if enemy is not None:
            update_fields["enemy"] = enemy.dict()
        if nodestate is not None:
            update_fields["nodestate"] = nodestate

        if update_fields:
            railway_node_collection.update_one(
                {"uid": uid, "nodeid": nodeid}, {"$set": update_fields}
            )
            return True

        return True

    except Exception as e:
        print(f"WARN:     {str(e)}")
        return False
