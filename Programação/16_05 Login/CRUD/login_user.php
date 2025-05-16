<?php
    //Incluir o arquivo de conexão com o banco de dados Include "database.php";
    include "header.php";
    include_once "database.php";

    //Iniciar a sessão em PHP
    session_start();

    //Recuperar as informações via POST do formulário
    $login = $_POST['login_user'];
    $password = $_POST['password_user'];

    //Criar uma validação para verificar se os campos do formulário estão preenchides
    if(empty($login))
    {
        $_SESSION['mensagem'] = "Preencha o campo Login"; 
        header("Location: form_login.php");
    }
    elseif(empty($password))
    {
        $_SESSION['mensagem'] = "Preencha o campo Senha";
        header("Location: form_login.php");
    }
    else 
    {
        //Criar uma string com o comando en SQ1. para buscar as informações de Jogin no banco de dades $sql login "SELECT FROM login sge MHERE login sge $login" AND password sge "Spassword
        $sql_login = "SELECT * FROM login_sge WHERE login_sge = '$login' AND password_sge = '$password'";

        //Conectar ao banco de dados e executar o comando em SQL
        $resultado = mysqli_query($conexao, $sql_login);

        //Converte o resultado da consulta ao banco em um array associativo
        $dados = mysqli_fetch_array($resultado);

        //Validar o login e senha retornados da consulta ao BD
        if($dados['login_sge'] == $login and $dados['password_sge'] == $password)
        {
            //Criar u novo array com os dados de usuario
            $usuario = array("login" => $dados['login_sge'], "senha" => $dados['password_sge'], "perfil" => $dados['profile_sge']);
            //Colocar o array do usuario e sessão
            $_SESSION['usuario'] = $usuario;
            //Redirecionar para a pagina de verificação
            header("Location: painel.php");
        }
        else
        {
            //Criar uma mensagem de aviso de erro no login ou senha informados
            $_Session['mensagem'] = "Login ou Senha incorreto";
            header("Locarion: form_login.php");
        }
    }
?>