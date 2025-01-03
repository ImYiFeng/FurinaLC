from fastapi import FastAPI
from .battle import (
    EnterExpDungeon,
    EnterRailwayDungeon,
    EnterRailwayDungeonNode,
    EnterStageBattle,
    ExitExpDungeon,
    ExitStageBattle,
)
from .coupon import (
    GetUserCouponState,
    UseCoupon,
)
from .gacha import (
    ClaimClosedGachaRewards,
    PlayGacha,
)
from .logs import (
    CheckSeasonLog,
    FetchLatestSynchronousData,
    GetAbnormalityLogData,
    GetDailyDungeonInfo,
    GetDanteNoteState,
    GetDungeonSaveInfoAll,
    GetRailwayDungeonNodeAndLogAll,
)
from .theater import (
    CompleteTheaterStory,
    ExitStory,
    GetTheaterInfo,
)
from .user import (
    ChangeCurrentAnnouncer,
    GetFriendsData,
    GetProfileTicketDecoDatas,
    GetUserBanners,
    LoadUserDataAll,
    SetPersonalityGacksungIllust,
    UpdateFormation,
    UpdateLobbyCg,
    UpdateProfileTicketDeco,
    UpdateUserProfile,
)


def add_api_handler(app: FastAPI):
    app.post("/api/FetchLatestSynchronousData")(FetchLatestSynchronousData.handle)
    app.post("/api/LoadUserDataAll")(LoadUserDataAll.handle)
    app.post("/api/CheckSeasonLog")(CheckSeasonLog.handle)
    app.post("/api/UpdateFormation")(UpdateFormation.handle)
    app.post("/api/ChangeCurrentAnnouncer")(ChangeCurrentAnnouncer.handle)
    app.post("/api/SetPersonalityGacksungIllust")(SetPersonalityGacksungIllust.handle)
    app.post("/api/GetUserCouponState")(GetUserCouponState.handle)
    app.post("/api/UseCoupon")(UseCoupon.handle)
    app.post("/api/GetUserBanners")(GetUserBanners.handle)
    app.post("/api/GetProfileTicketDecoDatas")(GetProfileTicketDecoDatas.handle)
    app.post("/api/UpdateUserProfile")(UpdateUserProfile.handle)
    app.post("/api/UpdateProfileTicketDeco")(UpdateProfileTicketDeco.handle)
    app.post("/api/UpdateLobbyCg")(UpdateLobbyCg.handle)
    app.post("/api/GetFriendsData")(GetFriendsData.handle)
    app.post("/api/GetDungeonSaveInfoAll")(GetDungeonSaveInfoAll.handle)
    app.post("/api/GetRailwayDungeonNodeAndLogAll")(
        GetRailwayDungeonNodeAndLogAll.handle
    )
    app.post("/api/EnterRailwayDungeon")(EnterRailwayDungeon.handle)
    app.post("/api/ClaimClosedGachaRewards")(ClaimClosedGachaRewards.handle)
    app.post("/api/EnterStageBattle")(EnterStageBattle.handle)
    app.post("/api/ExitStageBattle")(ExitStageBattle.handle)
    app.post("/api/GetDailyDungeonInfo")(GetDailyDungeonInfo.handle)
    app.post("/api/EnterExpDungeon")(EnterExpDungeon.handle)
    app.post("/api/ExitExpDungeon")(ExitExpDungeon.handle)
    app.post("/api/GetAbnormalityLogData")(GetAbnormalityLogData.handle)
    app.post("/api/GetTheaterInfo")(GetTheaterInfo.handle)
    app.post("/api/CompleteTheaterStory")(CompleteTheaterStory.handle)
    app.post("/api/GetDanteNoteState")(GetDanteNoteState.handle)
    app.post("/api/PlayGacha")(PlayGacha.handle)
    app.post("/api/ExitStory")(ExitStory.handle)
    app.post("/api/EnterRailwayDungeonNode")(EnterRailwayDungeonNode.handle)
