-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Ноя 02 2023 г., 08:13
-- Версия сервера: 8.0.35-0ubuntu0.22.04.1
-- Версия PHP: 8.1.2-1ubuntu2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `schedule`
--

-- --------------------------------------------------------

--
-- Структура таблицы `groups`
--

CREATE TABLE `groups` (
  `id` int NOT NULL,
  `name` text COLLATE utf8mb4_general_ci NOT NULL,
  `course` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `groups`
--

INSERT INTO `groups` (`id`, `name`, `course`) VALUES
(3, '1АС1', 1),
(4, '1ИС1', 1),
(5, '1ИС2', 1),
(6, '1ОС1', 1),
(7, '1С1', 1),
(8, '2АС1', 2),
(9, '2ИС1', 2),
(10, '2ИС2', 2),
(11, '2ОС2', 2),
(12, '2С1', 2),
(13, '2Э1', 2),
(14, '3АС1', 3),
(15, '3ИС1', 3),
(16, '3ИС2', 3),
(17, '3ОС1', 3),
(18, '3С1', 3),
(19, '3Э1', 3),
(20, '4ИС1', 4),
(21, '4ОС1', 4),
(22, '4ПИ1', 4),
(23, '4С1', 4);

-- --------------------------------------------------------

--
-- Структура таблицы `group_subjects`
--

CREATE TABLE `group_subjects` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `subject_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `group_subjects`
--

INSERT INTO `group_subjects` (`id`, `group_id`, `subject_id`) VALUES
(3, 3, 3),
(4, 3, 4),
(5, 3, 5),
(6, 3, 6),
(7, 3, 7),
(8, 3, 8),
(9, 3, 9),
(10, 3, 10),
(11, 3, 11),
(12, 3, 12),
(13, 3, 13),
(14, 4, 4),
(15, 4, 3),
(16, 4, 14),
(17, 4, 6),
(18, 4, 7),
(19, 4, 8),
(20, 4, 9),
(21, 4, 10),
(22, 4, 15),
(23, 4, 16),
(24, 4, 17),
(25, 5, 3),
(26, 5, 4),
(27, 5, 14),
(28, 5, 6),
(29, 5, 7),
(30, 5, 8),
(31, 5, 9),
(32, 5, 10),
(33, 5, 15),
(34, 5, 16),
(35, 5, 17),
(36, 6, 3),
(37, 6, 4),
(38, 6, 5),
(39, 6, 6),
(40, 6, 7),
(41, 6, 8),
(42, 6, 9),
(43, 6, 10),
(44, 6, 11),
(45, 6, 12),
(46, 6, 13),
(47, 7, 3),
(48, 7, 4),
(49, 7, 5),
(50, 7, 6),
(51, 7, 7),
(52, 7, 8),
(53, 7, 9),
(54, 7, 10),
(55, 7, 18),
(56, 7, 19),
(57, 7, 17),
(58, 8, 6),
(59, 8, 20),
(60, 8, 21),
(61, 8, 11),
(62, 8, 22),
(63, 8, 23),
(64, 8, 24),
(65, 8, 25),
(66, 8, 26),
(67, 8, 27),
(68, 9, 6),
(69, 9, 28),
(70, 9, 21),
(71, 9, 29),
(72, 9, 30),
(73, 9, 31),
(74, 9, 32),
(75, 9, 33),
(76, 9, 34),
(77, 9, 35),
(78, 9, 36),
(79, 10, 6),
(80, 10, 37),
(81, 10, 38),
(82, 10, 29),
(83, 10, 30),
(84, 10, 31),
(85, 10, 32),
(86, 10, 33),
(87, 10, 34),
(88, 10, 35),
(89, 10, 36),
(90, 11, 6),
(91, 11, 20),
(92, 11, 21),
(93, 11, 11),
(94, 11, 39),
(95, 11, 22),
(96, 11, 40),
(97, 11, 41),
(98, 11, 26),
(99, 11, 27),
(100, 12, 42),
(101, 12, 6),
(102, 12, 20),
(103, 12, 21),
(104, 12, 18),
(105, 12, 22),
(106, 12, 43),
(107, 12, 44),
(108, 12, 45),
(109, 12, 26),
(110, 12, 27),
(111, 13, 42),
(112, 13, 6),
(113, 13, 28),
(114, 13, 8),
(115, 13, 46),
(116, 13, 47),
(118, 13, 48),
(120, 13, 49),
(121, 13, 50),
(122, 13, 51),
(123, 13, 52),
(124, 13, 53),
(125, 14, 20),
(126, 14, 8),
(127, 14, 54),
(128, 14, 55),
(129, 14, 56),
(130, 14, 109),
(131, 14, 57),
(132, 14, 58),
(133, 14, 59),
(134, 14, 60),
(135, 15, 28),
(136, 15, 8),
(137, 15, 61),
(138, 15, 109),
(139, 15, 62),
(140, 15, 63),
(141, 15, 64),
(142, 15, 65),
(143, 15, 66),
(144, 15, 67),
(145, 15, 68),
(146, 15, 1),
(147, 16, 28),
(148, 16, 8),
(149, 16, 61),
(151, 16, 109),
(152, 16, 62),
(153, 16, 63),
(154, 16, 64),
(155, 16, 65),
(156, 16, 66),
(157, 16, 67),
(158, 16, 68),
(159, 16, 1),
(160, 17, 20),
(161, 17, 8),
(162, 17, 69),
(163, 17, 56),
(164, 17, 109),
(165, 17, 70),
(166, 17, 71),
(167, 17, 73),
(168, 17, 72),
(169, 17, 74),
(170, 17, 75),
(171, 18, 20),
(172, 18, 8),
(173, 18, 43),
(174, 18, 76),
(175, 18, 55),
(176, 18, 56),
(177, 18, 109),
(178, 18, 77),
(179, 18, 78),
(180, 18, 79),
(181, 19, 8),
(182, 19, 80),
(183, 19, 81),
(184, 19, 56),
(185, 19, 82),
(186, 19, 83),
(187, 19, 84),
(188, 19, 85),
(189, 19, 86),
(190, 20, 28),
(191, 20, 8),
(192, 20, 87),
(193, 20, 88),
(194, 20, 53),
(195, 20, 89),
(196, 20, 90),
(197, 20, 91),
(198, 20, 92),
(199, 21, 20),
(200, 21, 8),
(201, 21, 93),
(202, 21, 48),
(203, 21, 94),
(204, 21, 95),
(205, 21, 96),
(206, 21, 73),
(207, 21, 72),
(208, 21, 97),
(209, 21, 98),
(210, 22, 110),
(211, 22, 8),
(212, 22, 54),
(213, 22, 53),
(214, 22, 99),
(216, 22, 100),
(217, 22, 101),
(218, 22, 102),
(219, 22, 103),
(220, 22, 104),
(221, 23, 20),
(222, 23, 8),
(223, 23, 54),
(224, 23, 105),
(225, 23, 106),
(226, 23, 107),
(227, 23, 79),
(228, 23, 108);

-- --------------------------------------------------------

--
-- Структура таблицы `schedules`
--

CREATE TABLE `schedules` (
  `id` int NOT NULL,
  `date` date NOT NULL,
  `visible` tinyint(1) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `schedules`
--

INSERT INTO `schedules` (`id`, `date`, `visible`) VALUES
(1, '2023-10-31', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `schedule_params`
--

CREATE TABLE `schedule_params` (
  `id` int NOT NULL,
  `schedule_id` int NOT NULL,
  `group_id` int NOT NULL,
  `subject_id` int NOT NULL,
  `number` int NOT NULL,
  `office` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `subjects`
--

CREATE TABLE `subjects` (
  `id` int NOT NULL,
  `name` text COLLATE utf8mb4_general_ci NOT NULL,
  `teacher_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `subjects`
--

INSERT INTO `subjects` (`id`, `name`, `teacher_id`) VALUES
(1, 'ТРиЗБД', 1),
(3, 'Русский язык	', 3),
(4, 'Литература', 3),
(5, 'ИнЯзык', 4),
(6, 'История', 5),
(7, 'География', 6),
(8, 'ФизКультура', 7),
(9, 'ОБЖ', 8),
(10, 'Обществознание', 9),
(11, 'Математика', 10),
(12, 'Информатика', 11),
(13, 'Физика', 12),
(14, 'ИнЯзык', 13),
(15, 'Математика', 14),
(16, 'Информатика', 15),
(17, 'Физика', 16),
(18, 'Математика', 17),
(19, 'Информатика', 18),
(20, 'ИЯПД', 4),
(21, 'ФизКультура', 8),
(22, 'ИнжГраф', 19),
(23, 'МСиС', 23),
(24, 'Ядерная физика', 22),
(25, 'Теплотехника', 35),
(26, 'Учебная практика', 19),
(27, 'Учебная практика', 20),
(28, 'ИЯПД', 2),
(29, 'ЭВМ', 14),
(30, 'ОСиС', 24),
(31, 'ААС', 24),
(32, 'ИнфТехнолог', 25),
(33, 'ОАиП', 11),
(34, 'ОПБД', 25),
(35, 'ГДиМ', 15),
(36, 'ОснТехнолог', 26),
(37, 'ИЯПД', 13),
(38, 'ФизКультура', 45),
(39, 'ИТПД', 28),
(40, 'ОЯФДИ', 27),
(41, 'ОАРВПОЦРиТМ', 12),
(42, 'ОснФилософии', 5),
(43, 'ЭиЭ', 17),
(44, 'МСиС', 29),
(45, 'ЭМиТ', 29),
(46, 'Математика', 9),
(47, 'ЭОП', 29),
(48, 'ЭконОрганиз', 32),
(49, 'НиН', 42),
(50, 'ОБУ', 31),
(51, 'ДОУ', 6),
(52, 'Статистика', 32),
(53, 'Менеджмент', 9),
(54, 'ПсихОбщения', 9),
(55, 'ОснЭкономики', 32),
(56, 'ПОПД', 4),
(57, 'ТООиВТОиСАЭ', 33),
(58, 'АЭС', 35),
(59, 'ЯУАЭС', 35),
(60, 'КиЗТОиТСАЭ', 34),
(61, 'ДМЭМЛ', 14),
(62, 'РПМ', 18),
(63, 'СистПрограм', 36),
(64, 'Учебная практика', 18),
(65, 'ТРПО', 18),
(66, 'ИСРПО', 37),
(67, 'МатМоделир', 14),
(68, 'ВиПКС', 26),
(69, 'СТП', 28),
(70, 'АЭСиТО', 39),
(71, 'ТРМЭСАФПТД', 38),
(72, 'Учебная практика', 16),
(73, 'Учебная практика', 12),
(74, 'ОВОЭБМиНМЭС', 34),
(75, 'ПМТОРМНиТОС', 12),
(76, 'ИТПД', 40),
(77, 'ИТ', 29),
(78, 'ТОСиСОиМ', 41),
(79, 'Учебная практика', 41),
(80, 'ОПД', 45),
(81, 'ИТПД', 31),
(82, 'ПОБУИФАО', 42),
(83, 'БТПиОИ', 31),
(84, 'Учебная практика', 42),
(85, 'ОРБиВФ', 43),
(86, 'ТСБО', 43),
(87, 'ССиТД', 29),
(88, 'ЧислМетоды', 14),
(89, 'ПиРП', 44),
(90, 'ПрикПрограм', 36),
(91, 'РМП', 24),
(92, 'ТРиЗБД', 25),
(93, 'Охрана труда', 29),
(94, 'ПАО', 16),
(95, 'МТП', 28),
(96, 'РОиККРМНиТОС', 12),
(97, 'ОТМССА', 16),
(98, 'ОРУНиОАО', 16),
(99, 'РВиА РАИС', 25),
(100, 'РВиА РП', 36),
(101, 'СиП М', 9),
(102, 'СиП ПОКС', 1),
(103, 'СиП СА', 24),
(104, 'СиП НИС', 26),
(105, 'ТЭСиС', 41),
(106, 'РЗСиС', 41),
(107, 'ТДиРЭ', 41),
(108, 'ОУППП', 45),
(109, 'БЖД', 8),
(110, 'ИнЯзык', 2);

-- --------------------------------------------------------

--
-- Структура таблицы `teachers`
--

CREATE TABLE `teachers` (
  `id` int NOT NULL,
  `fullname` text COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `teachers`
--

INSERT INTO `teachers` (`id`, `fullname`) VALUES
(1, 'Попов Д.А.'),
(2, 'Бушуева Е.Л.'),
(3, 'Бакирова Н.В.'),
(4, 'Потапова Н.В.'),
(5, 'Орлов П.Е.'),
(6, 'Захарова О.А.'),
(7, 'Кириевская О.Р.'),
(8, 'Жихарев А.Ю.'),
(9, 'Зеркалий Н.Г.'),
(10, 'Евдокимова С.Н.'),
(11, 'Токманцев Д.А.'),
(12, 'Устьянцев А.А.'),
(13, 'Сулейманова Э.Д.'),
(14, 'Брусницына Л.Н.'),
(15, 'Ларионов А.И.'),
(16, 'Кочуров А.Л.'),
(17, 'Олейников-Мендрух Е.Н.'),
(18, 'Уварова М.Е.'),
(19, 'Русинов-Попов Г.А.'),
(20, 'Гуральский Н.Д.'),
(22, 'Тучков А.М.'),
(23, 'Учебная практика'),
(24, 'Терещенко В.В.'),
(25, 'Бушмелева Е.А.'),
(26, 'Бушуева А.С.'),
(27, 'Антонов А.Г.'),
(28, 'Кирякова П.В.'),
(29, 'Назмутдинова В.К.'),
(31, 'Новикова О.В.'),
(32, 'Ворожцова Л.О.'),
(33, 'Сергеев М.И.'),
(34, 'Калмыкова Н.М.'),
(35, 'Бельтюков А.И.'),
(36, 'Писцова А.С.'),
(37, 'Копырин Р.Е.'),
(38, 'Мужева А.В.'),
(39, 'Аристов Н.М.'),
(40, 'Фирстова Л.В.'),
(41, 'Гребенюк А.П.'),
(42, 'Ольшанская Т.В.'),
(43, 'Грачева Е.П.'),
(44, 'Соловьева Н.С.'),
(45, 'Лихачева Е.Г.');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` text COLLATE utf8mb4_general_ci NOT NULL,
  `password` text COLLATE utf8mb4_general_ci NOT NULL,
  `session` text COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `session`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$HIyUepTFaKS3hOc7$2108e642943c957615512afacb4c8d4acf9315573e42b45537f8a886a823c706', '9dc37844-014b-4ffa-ac5b-1101eecaaddb');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `group_subjects`
--
ALTER TABLE `group_subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `groupsubjects_group_id` (`group_id`),
  ADD KEY `groupsubjects_subject_id` (`subject_id`);

--
-- Индексы таблицы `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `schedule_params`
--
ALTER TABLE `schedule_params`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scheduleparams_schedule_id` (`schedule_id`),
  ADD KEY `scheduleparams_group_id` (`group_id`),
  ADD KEY `scheduleparams_subject_id` (`subject_id`);

--
-- Индексы таблицы `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `subjects_teacher_id` (`teacher_id`);

--
-- Индексы таблицы `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT для таблицы `group_subjects`
--
ALTER TABLE `group_subjects`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;

--
-- AUTO_INCREMENT для таблицы `schedules`
--
ALTER TABLE `schedules`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `schedule_params`
--
ALTER TABLE `schedule_params`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT для таблицы `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `group_subjects`
--
ALTER TABLE `group_subjects`
  ADD CONSTRAINT `group_subjects_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `group_subjects_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `schedule_params`
--
ALTER TABLE `schedule_params`
  ADD CONSTRAINT `schedule_params_ibfk_1` FOREIGN KEY (`schedule_id`) REFERENCES `schedules` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `schedule_params_ibfk_2` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `schedule_params_ibfk_3` FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `subjects`
--
ALTER TABLE `subjects`
  ADD CONSTRAINT `subjects_ibfk_1` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
