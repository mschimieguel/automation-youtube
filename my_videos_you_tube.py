from automation_you_tube import *
#este codigo tem como intuito entrar no you tube studio e pegar dados dos seus videos no you tube (url,nome) e exportar para uma planilha .xlsx

#escolhendo o navegador
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com")
delay(10)

#clicando no botão de login
item = driver.find_element(By.CSS_SELECTOR,"ytd-masthead div#buttons ytd-button-renderer a")
item.click()
delay(5)


usuario = input("digite o usuario google:")
senha = input("Digite a senha de sua conta google:")
#funcao criada para entrar em uma conta google
login_google_account(driver,usuario,senha)

WebDriverWait(driver, 300).until(
    expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead button#avatar-btn"))
)
print("login ok")

#pesquisa entre os seus videos no you tube studio dado um termo de pesquisa
search = input ("Digite o curso que deseja pesquisar:\n")
videos = youtube_videos_data(driver,search)

#exportando o dataframe em planilha do excel
videos.to_excel('planilha/curso'+search+'.xlsx', engine='xlsxwriter')
