<?php
    $nome = $_GET["nome"];
    $apartamento = $_GET["apartamento"];
    $diaria = $_GET["diaria"];
    $consumo = $_GET["consumo"];

    if($apartamento == "a")
    {   
        $totalDiaria = $diaria * 150;
        $subtotal = $totalDiaria + $consumo;
        $taxaServico = $subtotal*0.1;
        $total = $subtotal + $taxaServico;
        $valorUnitarioDiaria = 150;
        echo "O nome do hospede é : ". $nome . "<br><br>". " O tipo de apartamento que ele ficou foi : ". $apartamento . "<br><br>". " O número de diárias utulizadas foi : ".
        $diaria . "<br><br>". " O valor da diaria para esse tipo de apartamento é : ". $valorUnitarioDiaria . "<br><br>". " O consumo interno foi : ". $consumo . "<br><br>"." O subtotal foi : "
        . $subtotal . "<br><br>". " O valor da taxa de serviço foi : ". $taxaServico . "<br><br>". "e o total gasto foi : ". $total;

    }
    elseif($apartamento == "b")
    {
        $totalDiaria = $diaria * 100;
        $subtotal = $totalDiaria + $consumo;
        $taxaServico = $subtotal*0.1;
        $total = $subtotal + $taxaServico;
        $valorUnitarioDiaria = 100;
        echo "O nome do hospede é : ". $nome . "<br><br>". " O tipo de apartamento que ele ficou foi : ". $apartamento . "<br><br>". " O número de diárias utulizadas foi : ".
        $diaria . "<br><br>". " O valor da diaria para esse tipo de apartamento é : ". $valorUnitarioDiaria . "<br><br>". " O consumo interno foi : ". $consumo . "<br><br>"." O subtotal foi : "
        . $subtotal . "<br><br>". " O valor da taxa de serviço foi : ". $taxaServico . "<br><br>". "e o total gasto foi : ". $total;
    }
    elseif($apartamento == "c")
    {
        $totalDiaria = $diaria * 75;
        $subtotal = $totalDiaria + $consumo;
        $taxaServico = $subtotal*0.1;
        $total = $subtotal + $taxaServico;
        $valorUnitarioDiaria = 75;
        echo "O nome do hospede é : ". $nome . "<br><br>". " O tipo de apartamento que ele ficou foi : ". $apartamento . "<br><br>". " O número de diárias utulizadas foi : ".
        $diaria . "<br><br>". " O valor da diaria para esse tipo de apartamento é : ". $valorUnitarioDiaria . "<br><br>". " O consumo interno foi : ". $consumo . "<br><br>"." O subtotal foi : "
        . $subtotal . "<br><br>". " O valor da taxa de serviço foi : ". $taxaServico . "<br><br>". "e o total gasto foi : ". $total;
    }
    elseif($apartamento == "d")
    {
        $totalDiaria = $diaria * 50;
        $subtotal = $totalDiaria + $consumo;
        $taxaServico = $subtotal*0.1;
        $total = $subtotal + $taxaServico;
        $valorUnitarioDiaria = 50;
        echo "O nome do hospede é : ". $nome . "<br><br>". " O tipo de apartamento que ele ficou foi : ". $apartamento . "<br><br>". " O número de diárias utulizadas foi : ".
        $diaria . "<br><br>". " O valor da diaria para esse tipo de apartamento é : ". $valorUnitarioDiaria . "<br><br>". " O consumo interno foi : ". $consumo . "<br><br>"." O subtotal foi : "
        . $subtotal . "<br><br>". " O valor da taxa de serviço foi : ". $taxaServico . "<br><br>". "e o total gasto foi : ". $total;
    }