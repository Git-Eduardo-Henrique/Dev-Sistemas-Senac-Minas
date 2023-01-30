<?php

if(isset($_POST['submit'])){

  include_once('db_submit.php');
  
      $nome = $_POST['nome'];
      $email = $_POST['email'];
      $telefone = $_POST['telefone'];
  
      $result = mysqli_query($conexao, "INSERT INTO formu (nome, email, whatsapp) VALUES ('$nome', '$email', '$telefone')");
  }

?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="img/nvidia_ico.ico" type="image/x-icon">
    <title>Sorteio RTX 4090 TI | Gallardo</title>

    <link rel="stylesheet" href="style.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js"></script>


</head>
<body>
    <header>
        <nav class="navbar">
            <a href="#" class="logo">NVidia</a>
            <ul class="nav-menu">

                <li class="nav-item"><a href="#form-container" class="nav-link">Sorteio</a></li>
                <li class="nav-item"><a href="#" class="nav-link">Outros Produtos</a></li>
                <li class="nav-item"><a href="#contact" class="nav-link">Contato</a></li>
        
            </ul>
            <div class="burguer">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </nav>
    </header>

    <main>
        <h1 class="title">Ganhe a RTX 4090 TI: <br>
            O poder máximo para jogar!</h1>

            <!-- Slider Carousel -->
            <div class="carousel">
                <div class="slides">
                  <div class="slide">
                    <img src="img/rtx_4090.png" alt="image1">
                  </div>
                  <div class="slide">
                    <img src="img/rtx_4090_deitada.png" alt="image2">
                  </div>
                  <div class="slide">
                    <img src="img/rtx_4090_frente.png" alt="image3">
                  </div>
                  <div class="slide">
                    <img src="img/rtx_4090_lateral.png" alt="image4">
                  </div>
                </div>
                <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                <a class="next" onclick="plusSlides(1)">&#10095;</a>
                <div class="indicator-container">
                    <div class="indicator" onclick="currentSlide(1)"></div>
                    <div class="indicator" onclick="currentSlide(2)"></div>
                    <div class="indicator" onclick="currentSlide(3)"></div>
                    <div class="indicator" onclick="currentSlide(4)"></div>
                  </div>
              </div>
              <!-- Fim do carousel -->

              <div class="line"></div>

              <h3 class="paragrafo">Jogue como nunca antes com a RTX 4090 TI, a placa de vídeo mais poderosa do mercado. Com tecnologia de última geração, esta placa oferece desempenho incrível e gráficos imersivos. E agora você tem a chance de ganhá-la! Participe do nosso sorteio e tenha a chance de transformar a sua jogabilidade. Não perca essa oportunidade única de levar seus jogos ao próximo nível. <br>
                Clique agora em “Quero Participar” para concorrer à RTX 4090 TI GALLARDO.</h3>

              <div class="bt">
                <h1><a href="#form-container">Quero Participar</a></h1>
              </div>
              
              
              <h1 class="title-2">Transforme agora seus jogos em <br> 
                obras de arte com a rtx 4090 ti gallardo
                </h1>


                

                
    </main>

    <!-- parte do Eduardo -->
    <!-- Formulário -->
    <section class="form-container" id="form-container">

        <form action="index.php" method="post">
          <h1>FORMULÁRIO PARA O SORTEIO</h1>

          <label for="name">Nome:</label>
          <input type="text" id="name" name="nome" class="input-field" required>

          <label for="email">Email:</label>
          <input type="email" id="email" name="email" class="input-field" required>

          <label for="whatsapp">WhatsApp:</label>
          <input type="text" id="whatsapp" name="telefone" class="input-field" required>
  
          <input class="green-button" type="submit" name="submit">
        </form>

    </section>
    <!-- Fim do Formulário -->

    <footer>
        <div class="contact" id="contact">
            <p>Contatos</p>
            <p>Email: nvidiasorteio@gmail.com</p>
            <p>Phone: 555-555-5555</p>
          </div>
          <div class="social-media">
            <p>Siga nossas Páginas</p>
            <a href="#" class="facebook"></a>
            <a href="#" class="twitter"></a>
            <a href="#" class="instagram"></a>
          </div>
          <p>Developed by Matheus and Eduardo</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>