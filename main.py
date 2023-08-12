from FakePinterest import app

if __name__ == '__main__':  # if __name__ == '__main__' -> é uma condição que verifica se o módulo Python atual é o
    # principal, ou seja, se ele está sendo executado diretamente pelo interpretador Python,
    # e não importado por outro módulo. Isso é útil para definir um ponto de entrada para
    # a aplicação, que só será executado se o módulo for o principal.
    app.run(debug=True)  # app.run(debug=True) -> é um método que inicia um servidor web local para rodar a
    # aplicação Flask.
    # O parâmetro debug=True habilita o modo de depuração, que permite ver os erros e as
    # mudanças no código em tempo real, sem precisar reiniciar o servidor.
