from flask import Flask, url_for, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def latest_news(channel_name):
    telegram_url = 'https://t.me/s/'
    url = telegram_url + channel_name
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    link = soup.find_all('a')
    url = link[-1]['href']
    url = url.replace('https://t.me/', '')
    channel_name, news_id = url.split('/')
    urls = []
    for i in range(5):
        urls.append(f'{channel_name}/{int(news_id) - i}')
    return urls

@app.route('/site')
def index():
    return f"""<!doctype html>
                <html>
                <head>
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                   <title>GenshinFun.ru</title>
                     <div id='rectangle'><div>
                     <div id="button1">
                      <button onclick="window.location.href = 'http://127.0.0.1:8080/arts';" class="btn btn-primary">Арты</button>
                      <button onclick="window.location.href = 'http://127.0.0.1:8080/characters';" class="btn btn-primary">Биография</button>
                      <button onclick="window.location.href = 'http://127.0.0.1:8080/tg';" class="btn btn-primary">Новости</button>
                      <button onclick="window.location.href = 'http://127.0.0.1:8080/torg';" class="btn btn-primary">Торговцы</button>
                     </div>
                </head>
                <body>
                    <div class="inform">
                        Рады приветствовать тебя на сайте GenshinFun. Здесь ты найдешь много<br>
                        интересного, а именно: крутые арты, биография архонтов, полезные ссылки,<br>
                        полезные новости.<br>
                        <center><font color="lime" size="26">Немного о игре Genshin Impact</font></center>
                        «Genshin Impact» – приключенческая ролевая игра с открытым миром. Вам <br>
                         предстоит исследовать волшебный мир Тейват. На этом огромном континенте <br>
                         вы посетите семь королевств, найдёте спутников с различными умениями и <br>
                         сразитесь с могущественными врагами в поисках пропавшего близкого человека.<br>
                         А ещё можно просто странствовать безо всякой цели, разгадывая тайны<br>
                         наполненного жизнью мира. Пусть любопытство указывает вам путь! Разыщите<br>
                         родного человека и узнайте, что же всё-таки произошло!<br>
                         <font color="darkred" size="18">Полезные ссылки</font><br>
                         <a href="https://www.hoyolab.com/home">Hoyolab</a> - для сбора ежедневных наград<br>
                         <a href="https://genshin-impact-map.appsample.com/?map=teyvat">Genshin Impact Map</a> - интерактивная карта<br>
                         <a href="https://paimon.moe/wish/">Paimon.moe</a> - счетчик круток<br>
                         <img class="klee" src="{url_for('static', filename='img/top_klee.jpg')}" alt="">
                    </div>
                    <div class="text" style="font-variant:inherit"><h1>GenshinFun<h1></div>
                    <img id="fon_img" src="{url_for('static', filename='img/fon_1.jpg')}" alt="">
                </body>
                </html> """


@app.route('/characters')
def main_page():
    return f"""<!doctype html>
                <html>
                <head>
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                   <title>Архонты</title>
                   <div id="hm_button">
                    <button onclick="window.location.href = 'http://127.0.0.1:8080/site';">Вернуться</button>
                   </div>
                </head>
                <body bgcolor="#ffffff">
                   <center id="mon"><b>Монштад<b><center>
                   <img class="venti" src="{url_for('static', filename='img/venti123.png')}" alt="">
                   <div class="txt1">
                    <mark>Венти</mark> -  обычный бард, слоняющийся по улочкам Мондштадта.
                    Неведомые ветра привели барда в эти земли. Порой его песни стары как свет, а иной раз он напевает еще
                    ненаписанные строки. Он любит яблоки и живую атмосферу, но не любит сыры и всё липкое.
                    Когда он управляет ветрами, его Анемо сила проявляется в виде перьев. Венти привлекает их лёгкость и беспечность.
                    Венти поселился в Мондштадте совсем недавно, и его заработок был намного ниже остальных бардов-мондштадтцев.
                    Но завидев достаточную сумму в горшочке, будьте уверены, Венти потратит ее в ближайшей таверне.
                    Но несовершеннолетний облик Венти не позволяет ему купить алкоголь.
                    Когда ему отказали в первый раз, Венти только пробормотал что-то вроде: «А вот раньше таких правил не было».
                    Но когда он узнал, что подобное правило установлено во всех тавернах города, Венти придумал новый план.
                    Вместо того, чтобы просить за свои выступления мора, Венти зажимал в зубах бокал, одновременно играя на лире,
                    и просил своих зрителей подливать ему вино.
                    Такие нововведения добавили ему популярности в Мондштадте.
                    Однако главной причиной срывов выступлений была его аллергия на кошек.
                    Он начинал неистово чихать даже при одном их виде и надеялся, что рядом не будут проходить кошки,
                    когда он будет выступать с зажатым в зубах бокалом вина.
                    Поэтому Венти для своих выступлений выбирает места подальше от пушистых, но каким-то образом бездомные
                    коты тянутся к нему даже с других концов города.   
                   </div>
                   <center id="lu"><b>Лю эй<b><center>
                   <img class="ded" src="{url_for('static', filename='img/deed.png')}" alt="">
                   <div class="txt2">
                    <mark>Чжун Ли</mark> — спокойный, сдержанный и вежливый человек, который много знает об истории и культуре Ли Юэ.
                    Он придерживается очень философских взглядов на деньги и с большим уважением относится к традициям Ли Юэ,
                    в том числе к тем, которые были забыты или искажены с течением времени. Чжун Ли очень ценит контракты.
                    Несмотря на то, что Чжун Ли обладает широким кругозором, как правило, он скромен, и даже кажется
                    несколько неуверенным в том,
                    что он, как он выражается, «буржуазный паразит» Одной из наиболее характерных черт Чжун Ли является
                    его склонность
                    забывать о Море в сделках, соглашаясь тратить большие суммы денег, не имея под рукой никакой Моры,
                    и даже принимая "скидки"
                    как должное, несмотря на то, что это очевидная афера. Он часто полагается на финансовую поддержку
                    других или Похоронного
                    Бюро «Ваншэн» Хотя он дружит с Ху Тао, которая доверяет ему больше всех, ему не нравится её
                    детское поведение. 
                    Позже выясняется, что его беспечность вызвана тем, что он был Гео Архонтом и создателем Моры.
                    С Сердцем Бога, позволяющим
                    создавать бесконечное количество моры, ему никогда не приходилось беспокоиться о нехватке личных
                    финансов. К сожалению, когда он
                    решил жить среди смертных, ему не хватило дальновидности, чтобы найти альтернативу для смертных,
                    чтобы чеканить Мору без Сердца Бога. 
                    Чжун Ли, как и Венти, по видимому видит своё человеческое обличие как нечто отдельное от своей
                    божественной формы. Как Бог Контрактов, Чжун Ли воспринимает контракты серьёзно и честно, поскольку выполнять
                    соглашение легко, и недоумевает, как люди не могу соблюдать такую простую концепцию; он утверждает,
                    что все, кто нарушает контракт, будут страдать от Гнева Камня.
                   </div>
                   <center id="inadzuma"><b>Инадзума<b><center>
                   <img class="baal" src="{url_for('static', filename='img/baal.png')}" alt="">
                   <div class="txt3">
                    <mark>Сёгун Райдэн</mark> твёрдо верит в то, что, по её мнению, является вечностью — местом, в котором всё
                    остается неизменным, независимо от того, что происходит на самом деле. Она благородна в своём
                    поведении и почитаема народом Инадзумы. Сёгун Райдэн существует в двух формах: Райдэн Эи, её истинная
                    личность, и Сёгун, кукла, созданная Эи, чтобы действовать в качестве правителя Инадзумы вместо неё,
                    пока та медитирует в Мире Эвтюмии. Эта кукла следует набору запрограммированных в ней директив,
                    которые чрезвычайно трудно изменить даже самой Эи. Сёгун холодна и сурова по характеру, временами
                    даже черства; она ограничена в эмоциях, не имеет симпатий и антипатий и не нуждается в отдыхе.
                    Сёгун считает себя помощницей Эи и делает именно то, что она хочет, не больше и не меньше; она не
                    может действовать без её руководства, и если функции куклы отключены, Сёгун становится неспособной
                    делать что-либо. Из-за ограниченного набора функций и апатии Эи ко всему, что находится за пределами
                    вечности, которую она ищет, Сёгуном легко могут манипулировать внешние силы, например, когда Клан
                    Кудзё и Фатуи использовали её, чтобы начать и увековечить Указ об Охоте за Глазами Бога.
                    Хотя Эи всё ещё относительно стойкая по сравнению с большинством людей, она заметно более эмоциональна
                    и дружелюбна, чем Сёгун. В отличие от неё, у Эи есть любимые и нелюбимые вещи, такие как сладости.
                    Из-за своей преданности вечности, Эи с опаской относится к переменам, хотя проявляет, скорее
                    любопытство, чем презрение, когда речь заходит о новых вещах, таких как внешний вид Путешественника
                    и обычаи современного мира. Из-за того, что она потеряла многих своих близких на протяжении веков,
                    Эи движет страх перед дальнейшей потерей, желая сохранить Инадзуму на всю вечность. 
                   </div>
                </body>
                </html> """


@app.route('/arts')
def a_lot_of_arts():
    return f"""<!doctype html>
                  <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                    <title>Арты по игре Genshin Impact</title>
                  </head>
                  <body bgcolor="#282828">
                  <div class="col-md-4 col-lg-offset-1">
                          <br><button type="button" class="btn btn-primary btn-lg" onclick="window.location.href = 'http://127.0.0.1:8080/site';">Вернуться</button><br>
                  </div>
                  <div class="container">
                    <br>
                    <div id="myCarousel" class="carousel slide" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#myCarousel" data-slide-to="1" class="active"></li>
                        <li data-target="#myCarousel" data-slide-to="2"></li>
                        <li data-target="#myCarousel" data-slide-to="3"></li>
                        <li data-target="#myCarousel" data-slide-to="4"></li>
                        <li data-target="#myCarousel" data-slide-to="5"></li>
                      </ol>
                      <div class="carousel-inner" role="listbox">
                        <div class="item active">
                          <img src="{url_for('static', filename='img/img1.jpg')}" alt="1">
                              <div class="carousel-caption d-none d-md-block">
                              </div>
                        </div>
                        <div class="item">
                          <img src="{url_for('static', filename='img/img2.jpg')}" alt="2">
                              <div class="carousel-caption d-none d-md-block">
                              </div>
                        </div>
                        <div class="item">
                          <img class="d-block w-100" src="{url_for('static', filename='img/img3.jpg')}" alt="3">
                          <div class="carousel-caption d-none d-md-block">
                              </div>
                        </div>
                        <div class="item">
                          <img src="{url_for('static', filename='img/img4.jpg')}" alt="4">
                          <div class="carousel-caption d-none d-md-block">
                              </div>
                        </div>
                        <div class="item">
                          <img class="d-block w-100" src="{url_for('static', filename='img/img5.jpg')}" alt="5">
                          <div class="carousel-caption d-none d-md-block">
                          </div>
                        </div>
                      </div>
                      <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>
                    </div>
                  </div>
                  </body>
                  </html> """


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                            <title>Регистрация</title>
                          </head>
                          <body>
                               <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <input type="password" class="form-control" id="password" placeholder="Повторите пароль" name="repassword">
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <input type="button" onclick="window.location.href = 'http://127.0.0.1:8080/site';" value="Зарегистрироваться"/>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['repassword'])
        print(request.form['class'])
        print(request.form['sex'])
        return


@app.route('/tg', methods=["POST", "GET"])
def telegram():
    url = []
    if request.method == "GET":
        return render_template('index.html', url=url)
    else:
        channel_name = request.form['adress']
        urls = latest_news(channel_name)
        return render_template('index.html', urls=urls)


@app.route('/torg')
def shopper():
    return f"""<!doctype html>
                <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <title>Полезные торговцы</title> 
                </head>
                <body>
                   <div id="home_button">
                   <button onclick="window.location.href = 'http://127.0.0.1:8080/site';" class="btn btn-primary">Вернуться</button>
                   </div>
                   <center><h1>Торговцы, которых<br> возможно ты искал</h1></center>
                   <div class="torg_txt">
                        <b id='torg_mon'>Торговцы моншатада</b><br>
                        <a href="#C1">Флора, владелица «Шёпота цветов» (появляется днём)</a><br>
                        <a href="#C2">Гёте, владелец отеля «Гёте»</a><br>
                        <a href="#C3">Бланш, продавец «Мондштадтского купца»</a><br>
                        <a href="#C4">Великолепный Хопкинс (передвигается)</a><br>
                        <a href="#C5">Клорис, ботаник (передвигается)</a><br>
                        <a href="#C6">Нантак, мастер рыбалки из Мондштадта</a><br>
                        <b id='torg_lu'>Торговцы Лю эй</b><br>
                        <a href="#C7">Верр Голдет, хозяйка постоялого двора «Ваншу»</a><br>
                        <a href="#C8">Мисс Бай, мельник</a><br>
                        <a href="#C9">Бо Лай, хозяин «Тысячи мелочей»</a><br>
                        <a href="#C10">Цзи Фан, хозяйка книжного магазина «Ваньвэнь»</a><br>
                        <a href="#C11">Травник Гуй, целитель из хижины «Бубу»</a><br>
                        <a href="#C12">Ли Цай, работница глазурного павильона</a><br>
                        <a href="#C13">Юэ Шу, работница шатра «Синьюэ»</a><br>
                        <a href="#C14">Чан Шунь, торговец</a><br>
                        <a href="#C15">Ши Тоу, хозяин «Загадки нефрита»</a><br>
                        <a href="#C16">Шеф-повар Мао, хозяин ресторана «Народный выбор»</a><br>
                        <b id='torg_inadzuma'>Торговцы Инадзумы</b><br>
                        <a href="#C17">Аои, владелец магазина «Цукумомоно»</a><br>
                        <a href="#C18">Симура Камбэй, владелец ресторана «Симура»</a><br>
                        <a href="#C19">Курода, редактор издательского дома Яэ</a><br>
                        <a href="#C20">Киминами Анна, владелец ресторана «Киминами»</a><br>
                        <a href="#C21">Цю Юэ, управляющий филиалом торговой компании Тюю</a><br>
                        <a href="#C22">Обата, рыбак</a><br>
                        <a href="#C23">Ямасиро Кэнта</a><br>
                        <a href="#C24">Кудзирай Момидзи, инадзумская мастерица рыбалки</a><br>
                    </div>
                    <div class="txt_mon">
                        <strong id='torg_mon'><right><font size='24px'>Торговцы моншатада</font></right></strong><br>
                        <strong id="C1">Флора, владелица «Шёпота цветов» (появляется днём)</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/flora.jpg')}" alt=""><br><br>
                            -Цветок-сахарок;<br>
                            -Ветряная астра;<br>
                            -Сесилия;<br>
                            -Трава-светяшка;<br>
                            -Лилия калла.<br><br>
                        <strong id="C2">Гёте, владелец отеля «Гёте»(появляется днём)</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/gete.jpg')}" alt=""><br><br>
                            -Указатель из сухого дерева;<br>
                            -Палатка с громоотводом;<br>
                            -Простая одноместная палатка;<br>
                            -Лагерь искателей приключений.<br><br>
                        <strong id="C3">Бланш, продавец «Мондштадтского купца»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/blansh.jpg')}" alt=""><br><br>
                        -Соль; <br>
                            -Перец;<br>
                            -Лук;<br>
                            -Молоко;<br>
                            -Помидор;<br>
                            -Капуста;<br>
                            -Картофель;<br>
                            -Пшеница.<br><br>
                        <strong id="C4">Великолепный Хопкинс (передвигается)</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/hopkins.jpg')}" alt=""><br><br>
                            -Святая вода<br><br>
                        <strong id="C5">Клорис, ботаник (передвигается)</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/kloris.jpg')}" alt=""><br><br>
                            -Львиный зев;<br>
                            -Мята;<br>
                            -Волчий крюк;<br>
                            -Валяшка;<br>
                            -Гриб филанемо.<br><br>
                        <strong id="C6">Нантак, мастер рыбалки из Мондштадта</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/Nantak.jpg')}" alt=""><br><br>
                            -Рецепт: Кровавое месиво;<br>
                            -Рецепт: Фальшивый червь;<br>
                            -Рецепт: Фальшивая муха;<br>
                            -Переплетение ветров.<br><br>
                        <strong id='torg_lu'><font size='24px'>Торговцы Лю эй</font></strong><br>
                        <strong id="C7">Верр Голдет, хозяйка постоялого двора «Ваншу»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/ver.jpg')}" alt=""><br><br>
                            -Миндальный тофу;<br>
                            -Голубцы с грибами;<br>
                            -Острая курица на пару;<br>
                            -Лапша «Дары гор»;<br>
                            -Куриный шашлычок с грибами;<br>
                            -Мацутакэ;<br>
                            -Сливочное масло;<br>
                            -Сосиска;<br>
                            -Шелковица;<br>
                            -Стеклянный колокольчики;<br>
                            -Рецепт: Вегетарианские мидии;<br>
                            -Рецепт: Свиной суп с бамбуком;<br>
                            -Рецепт: Обжаренные креветки.<br><br>
                        <strong id="C8">Мисс Бай, мельник</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/baj.jpg')}" alt=""><br><br>
                            -«Сельская услада»;<br>
                            -Тофу;<br>
                            -Миндаль;<br>
                            -Шелковица;<br>
                            -Глазурная лилия;<br>
                            -Рецепт: Лапша «Дары гор»;<br>
                            -Рецепт: «Сельская услада»;<br>
                            -Рецепт: Заоблачный гоба<br><br>
                        <strong id="C9">Бо Лай, хозяин «Тысячи мелочей»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/boo_torg.jpg')}" alt=""><br><br>
                            -Яблоко;<br>
                            -Закатник;<br>
                            -Рыба;<br>
                            -Звёздная ракушка.<br><br>
                        <strong id="C10">Цзи Фан, хозяйка книжного магазина «Ваньвэнь»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/czi-fan.jpg')}" alt=""><br><br>
                            -Властелин Инкогнито. Том IV;<br>
                            -Записи бродяги. Отлив;<br>
                            -Хроники заоблачного предела: Дворец морского божества;<br>
                            -Хроники заоблачного предела: Горные духи;<br>
                            -Хроники заоблачного предела: Цилинь;<br>
                            -Хроники заоблачного предела: Укрытый нефрит;<br>
                            -Традиции Ли Юэ: Шелковица;<br>
                            -Жемчужная нить. Том II;<br>
                            -Жемчужная нить. Том III;<br>
                            -Одинокий клинок в пустошах IV;<br>
                            -Разбитые мечты: Сапфир;<br>
                            -Ночь в бамбуковом лесу II;<br>
                            -Ночь в бамбуковом лесу III;<br>
                            -Легенда о разбитой алебарде. Том I;<br>
                            -Легенда о разбитой алебарде. Том IV;<br>
                            -Легенда о разбитой алебарде. Том V;<br><br>
                        <strong id="C11">Травник Гуй, целитель из хижины «Бубу»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/travnik.jpg')}" alt=""><br><br>
                            -Цветок цинсинь;<br>
                            -Конский хвост;<br>
                            -Чашечка лотоса;<br>
                            -Туманный цветок (венчик);<br>
                            -Пылающий цветок (тычинка);<br>
                            -Стеклянные колокольчики;<br>
                            -Рецепт: Яичный суп из лотоса.<br><br>
                        <strong id="C12">Ли Цай, работница глазурного павильона</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/li_torg.jpg')}" alt=""><br><br>
                            -Деликатесы скалистой гавани;<br>
                            -Лапша «Дары гор»;<br>
                            -Ветчина на сковороде;<br>
                            -Мясо «Тяньшу»;<br>
                            -Рецепт: Деликатесы скалистой гавани;<br>
                            -Рецепт: Ветчина на сковороде.<br><br>
                        <strong id="C13">Юэ Шу, работница шатра «Синьюэ»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/ua_shy.jpg')}" alt=""><br><br>
                            -Жареная лапша с рыбой;<br>
                            -Шарики с креветкой;<br>
                            -Полнолунная яичница;<br>
                            -Золотистый краб;<br>
                            -Рецепт: Жареная лапша с рыбой;<br>
                            -Рецепт: Полнолунная яичница.<br><br>
                        <strong id="C14">Чан Шунь, торговец</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/chan_torg.jpg')}" alt=""><br><br>
                            -Картофель;<br>
                            -Сахар;<br>
                            -Сыр;<br>
                            -Кор ляпис;<br>
                            -Электро кристалл.<br><br>
                        <strong id="C15">Ши Тоу, хозяин «Загадки нефрита»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/shi_torg.jpg')}" alt=""><br><br>
                            -Обломок железа;<br>
                            -Обломок белого железа;<br>
                            -Полуночный нефрит.<br><br>
                        <strong id="C16">Шеф-повар Мао, хозяин ресторана «Народный выбор»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/mao.jpg')}" alt=""><br><br>
                            -Яичница по-тейватски;<br>
                            -Рыбацкий бутерброд;<br>
                            -Куриный шашлычок с грибами;<br>
                            -Мука;<br>
                            -Сахар;<br>
                            -Сосиска;<br>
                            -Ветчина;<br>
                            -Рыба;<br>
                            -Краб;<br>
                            -Побеги бамбука;<br>
                            -Чашечка лотоса;<br>
                            -Мацутакэ;<br>
                            -Гриб;<br>
                            -Морковь;<br>
                            -Редис;<br>
                            -Заоблачный перчик;<br>
                            -Рецепт: Мятный салат;<br>
                            -Рецепт: Крабовый тофу;<br>
                            -Рецепт: Чёрный окунь;<br>
                            -Рецепт: Рыба-белка;<br>
                            -Рецепт: «Налетайка»;<br>
                            -Рецепт: «Благоденствие»;<br>
                            -Рецепт: «Мясные рулетики с мятой»;<br>
                            -Рецепт: Жареная рыба-тигр;<br>
                            -Рецепт: Рисовые пампушки;<br>
                            -Рецепт: Острая курица на пару;<br>
                            -Рецепт: Кристальные баоцзы;<br>
                            -Рецепт: Суп «Три вкуса»;<br>
                            -Рецепт: Лапша «Борода дракона».<br><br>
                        <strong id='torg_inadzuma'><font size='24px'>Торговцы Инадзумы</font></strong><br>
                        <strong id="C17">Аои, владелец магазина «Цукумомоно»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/aoi.jpg')}" alt=""><br><br>
                            -Соль;<br>
                            -Перец;<br>
                            -Лук;<br>
                            -Молоко;<br>
                            -Помидор;<br>
                            -Капуста;<br>
                            -Картофель;<br>
                            -Пшеница;<br>
                            -Рис;<br>
                            -Мясо креветки;<br>
                            -Тофу;<br>
                            -Трава наку.<br><br>
                        <strong id="C18">Симура Камбэй, владелец ресторана «Симура»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/simura.jpg')}" alt=""><br><br>
                            -Яичница по-тейватски;<br>
                            -Куриный шашлычок с грибами;<br>
                            -Рыбацкий бутерброд;<br>
                            -Рыба;<br>
                            -Краб;<br>
                            -Морская водоросль;<br>
                            -Фиалковая дыня;<br>
                            -Редис;<br>
                            -Сосиска;<br>
                            -Бекон;<br>
                            -Мука;<br>
                            -Сахар;<br>
                            -Рецепт: Яичный рулет;<br>
                            -Рецепт: Мисо-суп;<br>
                            -Рецепт: Якисоба;<br>
                            -Рецепт: Тонкоцу рамэн;<br>
                            -Рецепт: Унаги тядзукэ;<br>
                            -Рецепт: Пять драгоценных солений;<br>
                            -Рецепт: Креветочные печенья сакуры;<br>
                            -Рецепт: Суши с креветками;<br>
                            -Рецепт: Яичные суши;<br>
                            -Рецепт: Угорь-кабаяки;<br>
                            -Рецепт: Рагу отшельника;<br>
                            -Рецепт: Лапша удон;<br>
                            -Рецепт: Рисовый омлет.<br><br>
                        <strong id="C19">Курода, редактор издательского дома Яэ</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/kuroda.jpg')}" alt=""><br><br>
                            -Войны Хамаварана (Предисловие);<br>
                            -Войны Хамаварана (I);<br>
                            -Войны Хамаварана (II);<br>
                            -Ведьма и гончая. Том X;<br>
                            -Ведьма и гончая. Том XI;<br>
                            -Новые хроники шести кицунэ: Предисловие;<br>
                            -Новые хроники шести кицунэ (I);<br>
                            -Новые хроники шести кицунэ (II);<br>
                            -Новые хроники шести кицунэ (IV);<br>
                            -Новые хроники шести кицунэ (V);<br>
                            -Легенда о клинке (I);<br>
                            -Легенда о клинке (II);<br>
                            -Легенда о клинке (III);<br>
                            -Легенда о клинке (IV).<br>
                            -Странные теории Киёсикэн Синкагэути. Том I;<br>
                            -Змей и драконы из Токоёкоку;<br>
                            -Мина, принцесса павшего народа. Том I;<br>
                            -Мина, принцесса павшего народа. Том II;<br>
                            -Мина, принцесса павшего народа. Том III;<br>
                            -Мина, принцесса павшего народа. Том IV;<br>
                            -Мина, принцесса павшего народа. Том VI;<br>
                            -Цветы для принцессы Фишль. Том 0.<br><br>
                        <strong id="C20">Киминами Анна, владелец ресторана «Киминами»</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/anna.jpg')}" alt=""><br><br>
                            -Вкусный суп одзони;<br>
                            -Грибная пицца;<br>
                            -Особая грибная пицца;<br>
                            -Рецепт: Трёхцветное данго;<br>
                            -Рецепт: Суши с тунцом;<br>
                            -Рецепт: Тройные шашлычки;<br>
                            -Рецепт: Соба;<br>
                            -Рецепт: Рагу из редиса и рыбы;<br>
                            -Рецепт: Вакатакэни;<br>
                            -Рецепт: Ягодный мидзу мандзю;<br>
                            -Рецепт: Тайяки;<br>
                            -Рецепт: Жареный тото.<br><br>
                        <strong id="C21">Цю Юэ, управляющий филиалом торговой компании Тюю</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/cu_ua.jpg')}" alt=""><br><br>
                            -Обломок железа;<br>
                            -Обломок белого железа;<br>
                            -Электро кристалл.<br><br>
                        <strong id="C22">Обата, рыбак</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/obata.jpg')}" alt=""><br><br>
                            -Рыба;<br>
                            -Краб;<br>
                            -Мясо креветки;<br>
                            -Морской гриб.<br><br>
                        <strong id="C23">Ямасиро Кэнта</strong><br>
                        <i>Магазин открывается после завершения задания легенд Райдэн «Мимолётные сны».</i>
                        <img class="foto_torg" src="{url_for('static', filename='img/obata.jpg')}" alt=""><br><br>
                            -Жемчужина Санго;<br>
                            -Угорь;<br>
                            -Кубок везунчика;<br>
                            -Орлиное перо везунчика;<br>
                            -Серебряная корона везунчика;<br>
                            -Клевер везунчика;<br>
                            -Песочные часы везунчика.<br><br>
                        <strong id="C24">Кудзирай Момидзи, инадзумская мастерица рыбалки</strong><br>
                        <img class="foto_torg" src="{url_for('static', filename='img/Momidzi.jpg')}" alt=""><br><br>
                            -Нарукава Угай;<br>
                            -«Улов»;<br>
                            -Мера вина Ако.<br>       
                    </div>
                </body>
                </html> """

if __name__ == '__main__':
   app.run(port=8080, host='127.0.0.1')
