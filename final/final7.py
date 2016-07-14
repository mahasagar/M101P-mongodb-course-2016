# Collection
MongoCollection albums = database.getCollection("albums");
# Images
MongoCollection imgColl = database.getCollection("images");
FindIterable images = imgColl.find();
for (Document image : images) {
	Document album = albums.find(new Document("images", image.get("_id"))).first();
	if (album == null) {
		print image;
	}
}
