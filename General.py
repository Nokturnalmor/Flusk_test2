import project_cust_38.Cust_Functions as F
from flask import Flask, render_template, url_for, request
import project_cust_38.Cust_SQLite as CSQ
import graf_pad_mosh as GRAF
from jinja2 import Environment, BaseLoader


def generate_html(my_list):
    rtemplate = Environment(loader=BaseLoader()).from_string(my_list)

    return rtemplate

# https://fontawesome.ru/all-icons/

if F.nalich_file('templates') is False:
    F.sozd_dir('templates')

if F.nalich_file('static/css') is False:
    F.sozd_dir('static/css')

if F.nalich_file('static/images') is False:
    F.sozd_dir('static/images')

list_projects = [{"way":"КЛ","nn":'0193-21'},{"way":"КТ","nn":'0134-721'},
                 {"way":"КЛ","nn":'3193-21'},{"way":"КТ","nn":'3134-721'}]
list_ways = sorted(list({x['way'] for x in list_projects}))


zag_pr = ['Заготовительное производство', ["""Выполняет раскрой изделий чёрных и нержавеющих заготовок из 
листового металлопроката- способом лазерной резки металла. Имеем гильотину для резки металла. Имеет возможность 
оказывать услуги гибочных работ по металлу, а также пробивные работы листового металлопроката. """]]
meh_pr = ['Участок механической обработки', ["""Имеет возможность обрабатывать изделия из
 нержавеющих, черных сталей, титана. Используем токарные станки, сверлильно-расточные аппараты, фрезерные станки. 
"""]]
sb_pr = ['Слесарно-каркасный сборочно-сварочный цех ', ["""Выполняет вальцовку деталей, нарезание резьбы в отверстиях,
 разметку, рубку, рихтовку, сверление, полировку и сборку металлоконструкций. Производит сварочные работы : 
 газовая сварка и резка металла, различные режимы полуавтоматической сварки, различные режимы аргонодуговой 
 сварки вольфрамовым электродами, включая пульсирующий режим, точечная сварка"""]]
mal_pr = ['Цех покрытий и финишной обработки', ["""Производит работы по пескоструйной обработке металла, покрасочные
 работы. Выполняется покраска серийной продукции и мелких партий 
 металлоконструкций. Покрасочное производство ориентировано на большое количество различных мелких деталей, 
 работы по металлу выполняются с помощью ручных распылителей с электростатических эффектом. Применяется для 
 быстрой окраски больших плоских поверхностей"""]]

divisions = [['Отдел комплектации', ["""Контролирует условия хранения оборудования, упаковывание продукции и 
комплектующих изделий, правильность их консервации и обеспечение сохранности. Организует ведение учёта наличия и 
движения оборудования и комплектующих изделий, ответственные при передаче продукции на склад. """, ]],
             ['Технологичекий отдел производства', ["""Разрабатывает технологические нормативы, инструкции, 
             схемы сборки, маршрутные карты, карты технического уровня и качества продукции и другую 
             технологическую документацию, вносит изменения в техническую документацию в связи с корректировкой 
             технологических процессов и режимов производства""", ]],
             ['Планово-диспетчерский отдел', ["""Контроль выполнения графика выпуска продукции цехом и прохождения 
             ДСЕ в цикле производства, ведение производственного плана на предприятие и предоставление отчётности по
              эффективности его выполнения. """, ]],
             ['Производственные цеха', ["""Основное производственное подразделение предприятия, участвует в общем
              процессе производства, выполняют определенные функции по изготовлению продукции по маршрутной карте 
              проекта. """, ]],
             ['Отдел механика', ["""Основная задача отдела является организация бесперебойной и технически правильной 
             эксплуатации и надежной работы тепло-энергического оборудования, содержание его в работоспособном 
             состоянии и на требуемом уровне точности""", ]],
             ['Главный сварщик', ["""Руководит технологической подготовкой выполнения сварочных работ, обеспечивает 
             изготовление и выпуск высококачественной продукции, совершенствование конструкций изделий, их 
             технологичность, экологичность, высокую производительность труда.""", ]], ]

leaderships = [['Антон Беляков', 'Обращаться по вопросам организации производственного процесса, регламентов'],
               ['Александр Серегин', 'Обращаться по вопросам выполнения производственных заданий и планов'],
               ['Ирина Власова', 'Обращаться по вопросам комплектации ДСЕ, готовой продукции'],
               ['Александр Гусев', 'Обращаться по вопросам сроков изготовления продукции, планов работ'],
               ['Виктор Егоров', 'Обращаться по вопросам ремонта и технического обслуживания оборудования'],
               ['Алексей Диков', 'Обращаться по вопросам технологической подготовки производства'],]

dict_info_ind = {'title': 'Производство Powerz', """o_nas""": ["""Энергия сильных людей - энергия лучших идей
""", ''],
                 'opportunity': [[zag_pr[0], zag_pr[1]],
                                 [meh_pr[0], meh_pr[1]],
                                 [sb_pr[0], sb_pr[1]],
                                 [mal_pr[0], mal_pr[1]], ],
                 'documents': {'title': """ Целью 
                 политики в области качества является разработка, 
                 выпуск и реализация конкурентоспособной продукции в установленные сроки, в заданных объемах, с уровнем 
                 качества, удовлетворяющим требованиям и ожиданиям наших потребителей и других заинтересованных сторон,
                  обеспечение устойчивого экономического положения организации, здоровья и безопасности персонала""",
                               "body": [
                                        """В своей работе мы руководствуемся –  законодательством РФ, а также 
                 собственной совестью. Неотъемлемой частью нашей работы является качество и сроки продукции.""","""Важно 
                 следовать документам, стандартам предприятия. """,]},
                 'fun_msg': ["""Пылесос был изобретен случайно. Один инженер заметил, что его новейший отпугиватель 
                 котов еще и неплохо втягивает пыль.""", 'Народное'],
                 'media': ['Медиа', 'о нас','https://novgorod-tv.ru/news/novgorodskaya-kompaniya-pauerz-prodolzhaet-narashhivat-zarubezhnye-rynki-sbyta-nevziraya-na-sankczii/',
                           "https://novgorod-tv.ru/novosti/58018-novgorodskoe-predpriyatie-kelast-planiruet-zapustit-novyj-tsekh.html"]}

dict_info_elem = {'title': 'План работ'}
r"""Sub ads()
          Set wb = Application.ActiveWorkbook
          Call FF.vigruzit_v_txt("C:\Python\Flusk_test2\templates\", "table.txt", "Çàäà÷è (4).xlsx", "Ëèñò1", 1, 10, "|")
End Sub
"""
def load_pr_proj():
    return  F.otkr_f(r'O:\Журналы и графики\Ведомости для передачи\table_pr_proj.txt',False,"|")

def clear_py(py):
    old_fr = r"Отдел технолога\В работе\Заказы для собственных нужд"
    py = py.replace(old_fr, '')
    py = py.replace('\\', '')
    return  py

def load_projects():
    dict_mk = CSQ.zapros('C:/DB_srv/Naryad.db',f"""SELECT Пномер, Номенклатура, Номер_заказа || "$" || Номер_проекта FROM mk""",rez_dict=True)


    def add_line(tbl,row):
        py = clear_py(row['Номер заявки'])

        mk_list = []

        for item in dict_mk:
            if item['Номер_заказа || "$" || Номер_проекта'] == row['Номер заявки'] + '$' + row['Номер проекта']:
                mk_list.append(item['Номенклатура'].replace(';','; '))

        tbl.append([row['Номер проекта'],py,row['Статус'],row['Кд'], row['Нормо-час сб'],'; '.join(mk_list),
              row['Резка'].split('/')[0], row['Мех_обработка'].split('/')[0],row['Сборка+сварка'].split('/')[0],
                    row['Покрытие'].split('/')[0], row['Упаковка'].split('/')[0]])
    list_table = F.otkr_f(r'O:\Журналы и графики\Ведомости для передачи\Sroki_etapov.txt', False, "|")
    list_table = F.list_to_dict(list_table)
    shapka = ['Номер проекта','Номер заявки','Статус','Дата получения КД', 'Нормо-час сб', 'Тех.прораб, МК',
              'Резка План_заверш', 'Мех_обработка План_заверш','Сборка+сварка План_заверш', 'Покрытие План_заверш', 'Упаковка План_заверш']
    tbl_kt = [shapka].copy()
    tbl_kl = [shapka].copy()
    tbl_shg = [shapka].copy()
    tbl_pr = [shapka].copy()

    for i in range(len(list_table)):
        if list_table[i]['Направление'] == "КТ":
            add_line(tbl_kt, list_table[i])
        if list_table[i]['Направление'] == "КЛ":
            add_line(tbl_kl, list_table[i])
        if list_table[i]['Направление'] == "ШГ":
            add_line(tbl_shg, list_table[i])
        if list_table[i]['Направление'] == "ПР":
            add_line(tbl_pr, list_table[i])
    tbl_kt = F.sort_po_kol(tbl_kt,'Сборка+сварка План_заверш', date_time=True,date_format="%d.%m.%Y")
    tbl_kl = F.sort_po_kol(tbl_kl, 'Сборка+сварка План_заверш', date_time=True,date_format="%d.%m.%Y")
    tbl_shg = F.sort_po_kol(tbl_shg, 'Сборка+сварка План_заверш', date_time=True,date_format="%d.%m.%Y")
    tbl_pr = F.sort_po_kol(tbl_pr, 'Сборка+сварка План_заверш', date_time=True,date_format="%d.%m.%Y")

    return [tbl_kt,
            tbl_kl,
            tbl_shg,
            tbl_pr]

def load_change_projects():
    list_table_etap = F.otkr_f(r'O:\Журналы и графики\Ведомости для передачи\Sroki_etapov.txt', False, "|")
    list_table_smena = F.otkr_f(r'O:\Журналы и графики\Ведомости для передачи\Изменение сроков сб.txt', False, "|")
    rez = [["Дата записи","Номер проекта","Номер заявки","Было","Стало","Разница,дней","Примечание"]]
    for item in list_table_smena[1:]:
        np = item[1]
        py = item[2]
        for etap_row in list_table_etap:
            if etap_row[0] == np and etap_row[1] == py:
                if item[5] != '-':
                    item[2] = clear_py(item[2])
                    rez.append(item)
                break
    return rez



app = Flask(__name__)


@app.route("/")
@app.route("/index")
def root():
    print(url_for('root'))
    return render_template('index.html', title=dict_info_ind['title'], o_nas=dict_info_ind['o_nas'],
                           opportunity=dict_info_ind['opportunity'], documents=dict_info_ind['documents'],
                           fun_msg=dict_info_ind['fun_msg'], divisions=divisions, media=dict_info_ind['media'],
                           leaderships=leaderships)


@app.route("/elements")
def elements():
    print(url_for('elements'))
    table_pr_proj = load_pr_proj()
    return render_template('elements.html', title=dict_info_elem['title'], leaderships=leaderships, divisions=divisions,
                           list_ways = list_ways, table_pr_proj=table_pr_proj)

@app.route("/projects")
def projects():
    print(url_for('projects'))
    kt_projects, kl_projects, shg_projects, pr_projects = load_projects()
    changes = load_change_projects()
    graf_pad_mosh = GRAF.graf_html()
    graf = generate_html(graf_pad_mosh)
    return render_template('projects.html', title=dict_info_elem['title'],
                           kt_projects=kt_projects,
                           kl_projects=kl_projects,
                           shg_projects=shg_projects,
                           pr_projects=pr_projects,
                           changes=changes,
                           date_now = F.now("%H:%M %d.%m.%Y"),graf_pad_mosh = graf)


@app.route("/projects/<way>", methods = ["POST","GET"])
def way(way):
    print(url_for('way', way =way))
    if request.method == 'POST':
        print(request.form)
    return render_template("way.html", title = way, list_projects = [_ for _ in list_projects if _['way'] == way])


@app.route("/projects/<way>/<proj>")
def info(way,proj):
    print(url_for('info', way = way, proj = proj))
    return f'Проект инфо {way}, {proj}'


if __name__ == "__main__":
    #app.run(debug=True, host='192.168.50.230', port=20001)
    app.run(debug=False,host='192.168.50.230',port=20000)
