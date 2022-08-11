<?php
    $host = "localhost"; # Dirección de servidor de la base de datos
    $user = "root"; # Usuario de la base de datos
    $password = ""; # Contraseña en la base de datos
    $dbname = "biblioteca"; # Nombre de la base de datos
    
    # Establecer conexión con la base de datos
    $mysqli = mysqli_connect($host, $user, $password, $dbname);

    /*
    if (!$mysqli) {
        echo "Error: No se pudo conectar a MySQL." . PHP_EOL;
        echo "errno de depuración: " . mysqli_connect_errno() . PHP_EOL;
        echo "error de depuración: " . mysqli_connect_error() . PHP_EOL;
        exit;
    }

    echo "Éxito: Se realizó una conexión apropiada a MySQL! La base de datos mi_bd es genial." . PHP_EOL;
    echo "Información del host: " . mysqli_get_host_info($mysqli) . PHP_EOL;
    */
?>