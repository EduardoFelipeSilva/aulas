<?php
    $idade = $_GET["idade"];

    if($idade >= 1 and $idade <= 120)
    {
        if($idade < 16)
        {
            echo "Não eleitor";
        }
        elseif($idade >= 18 and $idade <= 65)
        {
            echo "Eleitor obrigatório";
        }
        else
        {
            echo "Eleitor facultativo";
        }
    }
    else
    {
        echo "Idade inválida";
    }