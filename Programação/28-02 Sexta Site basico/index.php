<!-- ctrl ponto e virgula -->
 <!-- Php tem prioridade ja que html nao precisa de interpretador de texto -->

<!DOCTYPE html>
<!-- Indica para o navegador que a versão utilizada é o html 5 -->
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <!-- Determina o sistema unicode do site (Caracteres Especiais) -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Forma inicial de responsividade -->
        <title>Pagina em PHP</title>
        <!-- Nome que aparece no navegador -->
    </head>
    <body>
        <!-- Todo conteudo do site -->
            <!-- tag h1 responsavel por titulo -->
            <h1>Pagina em php</h1>

            <!-- 
            // tag abertura e fechamento de php, nao precisa fechar se tudo for php
            <?php

            ?> -->

            <!-- Imprimir algo na tela -->
            <?php
             print "<h1>Pagina em php<h1>"
            ?>

             <!-- variaveis é um espaço reservado na memoria para armazenar algum tipo de dado durante a execução de dados
              PHP e uma linguagem de programação fracamento tipada (alocação dinamica)-->
            <?php
            //   para declarar basta $ e o nome = variavel;
                $nome = "Eduardo Felipe"; // String - (Cadeia de caracter)
                $nome = 'E'; // char - caracter
                $nome = 10; // int - Inteiro
                $nome = 10.1; // float - Real
                $nome = true; // bool - Booleano

            // para imprimir a variavel usa echo ou print
            echo $nome;
            ?>
    </body>
</html>