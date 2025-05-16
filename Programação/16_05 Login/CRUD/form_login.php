<?php
    Include "header.php";
    session_start();
?>
<DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>

    <form action="login_user.php" method = "post">
        <label for="login_user">Login:</label>
        <input type="text" name="login_user" id="login_user" placeholder = "Informe seu login">
        
        <label for="password_user">Senha:</label>
        <input type="text" name="password_user" id="password_user" placeholder = "Digite sua senha">

        <input type = "submit" value = "Acessar">
    </form>

    <p><a href="#">Esqueceu sua senha</a></p>
    <p><a href="#">Cadastre-se</a></p>

    <?php
        if(isset($_SESSION['mensagem'])){
            echo "<div class='mensagem'>" . $_SESSION['mensagem'] . "</div>";
            unset($_SESSION['mensagem']);
        }
    ?>

</body>
</html>
