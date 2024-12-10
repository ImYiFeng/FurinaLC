from pydantic import BaseModel
from typing import List, Optional
from database.client import db
from resources.parser.railway_dungeon.railway_info import (
    # fetch_railway_info_list,
    create_railway_dungeon_save_info_format,
)
from limbus.formats import (
    RailwayDungeonSaveInfoFormat,
    RailwayUnitInfoFormat,
    RailwayExtraRewardStateFormat,
    RailwayBuffSetFormat,
    SaveDataForRailwayDungeon,
)

rd_save_collection = db["railway_dungeon_saves"]


class RailwayDungeonSaveInfoFormatWithUID(BaseModel):
    uid: int
    id: int
    prevclearnode: int
    currentnode: int
    lastclearnode: int
    personalities: List[RailwayUnitInfoFormat]
    payreward: int
    rewardstate: int
    extrarewardstate: List[RailwayExtraRewardStateFormat]
    firstcleardate: str
    currentclearrotation: int
    lastenternodeid: int
    lastclearrotation: int
    buffsets: List[RailwayBuffSetFormat]
    initseed: int
    currentseed: int
    enemySaveData: SaveDataForRailwayDungeon


def insert_railway_dungeon_save_info(uid: int) -> None:
    try:
        rd_save_format = create_railway_dungeon_save_info_format()

        rd_save_format_with_uid = RailwayDungeonSaveInfoFormatWithUID(
            uid=uid,
            id=rd_save_format.id,
            prevclearnode=rd_save_format.prevclearnode,
            currentnode=rd_save_format.currentnode,
            lastclearnode=rd_save_format.lastclearnode,
            personalities=rd_save_format.personalities,
            payreward=rd_save_format.payreward,
            rewardstate=rd_save_format.rewardstate,
            extrarewardstate=rd_save_format.extrarewardstate,
            firstcleardate=rd_save_format.firstcleardate,
            currentclearrotation=rd_save_format.currentclearrotation,
            lastenternodeid=rd_save_format.lastenternodeid,
            lastclearrotation=rd_save_format.lastclearrotation,
            buffsets=rd_save_format.buffsets,
            initseed=rd_save_format.initseed,
            currentseed=rd_save_format.currentseed,
            enemySaveData=rd_save_format.enemySaveData,
        )

        rd_save_collection.insert_one(rd_save_format_with_uid.dict())
    except Exception as e:
        print("WARN:     " + str(e))


def get_railway_dungeon_save_info(
    uid: int, dungeon_id: int
) -> Optional[RailwayDungeonSaveInfoFormat]:
    try:
        doc = rd_save_collection.find_one({"uid": uid, "id": dungeon_id})

        if doc:
            return RailwayDungeonSaveInfoFormat(
                id=doc["id"],
                prevclearnode=doc["prevclearnode"],
                currentnode=doc["currentnode"],
                lastclearnode=doc["lastclearnode"],
                personalities=doc["personalities"],
                payreward=doc["payreward"],
                rewardstate=doc["rewardstate"],
                extrarewardstate=doc["extrarewardstate"],
                firstcleardate=doc["firstcleardate"],
                currentclearrotation=doc["currentclearrotation"],
                lastenternodeid=doc["lastenternodeid"],
                lastclearrotation=doc["lastclearrotation"],
                buffsets=doc["buffsets"],
                initseed=doc["initseed"],
                currentseed=doc["currentseed"],
                enemySaveData=doc["enemySaveData"],
            )

        return None

    except Exception as e:
        print(f"WARN:     {str(e)}")
        return None


def update_railway_dungeon_save_info(
    uid: int,
    dungeon_id: int,
    prevclearnode: Optional[int] = None,
    currentnode: Optional[int] = None,
    lastclearnode: Optional[int] = None,
    personalities: Optional[List[RailwayUnitInfoFormat]] = None,
    payreward: Optional[int] = None,
    rewardstate: Optional[int] = None,
    extrarewardstate: Optional[List[RailwayExtraRewardStateFormat]] = None,
    firstcleardate: Optional[str] = None,
    currentclearrotation: Optional[int] = None,
    lastenternodeid: Optional[int] = None,
    lastclearrotation: Optional[int] = None,
    buffsets: Optional[List[RailwayBuffSetFormat]] = None,
    initseed: Optional[int] = None,
    currentseed: Optional[int] = None,
    enemySaveData: Optional[SaveDataForRailwayDungeon] = None,
) -> bool:
    try:
        update_fields = {}
        if prevclearnode is not None:
            update_fields["prevclearnode"] = prevclearnode
        if currentnode is not None:
            update_fields["currentnode"] = currentnode
        if lastclearnode is not None:
            update_fields["lastclearnode"] = lastclearnode
        if personalities is not None:
            update_fields["personalities"] = [p.dict() for p in personalities]
        if payreward is not None:
            update_fields["payreward"] = payreward
        if rewardstate is not None:
            update_fields["rewardstate"] = rewardstate
        if extrarewardstate is not None:
            update_fields["extrarewardstate"] = [er.dict() for er in extrarewardstate]
        if firstcleardate is not None:
            update_fields["firstcleardate"] = firstcleardate
        if currentclearrotation is not None:
            update_fields["currentclearrotation"] = currentclearrotation
        if lastenternodeid is not None:
            update_fields["lastenternodeid"] = lastenternodeid
        if lastclearrotation is not None:
            update_fields["lastclearrotation"] = lastclearrotation
        if buffsets is not None:
            update_fields["buffsets"] = [bs.dict() for bs in buffsets]
        if initseed is not None:
            update_fields["initseed"] = initseed
        if currentseed is not None:
            update_fields["currentseed"] = currentseed
        if enemySaveData is not None:
            update_fields["enemySaveData"] = enemySaveData.dict()

        if update_fields:
            rd_save_collection.update_one(
                {"uid": uid, "id": dungeon_id}, {"$set": update_fields}
            )
            return True

        return True

    except Exception as e:
        print(f"WARN:     {str(e)}")
        return False
