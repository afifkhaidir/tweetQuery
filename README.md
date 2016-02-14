# tweetQuery
Ini adalah program python untuk melakukan advance search twitter tanpa menggunakan Twitter Search API

Requirements:<br>
1. ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)<br>
2. Library selenium python (https://pypi.python.org/pypi/selenium)<br>
<br>
Langkah:<br>
1. Extract ChromeDriver<br>
2. Masukkan lokasi chromedriver.exe ke <code>browser = webdriver.Chrome()</code><br>
Contoh:<code>browser = webdriver.Chrome("C:/Users/Nurhikmah Afief/Documents/chromedriver.exe")</code><br>
3. Lakukan pencarian query melalui kotak search twitter menggunakan <code>since</code> dan <code>until</code>. Lalu copy URL nya ke<br>
<code>browser.get()</code><br>
Contoh:<code>browser.get("https://twitter.com/search?q=%23prayforriau%20since%3A2015-01-01%20until%3A2015-10-01&src=typd")</code><br>
4. Tentukan nilai variabel <code>scroll</code><br>
5. Jalankan program <code>python tweetQuery.py</code><br>
<br>
Hasil pencarian akan dimasukkan kedalam file <b>output.csv</b>
