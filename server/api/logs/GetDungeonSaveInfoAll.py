from limbus.requests import Cs, ReqGetDungeonSaveInfoAll
from limbus.responses import Sc, RspGetDungeonSaveInfoAll
from limbus.formats import (
    StoryDungeonSaveInfoFormat,
    MirrorDungeonSaveInfoFormat,
    # RailwayDungeonSaveInfoFormat,
    StoryMirrorDungeonSaveInfoFormat,
    # StoryDungeonCurrentInfoFormat,
    # DungeonMapNodeFormat,
    MirrorDungeonCurrentInfoFormat,
    StoryMirrorDungeonCurrentInfoFormat,
    MirrorDungeonClearInfoFormat,
    MirrorDungeonHistoryFormat,
)
from database.railway_dungeon.save_info import get_railway_dungeon_save_info


async def handle(req: Cs[ReqGetDungeonSaveInfoAll]):
    railway_id = req.parameters.railwayDungeonId
    user_id = req.userAuth.uid

    story_save_info = StoryDungeonSaveInfoFormat()

    mirror_origin_save_info = MirrorDungeonSaveInfoFormat(
        dungeonId=-1,
        idx=-1,
        currentInfo=MirrorDungeonCurrentInfoFormat(
            eid=-1,
        ),
    )

    railway_save_info = get_railway_dungeon_save_info(user_id, railway_id)

    story_mirror_save_info = StoryMirrorDungeonSaveInfoFormat(
        dungeonid=-1,
        currentinfo=StoryMirrorDungeonCurrentInfoFormat(
            eid=-1,
        ),
    )

    mirror_dungeon_clear_infos = [
        MirrorDungeonClearInfoFormat(
            dungeonid=railway_id,
            idx=0,
            clearnumber=1,
            defeatnumber=1,
        )
    ]

    mirror_dungeon_histories = [
        MirrorDungeonHistoryFormat(
            dungeonid=railway_id,
        )
    ]

    return Sc[RspGetDungeonSaveInfoAll](
        result=RspGetDungeonSaveInfoAll(
            storySaveInfo=story_save_info,
            mirrorOriginSaveInfo=mirror_origin_save_info,
            railwaySaveInfo=railway_save_info,
            storyMirrorSaveInfo=story_mirror_save_info,
            mirrorDungeonClearInfos=mirror_dungeon_clear_infos,
            mirrorDungeonHistories=mirror_dungeon_histories,
        )
    )
