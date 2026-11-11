import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        html = response.content.decode("utf-8")

        pozice = html.find("<a ")
        while pozice != -1:
            konec_tagu = html.find(">", pozice)
            tag = html[pozice:konec_tagu]

            zacatek = tag.find('href="')
            if zacatek != -1:
                zacatek = zacatek + 6
                konec = tag.find('"', zacatek)
                hrefs.append(tag[zacatek:konec])

            pozice = html.find("<a ", konec_tagu)

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(hrefs)
    # osetrete potencialni chyby pomoci vetve except
    except IndexError:
        print("Chyba: nebyla zadana url, spust program takto: python sixth.py https://www.jcu.cz")
    except requests.exceptions.RequestException as e:
        print(f"Stranku se nepodarilo stahnout: {e}")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
