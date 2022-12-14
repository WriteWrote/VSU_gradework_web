import numbers


class Person:
    def __init__(self, id, inst_id, inst_name, fac_id, fac_name, year,
                 groups):
        self.id = id
        self.inst_id = inst_id
        self.inst_name = inst_name
        self.fac_id = fac_id
        self.fac_name = fac_name
        self.year = year
        self.groups = groups


if __name__ == '__main__':
    profiles = []

    # читаем сырой набор данных и создаем список объектов Person
    # каждый Person представляет собой полные данные о вузе, факультете и списке групп
    with open("res_class_A.txt", "r", encoding='utf-8') as file:
        for line in file:
            parts = line.split(" ::: ")
            user_info = parts[0].strip("(").strip(")").strip("\'").split(", ")
            groups_info = parts[1].split(")(")
            groups_list = []

            for gr in groups_info:
                gr = gr.strip("(").strip(")").strip("\'").strip("")
                if gr.split(", \'").__len__() < 2:
                    gr = gr.strip("\"")
                    groups_list.append(gr.split(", \""))
                groups_list.append(gr.split(", \'"))

            profiles.append(Person(user_info[0], user_info[1],
                                   user_info[2], user_info[3],
                                   user_info[4], user_info[5],
                                   groups_list))
    file.close()

    # проходимся по всему списку профилей
    # словарь: айдишник - список списков групп
    # распихиваем по словарю всех пользователей:
    # извлекаем id всех групп профиля в список
    # если номер группы не парсится в число, не добавляем в список
    # проходимся по словарю:
    # сортируем каждый список списков групп по количеству групп
    # выходим из словаря и сортируем факультеты по количеству групп

    dict = {}

    for profile in profiles:
        if profile.fac_id not in dict:
            dict[profile.fac_id] = []

        profile_groups = []
        for group_pair in profile.groups:
            if group_pair[0].isdigit():
                profile_groups.append(group_pair[0])

        dict[profile.fac_id].append(profile_groups)

    for faculty in dict:
        dict[faculty].sort(key=len, reverse=True)

    # res = " ".join(sorted(dict, key=lambda key: len(dict[key])))
    res = sorted(dict.items(), key=lambda i: len(i[1]), reverse=True)

    file5classes = "parsedData14122022//parsedData5Classes.txt"
    file10classes = "parsedData14122022//parsedData10Classes.txt"

# for writing uncomment "file.write" sections
    with open(file10classes, "a", encoding='utf-8') as file:
        for i in range(10):
            # faculty id
            file.write(str(res[i][0]) + ": ")
            # faculty list of lists of groups
            # (291 for 10 classes)
            for j in range(291):
                # for each group
                for k in range(len(res[i][1][j])):
                    #for each element in group
                   file.write(str(res[i][1][j][k]) + " ")
                file.write("| ")

    file.close()

    with open(file5classes, "a", encoding="utf-8") as file:
        for i in range(5):
            # faculty id
            file.write(str(res[i][0]) + ": ")
            # faculty list of lists of groups
            # (601 for 5 classes)
            for j in range(601):
                # for each group
                for k in range(len(res[i][1][j])):
                    # for each element in group
                    file.write(str(res[i][1][j][k]) + " ")
                file.write("| ")

    file.close()


    print("finish him")
'''
    for i in range(10):
        print(len(res[i][1]))

    print("------")

    for i in range(10):
        for j in range(10):
            print(len(res[i][1][j]))
        print("***")
'''
