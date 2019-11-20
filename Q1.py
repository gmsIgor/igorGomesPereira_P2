#Q1
#a)
def parse_dic_date(date):
    list_date = date.split("/")
    dicio_date = {"ANO":int(list_date[0]), \
    "MES":int(list_date[1]), \
    "DIA":int(list_date[2])}

    return dicio_date

#b)
def is_active(status):
    if status[-2:] == "\n":
        status = status[:-1]

    status_bool = Nill                                   #should be 'None'

    if str(status) == "SIM":
        status_bool = True
    else:
        status_bool = False

    return status_bool

#c)
def list_info(info):
    listed_info = info.split(":")

    return listed_info

#d)
def separate_info(file):
    file.seek(0,0)
    read_file = file.readlines(file)
    info_list = []

    for line in read_file:
        info_list.append(line)
    file.close() #this file gets useless

    return info_list

#e)
def main():
    arq = open("cadastro.txt", "r")
    list_users = []
    info_list = separate_info(arq)

    for user in info_list:
        cpf = str(user_info[0])
        nome = str(user_info[1])
        nasc = parse_dic_date(user_info[2])
        cad_dat = parse_dic_date(user_info[3])
        ativo = is_active(user_info[4])

        list_users.append({"CPF": cpf, \
        "NOME": nome, \
        "DATA_DE_NASCIMENTO": nasc, \
        "DATA_DO_CADASTRO": cad_dat, \
        "ATIVO": ativo})

    for user in list_users:
        print(user)

main()
