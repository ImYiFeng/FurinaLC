from limbus.requests import Cs, ReqEnterRailwayDungeonMapNodeCommand
from limbus.responses import Sc, RspEnterRailwayDungeonMapNodeCommand


async def handle(req: Cs[ReqEnterRailwayDungeonMapNodeCommand]):
    cur_node_id = req.parameters.nodeid
    prev_node_id = cur_node_id if (cur_node_id - 1) <= 0 else cur_node_id - 1

    return Sc[RspEnterRailwayDungeonMapNodeCommand](
        result=RspEnterRailwayDungeonMapNodeCommand(
            nodeid=cur_node_id,
            currentNodeId=cur_node_id,
            prevClearNodeId=prev_node_id,
        )
    )
