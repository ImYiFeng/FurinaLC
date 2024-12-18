from limbus.requests import Cs, ReqEnterRailwayDungeon
from limbus.responses import Sc, RspEnterRailwayDungeon
from limbus.formats import RailwayDungeonSaveInfoFormat, RailwayNodeDataFormat
from database.railway_dungeon.save_info import (
    get_railway_dungeon_save_info,
    update_railway_dungeon_save_info,
)
from database.railway_dungeon.node_data import (
    get_railway_node_data,
    update_railway_node_data,
)

async def handle(req: Cs[ReqEnterRailwayDungeon]):
    user_id = req.userAuth.uid
    dungeon_id = req.parameters.dungeonId
    personalities = req.parameters.personalities

    node_data = RailwayNodeDataFormat()

    update_railway_dungeon_save_info(
        uid=user_id, dungeon_id=dungeon_id, personalities=personalities
    )

    save_info = get_railway_dungeon_save_info(user_id, dungeon_id)

    return Sc[RspEnterRailwayDungeon](
        result=RspEnterRailwayDungeon(
            saveInfo=save_info,
            startNodeData=node_data,
        )
    )
