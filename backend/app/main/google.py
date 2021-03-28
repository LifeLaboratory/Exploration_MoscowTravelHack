from main.base.provider import Provider
import requests


def get_google_info():
    """Метод запрашивает рейтинги мест в google по координатам мест"""
    places = Provider('main/sql').exec_by_file('get_places_for_tags.sql', {})
    google_key = ''
    for place in places:
        try:
            id_place = place['id']
            text_input = place['title']
            r = requests.get(f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={text_input}&inputtype=textquery&fields=rating,types&key={google_key}')
            try:
                rating = r.json()['candidates'][0]['rating']
                types = r.json()['candidates'][0]['types']
            except:
                rating = 0
                types = None
            Provider('main/sql').exec_by_file('insert_ratings.sql', {
                'id': id_place,
                'rating': rating,
            })
            if types:
                for type in types:
                     Provider('main/sql').exec_by_file('insert_tags.sql', {
                        'titles': [type]
                    })
                tags_inserted = Provider('main/sql').exec_by_file('get_tags_by_title.sql', {
                    'titles': types
                })
                for tag in tags_inserted:
                    Provider('main/sql').exec_by_file('insert_place_tag.sql', {
                        'place_id': id_place,
                        'tag_id': tag['id']
                    })
        except:
            pass

get_google_info()