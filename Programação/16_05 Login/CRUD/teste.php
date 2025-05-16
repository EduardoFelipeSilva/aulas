<?php 


    include_once "database.php";

    //  //////////////////////// Declarar e realizar a instrução sql

    //  /////////////////// MANEIRA 1 /////////////////////////////////

    //     $stmt = $mysqli->prepare("INSERT INTO sge_alunos( nome_aluno, email_aluno, celular_aluno) VALUES ( ?, ?, ?)");
    //     $stmt->bind_param("sss", $nome, $email, $celular); // "i" for integer, "s" for string

    //         // Verificar se cadastrou
    // // if ($stmt->execute()) {
    // //     echo "Record inserted successfully.";
    // // } else {
    // //     echo "Error: " . $stmt->error;
    // // }

        //  /////////////////// MANEIRA 2 /////////////////////////////////

        $sql_listar = "SELECT * FROM eduardo_Felipe_sge_aluno";
        $consulta_bd = mysqli_query($conexao, $sql_listar);

        if(mysqli_query($conexao,$sql_listar))
        {

        }
        else
        {
        
        }

?>