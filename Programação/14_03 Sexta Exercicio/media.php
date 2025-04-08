<?php

    $media = $_POST["media"];

    if($media >= 0 and $media <= 10)
    {
        if($media > 5)
        {
            echo "O Aluno esta aprovado";
        }
        elseif($media < 3 )
        {
            echo "O Aluno esta Reprovado";
        }
        else
        {
            echo "O Aluno precisa realizar o Exame";
        }
    }
    else
    {
        echo "Media invalida";
    }