import plotly.graph_objects as go
from plotly.subplots import make_subplots
import project_cust_38.Cust_Functions as F

def graf_html():
    list_kl = F.otkr_f("O:\Журналы и графики\Ведомости для передачи\gr_pad_mosh_kl.txt", separ="|")
    list_kt = F.otkr_f("O:\Журналы и графики\Ведомости для передачи\gr_pad_mosh_kt.txt", separ="|")
    list_sg = F.otkr_f("O:\Журналы и графики\Ведомости для передачи\gr_pad_mosh_sg.txt", separ="|")
    list_pr = F.otkr_f("O:\Журналы и графики\Ведомости для передачи\gr_pad_mosh_pr.txt", separ="|")
    #list_kl[1] = [round(F.valm(_)*204) for _ in list_kl[1]]
    #list_kl[2] = [F.valm(_)*204 for _ in list_kl[2]]
    summ_mosh = F.valm(list_kl[2][0]) + F.valm(list_kt[2][0]) + F.valm(list_sg[2][0]) + F.valm(list_pr[2][0])


    color = [[f'КЛ ','#8974AC',f'КЛ Макс. мощность {round(F.valm(list_kl[2][0])/summ_mosh*100)}%'],
             [f'КТ ','#E1AFAD',f'КТ Макс. мощность {round(F.valm(list_kt[2][0])/summ_mosh*100)}%'],
             [f'ШГ','#F9B883',f'ШГ Макс. мощность {round(F.valm(list_sg[2][0])/summ_mosh*100)}%'],
             [f'ПР','#C5D69E',f'ПР Макс. мощность {round(F.valm(list_pr[2][0])/summ_mosh*100)}%'],
             [f'СУММ','#ABABAB',f'Макс. мощность {round(summ_mosh/summ_mosh*100)}%']]
    rez = [[],[],[],[],[],[]]
    rez_default_mosh = [[], [], [], [], [], []]
    koef = 3.8
    
    for i in range(len(list_kl[0])):
        rez[0].append(list_kl[0][i])
        rez[1].append(round(F.valm(list_kl[1][i]) * koef))
        rez[2].append(round(F.valm(list_kt[1][i]) * koef))
        rez[3].append(round(F.valm(list_sg[1][i]) * koef))
        rez[4].append(round(F.valm(list_pr[1][i]) * koef))
        rez[5].append(round(F.valm(list_kl[1][i]) + F.valm(list_kt[1][i]) + F.valm(list_sg[1][i]) +
                            F.valm(list_pr[1][i])) * koef)

        rez_default_mosh[0].append(list_kl[0][i])
        rez_default_mosh[1].append(round(F.valm(list_kl[2][i]) * koef))
        rez_default_mosh[2].append(round(F.valm(list_kt[2][i]) * koef))
        rez_default_mosh[3].append(round(F.valm(list_sg[2][i]) * koef))
        rez_default_mosh[4].append(round(F.valm(list_pr[2][i]) * koef))
        rez_default_mosh[5].append(round(F.valm(list_kl[2][i]) + F.valm(list_kt[2][i]) + F.valm(list_sg[2][i]) +
                            F.valm(list_pr[2][i])) * koef)

    fig = make_subplots(5, 1, y_title="Месячный тоннаж, Тонн",subplot_titles = " ")
    for i in range(1, 6):
        scatt = go.Scatter(x=rez[0], y=rez[i], name = color[i-1][0], line=dict(color=color[i-1][1]))
        scatt2 = go.Scatter(x=rez[0], y=rez_default_mosh[i], name =color[i-1][2],  line = dict(color='rgb(215,20,20)'))
        fig.add_trace(scatt, i, 1)
        fig.add_trace(scatt2, i, 1)

    fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='black', size=14))
    fig.update_layout(height=int(900))

    with open('templates\\graf_pad_mosh.html', 'w+') as f:
        f.write(fig.to_html(full_html=False))
    return fig.to_html(full_html=False)

#graf_html()