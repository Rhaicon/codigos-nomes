import webbrowser
import urllib.parse

produto = input("Digite o nome do produto que deseja procurar: ")

# Codifica o texto para URL (espaços, acentos etc.)
query = urllib.parse.quote(produto)

urls = {
    "AliExpress": f"https://www.aliexpress.com/wholesale?SearchText={query}",
    "Mercado Livre": f"https://lista.mercadolivre.com.br/{query}",
    "Amazon": f"https://www.amazon.com.br/s?k={query}",
    "Shopee": f"https://shopee.com.br/search?keyword={query}",
    "Magazine Luiza": f"https://www.magazineluiza.com.br/busca/{query}/"
}

for site, url in urls.items():
    webbrowser.open_new_tab(url)
