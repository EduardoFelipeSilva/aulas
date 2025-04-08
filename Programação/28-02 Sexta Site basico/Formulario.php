<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulário</title>
    </head>
    <body>
        <!-- Duas configurações necessarias
         1 action = ação para onde a informaçao vai
            informa a pagina que vai tratar os dados
         2 method = metodo de envio e criptografia podendo ser GET ou POST
            GET envia informações via url e tem limite de dados e menos seguro
            Ex: http://localhost/desevolvimento/Aula28-02/calcular.php?num1=&num2= os dados enviados estão na url num1 e num2

            ctrl + f5 pra reccaregar e limpar o cache da web
            
            POST envia de forma criptografada sem limite de dados
            http://localhost/desevolvimento/Aula28-02/calcular.php os dados estão escondidos-->

        <form action="calcular.php" method="post">

            <!-- Recuperar as informaçoes do input atraves do name -->
            <!-- shift + alt + baixo para copiar as linhas  -->
            <input type="number" name="num1" ><br><br>
            <input type="number" name="num2" ><br><br>
            

            <!-- value e o nome do botão -->
            <input type="submit" value="Calcular">
        
        </form>
    </body>
</html>