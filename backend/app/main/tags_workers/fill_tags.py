from main.base.provider import Provider
from main.tags_workers.tags import get_tfidf, get_most_3, get_first_word

def fill_tags():
    places = Provider('main/sql').exec_by_file('get_places_for_tags.sql', {})
    result_tags = {}
    for place in places:
        result_tags[place['id']] = [get_first_word(place['title'])] + [get_most_3(place['description'])]
    tf_idf_result = get_tfidf(places)
    for key, value in tf_idf_result.items():
        if len(value) > 3:
            value = value.replace(',', '')
            value = value.replace('»', '')
            value = value.replace('«', '')
            result_tags[key] += [value]
    all_tags = []
    for tags in result_tags.values():
        all_tags += tags
    Provider('main/sql').exec_by_file('insert_tags.sql', {
        'titles': list(set(all_tags))
    })
    tags = Provider('main/sql').exec_by_file('get_tags.sql', {})

    for tag in tags:
        for key, valu in result_tags.items():
            if tag['title'] in valu:
                Provider('main/sql').exec_by_file('insert_place_tag.sql', {
                    'place_id': key,
                    'tag_id': tag['id']
                })
                break
    test = 1


fill_tags()