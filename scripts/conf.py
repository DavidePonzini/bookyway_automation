# URLs
LOGIN_PAGE = 'https://admin.gymtrainer.net/Account/Login'
ACCOUNTS_PAGE = 'https://admin.gymtrainer.net/Account/IndexView'

# Sleep times
SLEEP_LOGIN = 2
SLEEP_QUERY = .2
SLEEP_CREDITSAVE = .2

# Note template
NOTE_MESSAGE = '[Automation] {}'

# CSS selectors
SELECTOR_LOGIN_USERNAME = '#UserName'
SELECTOR_LOGIN_PASSWORD = '#Password'
SELECTOR_LOGIN_CONFIRM = '#login-button'
SELECTOR_ACCOUNTS_QUERYTEXT = '#search-form > input'
SELECTOR_ACCOUNTS_QUERYSUBMIT = '#search-form > button'
SELECTOR_ACCOUNTS_USERS = '#searchUser-result > ul > li'
SELECTOR_ACCOUNTS_USERS_NAME = 'p'  # to be used *after* `SELECTOR_ACCOUNTS_USERS`
SELECTOR_ACCOUNTS_USERS_EDIT = 'div.registryLiIcon.editIcon.floatright'  # to be used *after* `SELECTOR_ACCOUNTS_USERS`
SELECTOR_ACCOUNTS_NEXTPAGE = '#paginationnext'
SELECTOR_ACCOUNTS_USERS_CREDITS = '#div-credits-editor'
SELECTOR_CREDITS = '#form-credits > div > div'
SELECTOR_CREDITS_CURRENTCREDITS = 'div.creditNumber'
SELECTOR_CREDITS_NEWCREDITS = '#newCredits'
SELECTOR_CREDITS_ADD = '#radio-add'
SELECTOR_CREDITS_REMOVE = '#radio-remove'
SELECTOR_CREDITS_NOTE = '#creditsComment'
SELECTOR_CREDITS_SAVE = '#gympopup-yes'
SELECTOR_CREDITS_CANCEL = '#gympopup-no'