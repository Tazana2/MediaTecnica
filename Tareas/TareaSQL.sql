USE inemaps;

# Join separado por comas
SELECT e.codigoEstudiante, e.nombreEstudiante, p.descripcion, p.categoria
		FROM estudiantes e, posts p
	WHERE e.codigoEstudiante = p.codigoEstudiante AND e.codigoEstudiante LIKE "%12%";
SELECT c.descripcion, e.nombreEstudiante, c.codigoEstudiante
		FROM comentarios c,  estudiantes e
	WHERE c.codigoEstudiante = e.codigoEstudiante AND c.codigoEstudiante > 50 AND c.codigoEstudiante < 300;


# Alias 
SELECT e.codigoEstudiante AS Id_Estudiante, e.nombreEstudiante AS Nombre_Estudiante, CONCAT(p.descripcion, " | ", p.categoria) AS Contenido_Post
		FROM estudiantes e, posts p
	WHERE e.codigoEstudiante = p.codigoEstudiante;
SELECT c.descripcion AS Contenido_Comentario, e.nombreEstudiante AS Autor, c.codigoEstudiante AS Id_estudiante
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
SELECT COUNT(e.correo), p.categoria
	FROM estudiantes e 
		CROSS JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
			GROUP BY p.categoria
				HAVING COUNT(e.correo);
            
# Natural Join
SELECT  e.codigoEstudiante AS Id, e.correo AS Correo_Estudiante, p.categoria AS Categoria_Post
	FROM estudiantes e 
			NATURAL JOIN posts p
		ORDER BY p.categoria DESC;
SELECT e.correo AS Primer_Correo_Categoria, p.categoria AS Categoria
	FROM estudiantes e
			NATURAL JOIN posts p
		GROUP BY categoria ASC;
        
# Join de Columna nombrada
SELECT e.nombreEstudiante, p.descripcion
	FROM estudiantes e
		JOIN posts p USING (codigoEstudiante)
	WHERE e.contraseña LIKE "admin%";
SELECT e.correo, c.descripcion
	FROM estudiantes e
		JOIN comentarios c USING (codigoEstudiante)
	WHERE codigoEstudiante % 6 = 0;
    
# Inner Join
SELECT p.fechaPublicacion AS FechaPublicacion_Post, c.fechaPublicacion AS FechaPublicacion_Comentario
	FROM posts p
		INNER JOIN comentarios C ON p.idpost = c.idpost
	WHERE p.idpost LIKE "%24%" ORDER BY p.categoria ASC;
SELECT e.nombreEstudiante AS Autor, p.fechaPublicacion AS FechaPublicacion_Primer_Post, c.codigoEstudiante AS Codigo_Respuesta
	FROM estudiantes e
			INNER JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
		INNER JOIN comentarios c ON p.codigoEstudiante = c.codigoEstudiante
	WHERE p.fechaPublicacion BETWEEN "2022-01-01" AND "2022-03-27";

# Outer Join (left)
SELECT CONCAT(e.nombreEstudiante, " ID: ", e.codigoEstudiante) AS Datos_Estudiantes, p.idpost
	FROM estudiantes e
		LEFT JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
	ORDER BY p.categoria DESC;
SELECT CONCAT(p.categoria, " | ", p.codigoEstudiante) AS CodigoEstudiante_Categoria, c.idComentario
	FROM posts p
		LEFT JOIN comentarios c ON p.idpost = c.idpost
	WHERE c.idComentario LIKE "_4%";
SELECT CONCAT(e.correo, " | ", e.codigoEstudiante) AS Contacto_Autor, c.fechaPublicacion AS Fecha_PublicacionComentario_SiExiste
	FROM estudiantes e
		LEFT JOIN comentarios c ON e.codigoEstudiante = c.codigoEstudiante 
	ORDER BY e.codigoEstudiante DESC;
    
# Outer Join (right)
SELECT e.contraseña, c.fechaPublicacion
	FROM estudiantes e
		RIGHT JOIN comentarios c ON e.codigoEstudiante = c.codigoEstudiante
	WHERE c.fechaPublicacion BETWEEN "2022-03-27" AND "2022-04-06";
SELECT p.idpost AS Id_Post, e.nombreEstudiante, p.fechaPublicacion
	FROM posts p
		RIGHT JOIN estudiantes e ON p.codigoEstudiante = e.codigoEstudiante
	WHERE p.idpost % 78 = 0;
    
# Unión
SELECT e.codigoEstudiante, e.nombreEstudiante
		FROM estudiantes e, posts p
	WHERE e.codigoEstudiante = p.codigoEstudiante AND e.codigoEstudiante LIKE "%16%"
UNION 
SELECT COUNT(e.contraseña), p.categoria
	FROM estudiantes e 
		CROSS JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
			GROUP BY p.categoria
				HAVING COUNT(e.contraseña);
                
SELECT e.nombreEstudiante AS Autor, p.fechaPublicacion AS FechaPublicacion_Primer_Post, c.codigoEstudiante AS Codigo_Respuesta
	FROM estudiantes e
			INNER JOIN posts p ON e.codigoEstudiante = p.codigoEstudiante
		INNER JOIN comentarios c ON p.codigoEstudiante = c.codigoEstudiante
	WHERE p.fechaPublicacion BETWEEN "2022-01-01" AND "2022-03-27"
UNION
SELECT e.contraseña, c.fechaPublicacion, c.idComentario
	FROM estudiantes e
		RIGHT JOIN comentarios c ON e.codigoEstudiante = c.codigoEstudiante
	WHERE c.fechaPublicacion BETWEEN "2022-03-27" AND "2022-04-06";