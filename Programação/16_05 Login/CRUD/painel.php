<?php
    //incluir o header com as informaçoes da pagina em HTML
    include "header.php";
    //Iniciar a sessão em PHP
    session_start();
    //Captar o array colocado na sessão e armazenar na variavel
    $usuario = $_SESSION['usuario'];
    //Verificar o perfil de acesso
    if($usuario['perfil'] != "admin") { ?>
    <!-- Inicio do perfil de cliente -->
     <h2>SGE - Sistema de Gerenciamento Escolar</h2>
     <p>Painel de gerenciamento do sistema</p>
     <P>Você tem permissão de acesso do tipo:
        <?php echo $usuario['perfil'];?></P>
    <h3>Seja bem-vindo: <?php echo $usuario['login'];?></h3>
    <!-- Fim do perfil do Cliente -->
<?php }
else { ?>
    <!-- Inicio do perfil de Administrador -->
    <h2>SGE - Sistema de Gerenciamento Escolar</h2>
     <p>Painel de gerenciamento do sistema</p>
     <P>Você tem permissão de acesso do tipo:
     <?php echo $usuario['perfil'];?></P>
    <h3>Seja bem-vindo: <?php echo $usuario['login'];?></h3>
    <?php } ?>
    <!-- Fim do perfil do Cliente -->
<?php include "footer.php" ?>