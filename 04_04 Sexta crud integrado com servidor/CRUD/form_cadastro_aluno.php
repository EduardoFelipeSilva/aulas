<?php include_once "header.php"; ?>
<link rel="stylesheet" href="css/navbar.css">
<link rel="stylesheet" href="css/form_cadas_aluno.css">

</head>

<form action="cadastro_aluno.php" method="POST">
    <p>Formulario pra cadastrar alunos</p>
    <label for="nome">Nome:</label><br>
    <input type="text" name="nome" ><br><br>
    <label for="email">Email:</label><br>
    <input type="text" name="email" ><br><br>
    <label for="celular">Celular:</label><br>
    <input type="text" name="celular" ><br><br>
    <input type="submit" value = "Cadastrar aluno"> 
 
</form>
<a href="index.php"> 
    <img src="images/icons/voltar.svg" width="20px" alt="">
</a>
<?php include_once "footer.php" ?>