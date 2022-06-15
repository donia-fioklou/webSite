import json

from blog.models import BlogPost




chemin = "D:/development/blog-blogpost.json"

with open(chemin, "r") as f:
    data = json.load(f)
    
for bp in data:
    BlogPost.objects.create(title=bp["title"],
                            slug=bp["slug"],
                            published=bp["published"],
                            description=bp["description"],
                            date=bp["date"])