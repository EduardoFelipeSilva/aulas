<?php
    // declarar variavel
    // 2 recupearar as informaçoes do formulario

    $num1;
    $num2;
    $calculo;


    // Dentro dos [] o nome do input
    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $calculo = $num1 + $num2;


    
    echo "o primeiro numero é ". $num1 ."<br>". "o segundo numero é ". $num2 ."<br>";
    echo "a soma dos numeros é ". $calculo;