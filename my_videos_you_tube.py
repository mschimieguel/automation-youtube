from automation_youtube import *

#escolhendo o navegador
driver = webdriver.Firefox()
driver.get("https://www.youtube.com")
delay(10)

#clicando no botão de login
item = driver.find_element_by_css_selector("ytd-masthead div#buttons ytd-button-renderer a")
item.click()
delay(5)

Usuario = input("digite o usuario google:")
senha = input("Digite a senha de sua conta google:")
login_google_account(driver,usuario,senha)

WebDriverWait(driver, 300).until(
    expect.presence_of_element_located((By.CSS_SELECTOR, "ytd-masthead button#avatar-btn"))
)
print("login ok")

#pesquisa entre videos
search = input ("Digite o curso que deseja pesquisar:\n")
videos = youtube_videos_data(driver,search)

#exportando o dataframe em planilha do excel
videos.to_excel('planilha/curso'+search+'.xlsx', engine='xlsxwriter')
