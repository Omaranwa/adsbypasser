from mechanize import Browser, ParseString
from bs4 import BeautifulSoup


def exec_(config, summary, script):
    USERNAME = config['USERNAME']
    PASSWORD = config['PASSWORD']
    SCRIPT_ID = config['SCRIPT_ID']

    LOGIN_URL = 'https://monkeyguts.com/login/'
    EDIT_URL = 'https://monkeyguts.com/submit.php?id={0}'.format(SCRIPT_ID)

    b = Browser()

    # home page
    b.open(LOGIN_URL)
    b.select_form(name='login')
    b['username'] = USERNAME
    b['password'] = PASSWORD
    b.submit()

    # edit source
    b.open(EDIT_URL)
    # fixes parse error
    soup = BeautifulSoup(b.response().read())
    forms = soup.find_all('form')
    form = forms[1]
    t = form.find('textarea', id='code')
    t.string = ''
    forms = ParseString(form.prettify().encode('utf-8'), EDIT_URL)
    form = forms[1]
    form['descr'] = summary.encode('utf-8')
    form['code'] = script.encode('utf-8')
    form.submit()


# ex: ts=4 sts=4 sw=4 et
# sublime: tab_size 4; translate_tabs_to_spaces true; detect_indentation false; use_tab_stops true;
# kate: space-indent on; indent-width 4;
