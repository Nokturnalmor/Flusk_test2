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

    color = [[f'КЛ ','#653da9',f'КЛ Макс. мощность {round(F.valm(list_kl[2][0])/summ_mosh*100)}%','#00B0F0','КЛ с КД','#00B050','КЛ с ТД'],
             [f'КТ ','#d26e6a',f'КТ Макс. мощность {round(F.valm(list_kt[2][0])/summ_mosh*100)}%','#00B0F0','КТ с КД','#00B050','КТ с ТД'],
             [f'ШГ','#e7791f',f'ШГ Макс. мощность {round(F.valm(list_sg[2][0])/summ_mosh*100)}%','#00B0F0','ШГ с КД','#00B050','ШГ с ТД'],
             [f'ПР','#5b6b4a',f'ПР Макс. мощность {round(F.valm(list_pr[2][0])/summ_mosh*100)}%','#00B0F0','ПР с КД','#00B050','ПР с ТД'],
             [f'СУММ','#686868',f'Макс. мощность {round(summ_mosh/summ_mosh*100)}%','#00B0F0','с КД','#00B050','с ТД']]
    rez = [[],[],[],[],[],[]]
    rez_skd = [[], [], [], [], [], []]
    rez_std = [[], [], [], [], [], []]
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

        rez_skd[0].append(list_kl[0][i])
        rez_skd[1].append(round(F.valm(list_kl[3][i]) * koef))
        rez_skd[2].append(round(F.valm(list_kt[3][i]) * koef))
        rez_skd[3].append(round(F.valm(list_sg[3][i]) * koef))
        rez_skd[4].append(round(F.valm(list_pr[3][i]) * koef))
        rez_skd[5].append(round(F.valm(list_kl[3][i]) + F.valm(list_kt[3][i]) + F.valm(list_sg[3][i]) +
                            F.valm(list_pr[3][i])) * koef)

        rez_std[0].append(list_kl[0][i])
        rez_std[1].append(round(F.valm(list_kl[4][i]) * koef))
        rez_std[2].append(round(F.valm(list_kt[4][i]) * koef))
        rez_std[3].append(round(F.valm(list_sg[4][i]) * koef))
        rez_std[4].append(round(F.valm(list_pr[4][i]) * koef))
        rez_std[5].append(round(F.valm(list_kl[4][i]) + F.valm(list_kt[4][i]) + F.valm(list_sg[4][i]) +
                            F.valm(list_pr[4][i])) * koef)

        rez_default_mosh[0].append(list_kl[0][i])
        rez_default_mosh[1].append(round(F.valm(list_kl[2][i]) * koef))
        rez_default_mosh[2].append(round(F.valm(list_kt[2][i]) * koef))
        rez_default_mosh[3].append(round(F.valm(list_sg[2][i]) * koef))
        rez_default_mosh[4].append(round(F.valm(list_pr[2][i]) * koef))
        rez_default_mosh[5].append(round(F.valm(list_kl[2][i]) + F.valm(list_kt[2][i]) + F.valm(list_sg[2][i]) +
                            F.valm(list_pr[2][i])) * koef)

    fig = make_subplots(5, 1, y_title="Месячный тоннаж, Тонн",subplot_titles = " ")
    for i in range(1, 6):
        scatt_std = go.Scatter(x=rez_std[0], y=rez_std[i], name=color[i - 1][6], line=dict(color=color[i - 1][5]),fill='tozeroy')
        scatt_skd = go.Scatter(x=rez_skd[0], y=rez_skd[i], name=color[i - 1][4], line=dict(color=color[i - 1][3]),fill='tonexty')
        scatt = go.Scatter(x=rez[0], y=rez[i], name=color[i - 1][0], line=dict(color=color[i - 1][1]))
        scatt2 = go.Scatter(x=rez[0], y=rez_default_mosh[i], name =color[i-1][2],  line = dict(color='#e13d3d'))
        fig.add_trace(scatt_std, i, 1)
        fig.add_trace(scatt_skd, i, 1)
        fig.add_trace(scatt, i, 1)
        fig.add_trace(scatt2, i, 1)

    fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='black', size=14))
    fig.update_layout(height=int(900))

    with open('templates\\graf_pad_mosh.html', 'w+', encoding='utf-8') as f:
        f.write(fig.to_html(full_html=False))
    return fig.to_html(full_html=False)

#graf_html()
