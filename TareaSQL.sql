USE inemaps;

# Join separado por comas
SELECT e.codigoEstudiante, e.nombreEstudiante AS Nombre, CONCAT(p.descripcion, " | ", p.categoria) AS Contenido_Post
		FROM estudiantes e, posts p
	WHERE e.codigoEstudiante = p.codigoEstudiante;
SELECT c.descripcion AS Contenido_Comentario, e.nombreEstudiante AS Nombre_Creador, c.codigoEstudiante
		FROM comentarios c,  estudiantes e
	WHERE c.codigoEstudiante = e.codigoEstudiante;


# Cross Join
SELECT e.nombreEstudiante AS Nombre, p.fechaPublicacion AS Fecha_Publicacion_Primer_Post
	FROM estudiantes e
			CROSS JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
		WHERE p.fechaPublicacion BETWEEN "2021-03-01" AND "2021-05-01";
        
SELECT p.descripcion AS Publicacion, c.descripcion AS Comentarios_de_la_publicacion
	FROM posts p
			CROSS JOIN comentarios c ON c.idpost = p.idpost;
            
# Natural Join
SELECT e.correo 