import sys
from random import sample, choice, seed

first_name = list()
last_name = list()
with open('names.txt', 'r') as names_file:
    for name in names_file:
        full_name = name.strip().split()
        first_name.append(full_name[0])
        last_name.append(full_name[1])

course_codes = list()
with open('course_codes', 'r') as codes_file:
    for code in codes_file:
        course_codes.append(code.strip())

descriptions = list()
with open('desc.txt', 'r') as desc_file:
    for desc in desc_file:
        descriptions.append(desc.strip())

course_marks = ["HD", "DN", "CR", "PS", "FL", "ON"]
capacity_list = [5, 10, 15, 20, 25]
privacy_list = [1, 2, 3]

username = list()
user_num = 20
group_num = 50
with open('test_data.txt', 'w') as data_file:
    for i in range(1, user_num + 1):
        f = choice(first_name)
        l = choice(last_name)
        un = f'tester{i}'
        username.append(un)
        data_file.write(f'user = UserModel("{f}", "{l}", "{un}", "password")\n')
        for j in range(3):
            subject = choice(course_codes)
            mark = choice(course_marks)
            data_file.write(f'user.add_subject(SubjectModel("{subject}", "{mark}"))\n')
        data_file.write('system.add_user(user)\n')

    for i in range(1, group_num + 1):
        gname = choice(first_name)
        des = choice(descriptions)
        courses = sample(course_codes, 3)
        con = choice(username)
        attend = sample(username, 3)
        attend.append(con)
        attend = list(set(attend))
        capacity = choice(capacity_list)
        privacy = choice(privacy_list)
        data_file.write(f'group = GroupModel("{i}", "Group {gname}", "Location", "{des}", {courses}, 63643534234, "{con}", {attend}, {capacity}, {privacy})\n')
        data_file.write('system.add_group(group)\n')
    
