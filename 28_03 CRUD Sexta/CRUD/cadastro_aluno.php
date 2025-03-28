<?php 
    $nome = $_POST ["nome"];
    $email = $_POST ["email"];
    $celular = $_POST ["celular"];

    $mysqli = new mysqli("localhost", "root", "", "sge");
                    // Verificar se conectou com o banco
            // if ($mysqli->connect_error) {
            //     die("Connection failed: " . $mysqli->connect_error);
            // }

        $stmt = $mysqli->prepare("INSERT INTO sge_alunos( nome_aluno, email_aluno, celular_aluno) VALUES ( ?, ?, ?)");
        $stmt->bind_param("sss", $nome, $email, $celular); // "i" for integer, "s" for string

            // Verificar se cadastrou
    // if ($stmt->execute()) {
    //     echo "Record inserted successfully.";
    // } else {
    //     echo "Error: " . $stmt->error;
    // }
?>