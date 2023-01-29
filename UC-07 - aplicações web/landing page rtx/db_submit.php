<?php

// Conecta ao banco de dados
$host = "localhost:3306"; // Endereço do banco de dados
$user = "root"; // Nome de usuário do banco de dados
$password = "q1w2e3"; // Senha do banco de dados
$dbname = "Formulario"; // Nome do banco de dados

$conn = mysqli_connect($host, $user, $password, $dbname);

// Verifica se a conexão foi estabelecida
if (!$conn) {
    die("Falha ao conectar: " . mysqli_connect_error());
}

// Recupera os dados do formulário
$nome = $_POST["nome"];
$email = $_POST["email"];
$whatsapp = $_POST["whatsapp"];

// Cria a consulta SQL
$sql = "INSERT INTO formu (nome, email, whatsapp) VALUES ('$nome', '$email', '$whatsapp')";

// Executa a consulta
if (mysqli_query($conn, $sql)) {
    echo "Dados salvos com sucesso.";
} else {
    echo "Erro ao salvar os dados: " . mysqli_error($conn);
}

// Fecha a conexão
mysqli_close($conn);

?>
