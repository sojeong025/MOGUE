import pandas as pd
from community.models import UserArticle
from django.conf import settings

tmp_data = pd.read.csv('community/fixtures/id,title,content,img,created_at,movie_id.csv', sep=';')

products = [
    UserArticle(
        title = tmp_data.ix[row]['title'],
        content = tmp_data.ix[row]['content'],
        img = tmp_data.ix[row]['img'],
        created_at = tmp_data.ix[row]['created_at'],
        movie_id = tmp_data.ix[row]['movie_id']
    ) 
    for row in tmp_data['id']
]
UserArticle.objects.bulk_create(products)