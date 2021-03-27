from backend.app.main.base.provider import Provider


class Processor:
    @staticmethod
    def get_orders():
        return [
                'category',
                'Вид туризма',
                'На расстоянии',
                'Избранные',
                'Сезонность',
                'Теги'
            ]

    @staticmethod
    def get_categories():
        categories = Provider('main/sql').exec_by_file('get_place_categories.sql')
        return [category.get('title') for category in categories]

    @staticmethod
    def get_trip_types():
        trips = Provider('main/sql').exec_by_file('get_trip_categories.sql')
        return [trip.get('title') for trip in trips]

    @staticmethod
    def get_distance_types():
        return ['Пеший', 'На автомобиле']

    @staticmethod
    def get_favorite():
        return True

    @staticmethod
    def get_tags():
        tags = Provider('main/sql').exec_by_file('get_tags.sql')
        return [tag.get('title') for tag in tags]

    @staticmethod
    def get_seasons():
        seasons = Provider('main/sql').exec_by_file('get_list_seasons.sql')
        return [season.get('title') for season in seasons]
