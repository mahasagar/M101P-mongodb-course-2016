#Update
 ->
  db.movieDetails.update({title:"The Martain"},
  {$set: {"awards": {"wins" : "8"}}})

 - db.movieDetails.update(
         {title:"The Martian"},
         {$push:
           {reviews:
               {
                  rating:4.5,
                  date:ISODate("2016-01-12T09:00:00Z"),
                  reviewr:"sagar",
                  text:"The Martian is Awesome movie"
                                 }}})
 -