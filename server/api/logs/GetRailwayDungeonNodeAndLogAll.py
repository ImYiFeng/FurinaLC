from limbus.requests import Cs, ReqGetRailwayDungeonNodeAndLogAllCommand
from limbus.responses import Sc, RspGetRailwayDungeonNodeAndLogAllCommand
# from database.railway_dungeon.save_info import (
#     get_railway_dungeon_save_info
# )
# from database.railway_dungeon.node_data import (
#     get_railway_node_data
# )

async def handle(req: Cs[ReqGetRailwayDungeonNodeAndLogAllCommand]):
    # uid = req.userAuth.uid
    # dungeon_id = req.parameters.dungeonId
    
    # save_info = get_railway_dungeon_save_info(uid, dungeon_id)
    # node_data = get_railway_node_data(uid, save_info.)

    return Sc[RspGetRailwayDungeonNodeAndLogAllCommand](
        result=RspGetRailwayDungeonNodeAndLogAllCommand()
    )
