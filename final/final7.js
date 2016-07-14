var cur = db.images.find();
 
var j = 0;
while(cur.hasNext()){
	doc = cur.next();
	image_id = doc._id
 
	b = db.albums.find({images : image_id}).count()
	if(b == 0){
		db.images.remove({_id:image_id})
                print(image_id)
		j++;
	}
}
print(j)
