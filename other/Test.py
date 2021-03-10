import P2

temp = [
    (
        [
            ['74%', 'nazar8@yahoo.com', None, 'false', 'false', '02.12.2000'],
            ['11%', 'timofej43@yandex.ru', None, 'false', 'false', '02.02.2004'],
            ['5%', 'ruzidov48@yahoo.com', None, 'false', 'false', '17.10.2004'],
            ['74%', 'nazar8@yahoo.com', None, 'false', 'false', '02.12.2000'],
            ['75%', 'rostislav62@yandex.ru', None, 'false', 'false', '03.08.2003']
        ],
        [
            ['0.7', '0.1', '0.1', '0.8'],
            ['nazar8', 'timofej43', 'ruzidov48', 'rostislav62'],
            ['Не выполнено', 'Не выполнено', 'Не выполнено', 'Не выполнено'],
            ['02/12/00', '02/02/04', '17/10/04', '03/08/03']
        ]
    ),
    (
        [
            ['15%', 'timofej67@mail.ru', None, 'true', 'true', '12.03.2003'],
            ['44%', 'turunak62@yahoo.com', None, 'true', 'true', '07.02.2000'],
            ['60%', 'faradov10@mail.ru', None, 'false', 'false', '23.03.2004'],
            ['44%', 'turunak62@yahoo.com', None, 'true', 'true', '07.02.2000']
        ],
        [
            ['0.1', '0.4', '0.6'],
            ['timofej67', 'turunak62', 'faradov10'],
            ['Выполнено', 'Выполнено', 'Не выполнено'],
            ['12/03/03', '07/02/00', '23/03/04']
        ]
    ),
    (
        [
            ['13%', 'svatogor33@gmail.com', None, 'false', 'false', '03.01.1999'],
            ['84%', 'ramil_13@yahoo.com', None, 'true', 'true', '19.06.2002'],
            ['84%', 'ramil_13@yahoo.com', None, 'true', 'true', '19.06.2002'],
            ['6%', 'evgenij75@gmail.com', None, 'true', 'true', '22.11.2004']
        ],
        [
            ['0.1', '0.8', '0.1'],
            ['svatogor33', 'ramil_13', 'evgenij75'],
            ['Не выполнено', 'Выполнено', 'Выполнено'],
            ['03/01/99', '19/06/02', '22/11/04']
        ]
    ),
    (
        [
            ['57%', 'nusskij78@gmail.com', None, 'false', 'false', '06.11.2004'],
            ['73%', 'racezan58@yahoo.com', None, 'false', 'false', '03.06.2000'],
            ['8%', 'sergej29@yandex.ru', None, 'true', 'true', '25.06.2004'],
            ['8%', 'sergej29@yandex.ru', None, 'true', 'true', '25.06.2004']
        ],
        [['0.6', '0.7', '0.1'],
         ['nusskij78', 'racezan58', 'sergej29'],
         ['Не выполнено', 'Не выполнено', 'Выполнено'],
         ['06/11/04', '03/06/00', '25/06/04']
         ]
    ), ([['88%', 'secak86@gmail.com', None, 'true', 'true', '06.02.2001'], ['35%', 'melofan11@yandex.ru', None, 'false', 'false', '23.02.2002'], ['88%', 'secak86@gmail.com', None, 'true', 'true', '06.02.2001'], ['88%', 'tamerlan78@mail.ru', None, 'true', 'true', '25.04.2004'], ['14%', 'mulagic6@rambler.ru', None, 'true', 'true', '12.09.1999']], [['0.9', '0.3', '0.9', '0.1'], ['secak86', 'melofan11', 'tamerlan78', 'mulagic6'], ['Выполнено', 'Не выполнено', 'Выполнено', 'Выполнено'], ['06/02/01', '23/02/02', '25/04/04', '12/09/99']]), ([['16%', 'aleksej17@yahoo.com', None, 'true', 'true', '22.11.2001'], ['29%', 'zituvev90@rambler.ru', None, 'false', 'false', '04.09.2002'], ['47%', 'zolatic7@mail.ru', None, 'true', 'true', '06.11.2004'], ['47%', 'zolatic7@mail.ru', None, 'true', 'true', '06.11.2004']], [['0.2', '0.3', '0.5'], ['aleksej17', 'zituvev90', 'zolatic7'], ['Выполнено', 'Не выполнено', 'Выполнено'], ['22/11/01', '04/09/02', '06/11/04']]), ([['62%', 'arsenij73@mail.ru', None, 'false', 'false', '07.11.2004'], ['56%', 'fomomberg97@gmail.com', None, 'true', 'true', '09.08.1999'], ['51%', 'devomanz57@yahoo.com', None, 'false', 'false', '23.08.2001'], ['15%', 'gordej84@yandex.ru', None, 'false', 'false', '23.01.2004'], ['15%', 'gordej84@yandex.ru', None, 'false', 'false', '23.01.2004']], [['0.6', '0.6', '0.5', '0.1'], ['arsenij73', 'fomomberg97', 'devomanz57', 'gordej84'], ['Не выполнено', 'Выполнено', 'Не выполнено', 'Не выполнено'], ['07/11/04', '09/08/99', '23/08/01', '23/01/04']]), ([['54%', 'vadim8@gmail.com', None, 'true', 'true', '15.02.2004'], ['93%', 'betefuk48@mail.ru', None, 'false', 'false', '21.01.1999'], ['86%', 'anatolij24@rambler.ru', None, 'true', 'true', '27.05.2002'], ['86%', 'anatolij24@rambler.ru', None, 'true', 'true', '27.05.2002'], ['72%', 'musodic24@mail.ru', None, 'false', 'false', '21.08.2003']], [['0.5', '0.9', '0.9', '0.7'], ['vadim8', 'betefuk48', 'anatolij24', 'musodic24'], ['Выполнено', 'Не выполнено', 'Выполнено', 'Не выполнено'], ['15/02/04', '21/01/99', '27/05/02', '21/08/03']])]

for t in temp:
    print(P2.f23(t[0]) == t[1])
