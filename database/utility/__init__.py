from database.client import db


def wipe_all_docs_contains_uid(uid: int, wipe_user: bool = False, db=db):
    collections = [
        "railway_dungeon_saves",
        "userbanners",
        "userprofiles",
        "usertickets",
        "announcers",
        "egos",
        "formations",
        "items",
        "personalities",
    ]
    if wipe_user:
        collections.append("users")

    for collection_name in collections:
        collection = db[collection_name]
        result = collection.delete_many({"uid": uid})
        print(
            "INFO:     "
            + f"Removed {result.deleted_count} document(s) from {collection_name}"
        )
