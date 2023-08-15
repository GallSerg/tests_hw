import unittest


class TestFirstTask(unittest.TestCase):

    def test_ff(self):
        expected_string = """На курсе Java-разработчик с нуля есть тёзки: Иван Бочаров, Иван Маркитан, Максим Батырев, Максим Воронцов, Сергей Индюков, Сергей Сердюк
На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Александр Иванов, Александр Ульянцев, Александр Шлейко, Евгений Шек, Евгений Шмаргунов
На курсе Python-разработчик с нуля есть тёзки: Александр Бардин, Александр Иванов, Александр Ульянцев
На курсе Frontend-разработчик с нуля есть тёзки: Александр Беспоясов, Александр Фитискин, Александр Шлейко"""
        self.assertEqual(first_function(), expected_string, 'Not equal')

    def test_sf(self):
        expected_string = """Python-разработчик с нуля - 12 месяцев
Java-разработчик с нуля - 14 месяцев
Fullstack-разработчик на Python - 20 месяцев
Frontend-разработчик с нуля - 20 месяцев"""
        not_expected = 'no'
        self.assertMultiLineEqual(second_function(), expected_string, 'Not multi-line equal')

    @unittest.expectedFailure
    def test_tf(self):
        expected_string = """Самый короткий курс(ы): Python-разработчик с нуля - <built-in function min> месяца(ев)
Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - <built-in function max> месяца(ев)"""
        not_expected = 'Not expected string'
        self.assertEqual(third_function(), not_expected, 'Expected failure not working')

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_py_f(self):
        assert first_function() == 'No'


def first_function():
    # Это вы мне? Подсчитываем тёзок на каждом курсе
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = []
    res = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":course, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)

    for course in courses_list:
        names_list = []
        for mentor in course["mentors"]:
            name, surname = mentor.split()
            names_list.append(name)
        unique_names = set(names_list)
        unique_names_list = sorted(list(unique_names))

        count_list = [names_list.count(name) for name in unique_names_list]
        same_name_list = []
        for name in unique_names_list:
            if names_list.count(name) > 1:
                for full_name in course["mentors"]:
                    first_name, surname = full_name.split()
                    if first_name == name:
                        same_name_list.append(full_name)
        if same_name_list:
            res.append(f'На курсе {course["title"]} есть тёзки: {", ".join(sorted(same_name_list))}')
    return '\n'.join(res)


def second_function():
    # Наводим порядок: упорядочиваем курсы по продолжительности

    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]

    courses_list = []
    res = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {k: [] for k in durations}
    for id, course in enumerate(courses_list):
        key = durations[id]
        durations_dict[key].append(course["title"])
    durations_dict = dict(sorted(durations_dict.items()))
    for duration, course in durations_dict.items():
        for cr in course:
            res.append(f'{cr} - {duration} месяцев')
    return '\n'.join(res)


def third_function():
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
               "Frontend-разработчик с нуля"]
    mentors = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
         "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
         "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
         "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
         "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
         "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
         "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
         "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
    ]
    durations = [14, 20, 12, 20]
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    mini = min(durations)
    maxi = max(durations)
    maxes = []
    minis = []
    res = []
    for index, duration in enumerate(durations):
        if duration == maxi:
            maxes.append(index)
        elif duration == mini:
            minis.append(index)
    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"])
    for id in maxes:
        courses_max.append(
            courses_list[id]["title"])
    courses_max = ', '.join(courses_max)
    courses_min = ', '.join(courses_min)
    res.append(f'Самый короткий курс(ы): {courses_min} - {min} месяца(ев)')
    res.append(f'Самый длинный курс(ы): {courses_max} - {max} месяца(ев)')
    return '\n'.join(res)


if __name__ == '__main__':
    unittest.main(verbosity=4)
