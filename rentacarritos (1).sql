-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-09-2023 a las 01:33:29
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rentacarritos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carritos`
--

CREATE TABLE `carritos` (
  `placa` varchar(6) NOT NULL,
  `tipo` int(11) NOT NULL,
  `valhora` int(11) NOT NULL,
  `valsemana` int(11) NOT NULL,
  `color` varchar(7) NOT NULL,
  `modelo` int(11) NOT NULL,
  `kilometraje` int(11) NOT NULL,
  `disponibilidad` tinyint(1) NOT NULL,
  `foto` varchar(50) NOT NULL,
  `borrado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `carritos`
--

INSERT INTO `carritos` (`placa`, `tipo`, `valhora`, `valsemana`, `color`, `modelo`, `kilometraje`, `disponibilidad`, `foto`, `borrado`) VALUES
('AFVELA', 2, 70000, 480000, '#ffffff', 2023, 0, 1, '', 0),
('D0MK', 7, 700000, 50000, '#ffffff', 2023, 0, 1, 'F20230714204438.png', 0),
('ddd222', 3, 4500, 135000, '#ffffff', 2023, 0, 1, 'F2023203654.jpeg', 0),
('dm3gd', 3, 300, 4000, '#8f3838', 2023, 0, 1, 'F20230728211711.png', 0),
('fff111', 4, 6900, 180000, '#000000', 2023, 0, 1, 'F20230728211757.png', 0),
('FYI09D', 2, 500000, 10000000, '#fb0404', 2024, 0, 0, 'F20230728213301.jpg', 0),
('HCD789', 1, 8500, 350000, '#e4111c', 2021, 0, 1, '', 0),
('ICHY22', 2, 50000, 500000, '#ffff00', 2020, 0, 1, '', 0),
('jjj334', 1, 3400, 87000, '#e61919', 2021, 0, 1, '', 1),
('JKL67G', 3, 8900, 40000, '#c9c9c9', 2025, 0, 1, 'F20230714205556.png', 0),
('KLÑM67', 7, 5000, 40000, '#555648', 2020, 0, 1, 'F20230714210205.jpg', 0),
('LANC23', 2, 5600, 70000, '#e8e8e8', 2024, 0, 1, 'F20230714205438.png', 0),
('LGT-77', 2, 4, 13, '#00ffd5', 2023, 0, 1, '', 1),
('LMF16G', 6, 200000, 2147483647, '#d1d1d1', 2026, 0, 1, 'F20230714205721.png', 0),
('MNL2F', 4, 123000, 500000, '#303030', 2024, 0, 1, 'F20230714205827.png', 0),
('NBHJ21', 9, 60000, 790000, '#000000', 2024, 0, 1, 'F20230714210332.jpeg', 0),
('NZI945', 1, 350000, 159580, '#9d7010', 1895, 0, 1, '', 1),
('QBB491', 1, 7800, 95000, '#3817de', 1999, 0, 0, '', 1),
('SDVR3F', 9, 400, 1264, '#ffffff', 2023, 0, 1, 'F20230714205346.webp', 0),
('Tch 57', 2, 2500, 85000, '#000000', 2022, 0, 1, '', 1),
('toyo21', 5, 1000, 40000, '#ffffff', 2024, 0, 1, 'F20230714205101.jpg', 0),
('TROYAN', 3500, 10000000, 2147483647, '#000000', 2025, 0, 1, '', 1),
('WBH6F', 2, 3000, 89000, '#ffffff', 2024, 0, 1, 'F20230714205243.jpg', 0),
('WGB3G', 4, 500000, 10000000, '#c7c7c7', 2024, 0, 1, 'F20230714205200.png', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `licencia` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `borrado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`licencia`, `nombre`, `telefono`, `direccion`, `borrado`) VALUES
('1010', 'Rogelio Tello', '300300300', 'Calle 34 # 5-67', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rentas`
--

CREATE TABLE `rentas` (
  `idrenta` int(11) NOT NULL,
  `placa` varchar(6) NOT NULL,
  `licencia` varchar(20) NOT NULL,
  `fecha1` datetime NOT NULL,
  `kilometraje1` int(11) NOT NULL,
  `fecha2` datetime NOT NULL,
  `kilometraje2` int(11) NOT NULL,
  `estado` varchar(10) NOT NULL,
  `observaciones` text NOT NULL,
  `borrado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rentas`
--

INSERT INTO `rentas` (`idrenta`, `placa`, `licencia`, `fecha1`, `kilometraje1`, `fecha2`, `kilometraje2`, `estado`, `observaciones`, `borrado`) VALUES
(3, 'QBB491', '1010', '2023-06-16 00:00:00', 0, '0000-00-00 00:00:00', 0, '', '', 0),
(4, 'FYI09D', '1010', '2023-06-16 00:00:00', 0, '0000-00-00 00:00:00', 0, '', '', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` varchar(10) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `contrasena` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contrasena`) VALUES
('afvelasco', 'Andres Fernando Velasco', '6a491681dac5312bc1b9b52c23b32f2c841e8c71da4bd59e474c50bc50dfbebb2b2982c4e90e289c62306722a01da4f12dd08e1e8e17a40cb3d02536f6e6f7e6');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carritos`
--
ALTER TABLE `carritos`
  ADD PRIMARY KEY (`placa`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`licencia`);

--
-- Indices de la tabla `rentas`
--
ALTER TABLE `rentas`
  ADD PRIMARY KEY (`idrenta`),
  ADD KEY `carro` (`placa`),
  ADD KEY `cliente` (`licencia`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `rentas`
--
ALTER TABLE `rentas`
  MODIFY `idrenta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `rentas`
--
ALTER TABLE `rentas`
  ADD CONSTRAINT `carro` FOREIGN KEY (`placa`) REFERENCES `carritos` (`placa`),
  ADD CONSTRAINT `cliente` FOREIGN KEY (`licencia`) REFERENCES `clientes` (`licencia`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
