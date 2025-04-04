<?php 
    $nome = $_POST ["nome"];
    $email = $_POST ["email"];
    $celular = $_POST ["celular"];

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

        $sql = "INSERT INTO eduardo_Felipe_sge_aluno(nome_aluno, email_aluno, celular_aluno) VALUES ( '$nome', '$email', '$celular')";

        if(mysqli_query($conexao,$sql))
        {
            echo "Cadastro realizado com sucesso";
        }
        else
        {
            echo "Falha ao realizar cadastro";
        }

?>