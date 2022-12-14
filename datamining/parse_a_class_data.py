from _operator import itemgetter
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

# быстрая сортировка
def quicksort(nums, fst, lst):
    if fst[1] >= lst[1]: return

    i, j = fst[1], lst[1]
    # pivot = nums[random.randint(fst, lst)][1]
    pivot = 0

    while i <= j:
        while nums[i][1] < pivot: i += 1
        while nums[j][1] > pivot: j -= 1
        if i <= j:
            nums[i][1], nums[j][1] = nums[j][1], nums[i][1]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


if __name__ == '__main__':
    profiles = []

# читаем сырой набор данных
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
    ###############################################################
    # собираем пары "id факультета - [id групп]
    fac_us_numb = {}
    # словарь id факультета -[[список групп 1]...[список групп Н]]
    fac_lg = {}

# список факультетов
    for u in profiles:
        with open("rawLabelsData.txt", "a", encoding="utf-8") as file:
            file.write(u.fac_id + "\n")
        file.close()
        buf_l_g = []
        buf_l_l_g = []

        for gr in u.groups:
            buf_l_g.append(gr[0])
# списки айдишников групп для каждого респондента
        with open("rawUsersData.txt", "a", encoding="utf-8") as file:
            file.write(str(buf_l_g) + "\n")
        file.close()

        if u.fac_id in fac_lg:
            buf_l_l_g = fac_lg[u.fac_id]  # list of lists of groups
            # buf_l2.append(buf_l)
            # fac_lg[u.fac_id] = buf_l2
        else:
            buf_l_l_g = []
            # buf_l2.append(buf_l)
            # fac_lg[u.fac_id] = buf_l2
        buf_l_l_g.append(buf_l_g)
        fac_lg[u.fac_id] = buf_l_l_g

    #################################################################

    excluded_facs = []

    med = 0
    count = 0

    for fac_id in fac_lg:
        if fac_lg[fac_id].__len__() < 2:
            excluded_facs.append(fac_id)
        else:
            med += fac_lg[fac_id].__len__()
            count += 1

    med = med / count
    print("MED: " + str(med))

    ####################################################################

    filtered_fac_lg = {}

    for fac_id in fac_lg:
        if fac_id in excluded_facs or fac_lg[fac_id].__len__() < 292:
            pass
        else:
            filtered_fac_lg[fac_id] = fac_lg[fac_id]

    ###################################################################
    # сначала отсортировать по количеству групп у каждого участника список,
    # потом удалить самых меньших, чтобы осталось 297 выживших
    for fac_id in filtered_fac_lg:
        # представим, что здесь сортировка списка списков по кол-ву эл-в
        sorted_l = filtered_fac_lg[fac_id]
        sorted_l.sort(key=len, reverse=True)
        del sorted_l[0: 347]
        del sorted_l[397:len(sorted_l)]
        filtered_fac_lg[fac_id] = sorted_l
        ##########################################################################
        with open("addonsData.txt", "a", encoding='utf-8') as file:
            file.write(str(fac_id) + ":::" + str(sorted_l) + "\n")
