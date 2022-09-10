filename = "test" + ".csv"
fw = open(filename, "w")
headers = "Product, Customer Name, Rating, Heading, Comment \n"
fw.write(headers)
reviews=[]
#mydict = {"Product": "searchString", "Name": "name", "Rating": "rating", "CommentHead": "commentHead","Comment": "custComment"}
mydict = ["searchString",  "name",  "rating",  "commentHead","custComment"]
reviews.append(mydict)
#mydict_1 = {"Product": "searchString_1", "Name": "name_1", "Rating": "rating_1", "CommentHead": "commentHead_1","Comment": "custComment_1"}
mydict_1 = ["searchString_1",  "name_1",  "rating_1",  "commentHead_1","custComment_1"]
reviews.append(mydict_1)

for i in reviews:
    k=i[0]
    for j in i[1:]:
        k=k+","+str(j)
    print(k)
    fw.write(str(k+"\n"))