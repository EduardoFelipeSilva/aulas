<?php
    $cargo = $_GET["cargo"];


    switch ($cargo) {
        case 1:
            echo "O cargo selecionado foi: Escrituário";
            break;
        case 2:
            echo "O cargo selecionado foi: Secretária";
            break;
        case 3:
            echo "O cargo selecionado foi: Caixa";
            break;
        case 4:
            echo "O cargo selecionado foi: Gerente";
            break;
        case 5:
            echo "O cargo selecionado foi: Diretor";
            break;
        default:
            echo "O codigo nao cadastrado";
    }