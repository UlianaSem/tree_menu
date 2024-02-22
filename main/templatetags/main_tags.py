from django.template import Library

from main.models import Item

register = Library()


@register.inclusion_tag("main/includes/items.html")
def draw_menu(menu, item):
    """
    Получает необходимые для вывода пункты меню
    :param menu: id меню
    :param item: id выбранного пункта
    :return: dict пунктами меню
    """
    def get_item(point):
        if point == '':
            point = None
            return [(0, menu_items.filter(parent=point))]

        point = menu_items.get(pk=point)
        points = []

        while point is not None:
            points.append((point.pk, menu_items.filter(parent=point)))
            point = point.parent

            if point is None:
                points.append((0, menu_items.filter(parent=point)))

        return points

    menu_items = Item.objects.filter(menu=menu)
    required_items = get_item(item)

    return {
        "menu_items": sort_answer(required_items, menu_items)
    }


def sort_answer(items, menu):
    """
    Приводит пункты меню в нужный порядок
    :param items: требуемые пункты меню
    :param menu: все пункты меню
    :return: list с пунктами меню
    """
    answer = []

    for item in reversed(items):
        try:
            index = answer.index(menu.get(pk=item[0]))
        except ValueError:
            index = 0
        except Item.DoesNotExist:
            index = len(answer)

        for i in item[1]:
            answer.insert(index, i)

    answer = list(reversed(answer))

    return answer


@register.simple_tag()
def build_answer(items):
    """
    Строит разметку меню
    :param items: пункты меню
    :return: string
    """
    string = ''

    for index in range(len(items)):
        template = \
            f"""<li class="nav-item"><a class="nav-link active"
             href="/get_item/{items[index].pk}/">{items[index].name}</a></li>\n"""

        if index == 0:
            string += template
        elif items[index].level > items[index-1].level:
            string += ('<ul>\n' + template)
        elif items[index].level < items[index-1].level:
            difference = (items[index-1].level - items[index].level) * '</ul>\n'
            string += (difference + template)
        else:
            string += template

    return string
