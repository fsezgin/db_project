db = db.getSiblingDB("library")
db.library.drop()

db.library.insertMany([
    {
        "id": 1,
        "author": "Mark Twain",
        "name": "İnsan Nedir?"
    },
    {
        "id": 2,
        "author": "Friedrich Nietzsche",
        "name": "İşte Böyle Buyurdu Zerdüşt"
    }
]);