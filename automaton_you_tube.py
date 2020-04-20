from automation import *

def login_google_account(driver,email,password):
	#login e senha
	driver.find_element_by_id("identifierId").send_keys(email)
	driver.find_element_by_id("identifierNext").click()
	delay(5)

	password_locator = (By.CSS_SELECTOR, 'div#password input[name="password"]')
	WebDriverWait(driver, 10).until(
	    expect.presence_of_element_located(password_locator)
	)
	password_label = driver.find_element(*password_locator)
	WebDriverWait(driver, 10).until(
	    expect.element_to_be_clickable(password_locator)
	)

	#senha = input ("Digite a senha do e-mail")
	password_label.send_keys(password)
	driver.find_element_by_id("passwordNext").click()
	delay(5)

	print("wait for login ...")

def youtube_videos_data(driver,search):
	#acessando a pagina de videos studio youtube
	driver.get("https://studio.youtube.com/channel/UCnC41LUg6ehJ3Gw8qh8kLGA/videos")
	delay(15)
	driver.find_element_by_id("text-input").send_keys(search+"\n")
	delay(6)
	#clicando em date para ordernar os videos
	date = driver.find_element_by_id("date-header-name").click()
	videos_data = pd.DataFrame()

	video_title,youtube_codes,video_duration = [],[],[]

	#como python nao possui ciclo do-wihle foi necessario criar um ciclo while true com uma clausula de parada
	while True:
		delay(5)
		video_title,youtube_codes,video_duration = youtube_search_page_elements(driver,video_title,youtube_codes,video_duration)
		if not youtube_search_next_page(driver):	
			break
			
	#adicionando
	videos_data['titulo'],videos_data['codigo'],videos_data['tempo'] = video_title,youtube_codes,video_duration
	
	return videos_data

def youtube_search_next_page(driver):
	#essa funcao passa para a proxima pagina e retorna true se isso for possivel
	next_page = driver.find_element_by_id("navigate-after")

	if next_page.get_attribute("aria-disabled") == 'true':	
		#se o botão de proxima pagina estiver desativado não é possivel mudar de pagina
		return False
	else:
		next_page.click()
		return True

def youtube_search_page_elements(driver,video_title,youtube_codes,video_duration):
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	
	#as tags a possuem em seu texto o titulo do video
	a_tags = soup.find_all('a',id='video-title')

	#apartir das tags de img extrai-se o codigo(id) do video  
	img_tags = soup.find_all('img',class_='style-scope ytcp-img-with-fallback')
	
	#as tags div possuem em seu texto a duracao do video
	div_tags= soup.find_all('div',class_='label style-scope ytcp-thumbnail') 
	
	#nao se pode ter uma quantidade de titulo ,codigo e de tempos diferentes
	if len(img_tags) != len(a_tags)  or len(img_tags) != len(div_tags) or len(a_tags) != len(div_tags):
		return None
	#adequando o texto para que fique os titulos ,o codigo e o tempo de duracao fiquem bem formatados 
	for i in range(len(img_tags)):
		video_title.append(str(a_tags[i].contents)[10:-8])
		youtube_codes.append(img_tags[i]['src'].split('/')[4])
		video_duration.append(str(div_tags[i].contents).replace("'","")[15:-13])
	
	return video_title,youtube_codes,video_duration