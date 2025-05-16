<?php 
    $id_aluno = $_POST["id_aluno"];
    $nome = $_POST ["nome"];
    $email = $_POST ["email"];
    $celular = $_POST ["celular"];

    include_once "database.php";


        $sql_uptade = "UPDATE eduardo_felipe_sge_aluno SET nome_aluno = '$nome', email_aluno = '$email', celular_aluno = '$celular'
        WHERE eduardo_felipe_sge_aluno.id_aluno = '$id_aluno'";
        

        if(mysqli_query($conexao,$sql_uptade))
        {
            header("location:..\CRUD\listar_cadastros.php");
        }
        else
        {
            echo "Falha ao realizar atualização";
        }

?>