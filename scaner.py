import shodan

# Tu clave API de Shodan
API_KEY = 'TU_API_KEY'

def scanear_con_shodan(query):
    # Inicializar el cliente de Shodan
    api = shodan.Shodan(API_KEY)
    
    try:
        # Realizar la búsqueda
        resultados = api.search(query)
        
        # Imprimir los resultados
        print(f"Se encontraron {resultados['total']} resultados para '{query}':")
        for resultado in resultados['matches']:
            print(f"Ip: {resultado['ip_str']}")
            print(f"Organización: {resultado.get('org', 'Desconocido')}")
            print(f"Sistema Operativo: {resultado.get('os', 'Desconocido')}")
            print(f"País: {resultado['country_name']}")
            print("------------------------------------")
    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Query de búsqueda
    query = input("Introduce la consulta de búsqueda: ")
    scanear_con_shodan(query)
