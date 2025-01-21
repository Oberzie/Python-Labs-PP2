# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def single_rate():
    name_of_movie = input("name of the movie: ")
    for x in movies:
        if x["name"]== name_of_movie and x["imdb"] > 5.5:
            print("True")

#2
def sublist():
    for x in movies:
        if x["imdb"] > 5.5:
            print(x["name"])
        
#3
def categories():
    category = input("what category should be movie: ")
    for x in movies:
        if x["category"] == category:
            print(x["name"])
 
 
#4
def avarage_imdb():
     total = 0
     for x in movies:
         total += x["imdb"]
     avg = total / len(movies)
     print(f"The average imdb rating is: {avg}")
         
         
#5 
def avarage_imdb_of_category():
    ctg = input("what category should be movie: ")
    total = 0
    count = 0
    for x in movies:
        if ctg == x["category"]:  
         total += x["imdb"]
         count += 1
    avg = total / count
    print(f"The average imdb rating of {ctg} is: {avg}")
        
#single_rate()
#sublist()
#categories()
#avarage_imdb()
#avarage_imdb_of_category()