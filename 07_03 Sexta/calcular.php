<?php

    $num1 = $_GET["num1"];
    $num2 = $_GET["num2"];
    $operacao = $_GET["operacao"];

    // echo $num1 . "<br><br>" . $num2 . "<br><br>" . $operacao . "<br><br>";

    if($operacao == 1)
    {
        $resultado = $num1 + $num2;
        echo "A soma do valor : ". $num1. " +  ". $num2. " é = ". $resultado;
    }
    elseif($operacao == 2 )
    {
        $resultado = $num1  - $num2;
        echo "A subtração do valor : ". $num1. " - ". $num2. " é = ". $resultado;
    }
    elseif($operacao == 3)
    {
        $resultado = $num1 * $num2;
        echo "A muliplicação do valor : ". $num1. " * ". $num2. " é = ". $resultado;
    }
    elseif($operacao == 4 and $num2 != 0)
    {
        $resultado = $num1 / $num2;
        echo "A divisão do valor : ". $num1. " / ". $num2. " é = ". $resultado;
    }
    else
    {
        echo "Não dividi por 0";
    }