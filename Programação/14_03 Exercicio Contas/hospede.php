<?php
    $nome = $_GET["nome"];
    $apartamento = $_GET["apartamento"];
    $diaria = $_GET["diaria"];
    $consumo = $_GET["consumo"];

    if($apartamento == "Tipo A")
    {   
        $totalDiaria = $diaria * 150;
        $subtotal = $totalDiaria + $consumo;


    }
    elseif($apartamento == "Tipo B")
    {
        $totalDiaria = $diaria * 100;
        $subtotal = $totalDiaria + $consumo;

    }
    elseif($apartamento == "Tipo C")
    {
        $totalDiaria = $diaria * 75;
        $subtotal = $totalDiaria + $consumo;

    }
    elseif($apartamento == "Tipo D")
    {
        $totalDiaria = $diaria * 50;
        $subtotal = $totalDiaria + $consumo;
    }
    $taxaServico = $subtotal*0.1;
    $total = $subtotal + $taxaServico;
    $valorUnitarioDiaria = 150;
    echo "O nome do hospede é : ". $nome . "<br><br>". " O tipo de apartamento que ele ficou foi : ". $apartamento . "<br><br>". " O número de diárias utilizadas foi : ".
    $diaria . "<br><br>". " O valor da diária para esse tipo de apartamento é : ". $valorUnitarioDiaria . "<br><br>". " O consumo interno foi : ". $consumo . "<br><br>"." O subtotal foi : "
    . $subtotal . "<br><br>". " O valor da taxa de serviço foi : ". $taxaServico . "<br><br>". "O total gasto foi : ". $total;