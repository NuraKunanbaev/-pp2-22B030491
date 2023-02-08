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
task = int(input("Choose the task: "))
if task == 1:
    def rating(s):
        for i in range(len(movies)):
            if movies[i]["name"] == s:
                if movies[i]["imdb"] >=5.5:
                    print("True")
                else:
                    print("False")
    s = input("Write name of the film: ")
    rating(s)

elif task == 2:
    def best_movies(movies):
        print("Best movies:")
        for i in range(len(movies)):
            if movies[i]["imdb"] >= 5.5:
                print(movies[i]["name"], movies[i]["imdb"])
    best_movies(movies)

elif task == 3:
    def category(s2):
        print("Movies in this category:")
        for i in range(len(movies)):
            if movies[i]["category"] == s2:
                print(movies[i]["name"])
    s2 = input("Enter the category: ")
    category(s2)
elif task == 4:
    print("average imdb in this movies:")
    def average_imdb(movies):
        sum = 0
        for i in range(len(movies)):
            sum+=movies[i]["imdb"]
        print(sum/(len(movies)))
    average_imdb(movies)
elif task == 5:
    def average_imdb_category(s3):
        sum2, sum3 = 0, 0
        for i in range(len(movies)):
            if movies[i]["category"] == s3:
                sum2+=movies[i]["imdb"]
                sum3+=1
        print("average value imdb is this category:", sum2/sum3)
    s3 = input("Enter the category: ")
    if __name__ == '__main__':
        average_imdb_category(s3)
