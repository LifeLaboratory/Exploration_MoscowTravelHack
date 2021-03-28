from main.filter.processor import Processor


class Provider:
    @staticmethod
    def get_filter():
        processor = Processor()
        orders = processor.get_orders()
        category = processor.get_categories()
        distance = processor.get_distance_types()
        favorite = processor.get_favorite()
        seasons = processor.get_seasons()
        tourism_type = processor.get_trip_types()
        tags = processor.get_tags()
        cities = processor.get_cities()
        data = {
            'orders': orders,
            'filters': {
                'Категории': category,
                'Вид туризма': tourism_type,
                'На расстоянии': distance,
                'Избранные': favorite,
                'Теги': tags,
                'Сезонность': seasons,
                'Город': cities
            },
            'default_filters': {
                'category': [
                    'Памятник'
                ],
                'Город': [
                    'Мурманск'
                ]
            }
        }
        return data