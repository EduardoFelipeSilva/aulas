<?php 

    //  /////////////////// MANEIRA 1 /////////////////////////////////

    // $mysqli = new mysqli("localhost", "root", "", "sge");
    //                 // Verificar se conectou com o banco
    //         // if ($mysqli->connect_error) {
    //         //     die("Connection failed: " . $mysqli->connect_error);
    //         // }


        //  /////////////////// MANEIRA 2 /////////////////////////////////

    // Declarar variaveis com as informaçoes do servidor
    // https://phpmyadmin.locaweb.com.br/
    // Serve do professor
    // $server = "sge_Fatec.mysql.dbaas.com.br";
    // $server_user = "sge_fatec";
    // $server_password = "Fatec25ADS!";
    // $database_name = "sge_fatec";

    //  Serve local
     $server = "localhost";
     $server_user = "root";
     $server_password = "";
     $database_name = "sge";

    // Declarar uma variavel para receber a função de conexão com o db
    $conexao = mysqli_connect($server, $server_user, $server_password, $database_name)

?>