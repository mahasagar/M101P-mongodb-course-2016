#Creaing Doc
 - creating docs using insert functions.
 - db.movieScratch.insert({"title":"Rocky","year":"1976","imdb":"12121"})
 - db.movieScratch.find().pretty()
 - creating multiple docs
    - db.movieScratch.insertMany([{"title":"Rocky","year":"1976","imdb":"12121"},{"title":"Rocky","year":"1976","imdb":"12121"}])
 - _id is unique.so..we cant use same _id again[duplicate key ].
    db.movieScratch.insert([{"title":"sholay","year":"1976","_id":"1212"},{"title":"sholay","year":"1976","_id":"1313"}])
 - it will still continue the insertion if error

 - insert is primary command to create docs
 - update command["upserts", can also be use to insert in doc
