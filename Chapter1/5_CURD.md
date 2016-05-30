#CURD
 - help : list of commands
 - show dbs : show databases
 - use db_name : to get in db : if not exists it make it in lazy and when insert it make it complete 
 - show collections : show all the collections/ like table
 - db.movie.insertOne({"title": "sucide Sqaud","yyear":"2016"});
 - return value is doc : wirte is successed
                         object id
 - unique object id is added
 - db.movie.find().pretty()
   - returns all the movies from movie collection
   - pretty() : formated output
 - first parameter for find({}) : will matach and return docs
 - db.movie.find({"year":"2016"}).pretty()
   - return value of find is not array of  docs.its Cursor object
     - we can assign the return to variable
     - its like js
   - we can use hasNext(),next() on that assign variable
   - var c = db.movie.find()
         c.hasNext()
	   - return true
         c.next()
	   - return doc
   
