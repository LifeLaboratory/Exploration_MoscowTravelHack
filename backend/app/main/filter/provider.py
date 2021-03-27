from main.filter.processor import Processor


class Provider:
    @staticmethod
    def get_filter():
        orders = Processor().get_orders()
        category = Processor().get_categories()
        distance = Processor().get_distance_types()
        favorite = Processor().get_favorite()
        seasons = Processor().get_seasons()
        tourism_type = Processor().get_trip_types()
        tags = Processor().get_tags()
        data = {
            'orders': orders,
            'filters': {
                'Категории': category,
                'Вид туризма': tourism_type,
                'На расстоянии': distance,
                'Избранные': favorite,
                'Теги': tags,
                'Сезонность': seasons
            },
            'default_filters': {
                'category': [
                    'Памятник'
                ],
                'Теги': [
                    'Экстрим'
                ]
            }
        }
        return data