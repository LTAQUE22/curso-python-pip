import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()


@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    
    return """
    <html>
        <head>
            <title>Aws Solution Arquitect</title>
        </head>
        <body>
            <h1>Yo Soy Inevitable</h1>
       
        <a href="https://www.sport.es/es/noticias/historico/hakuho-luchador-sumo-trofeos-anunciara-su-retirada-12118193"> 
        <h2>Sumo</h2>
        
        </a>
        
         
           </body>
    </html>
    """

def run():
    store.get_categories()

if __name__=='__main__':
    run()