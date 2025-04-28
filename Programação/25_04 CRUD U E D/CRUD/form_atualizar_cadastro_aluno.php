<?php 
include_once "header.php"; 
include_once "database.php";
include_once "navbar.php";

$id_aluno = $_GET['id_aluno'];

$sql_listar = "SELECT * FROM eduardo_Felipe_sge_aluno
WHERE eduardo_Felipe_sge_aluno.id_aluno = '$id_aluno'";
$consulta_bd = mysqli_query($conexao, $sql_listar);
// convertendo a consulta ao banco de dados em um array associativo
$dados_db = mysqli_fetch_assoc($consulta_bd);


?>
<link rel="stylesheet" href="css/navbar.css">
<link rel="stylesheet" href="css/form_cadas_aluno.css">

</head>

<form action="atualizar_cadastro_aluno.php" method="POST">
    <p>Formulario pra atualizar cadastrar de alunos</p>

    <input type="hidden" name="id_aluno" value="<?php echo $dados_db['id_aluno']?>>
    <label for="nome">Nome:</label><br>
    <input type="text" name="nome" value="<?php echo $dados_db['nome_aluno']?>"><br><br>
    <label for="email">Email:</label><br>
    <input type="text" name="email" value="<?php echo $dados_db['email_aluno']?>"><br><br>
    <label for="celular">Celular:</label><br>
    <input type="text" name="celular" value="<?php echo $dados_db['celular_aluno']?>"><br><br>
    <input type="submit" value = "atualizar_Cadastro"> 
 
</form>
<a href="index.php"> 
    <img src="images/icons/voltar.svg" width="20px" alt="">
</a>
<?php include_once "footer.php" ?>