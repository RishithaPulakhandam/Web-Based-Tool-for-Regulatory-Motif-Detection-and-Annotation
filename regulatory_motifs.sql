-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: rpulakh1
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `regulatory_motifs`
--

DROP TABLE IF EXISTS `regulatory_motifs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regulatory_motifs` (
  `motif_id` varchar(10) NOT NULL,
  `motif_name` varchar(100) DEFAULT NULL,
  `sequence_pattern` varchar(50) DEFAULT NULL,
  `motif_type` varchar(50) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`motif_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regulatory_motifs`
--

LOCK TABLES `regulatory_motifs` WRITE;
/*!40000 ALTER TABLE `regulatory_motifs` DISABLE KEYS */;
INSERT INTO `regulatory_motifs` VALUES ('MA0002.1','RUNX1','TATGTGGGAAA','Promoter','Species: Homo sapiens. Class: Runt domain factors. Family: Runt-related factors.'),('MA0003.1','TFAP2A','GCCGGGGGG','Promoter','Species: Homo sapiens. Class: Basic helix-span-helix factors (bHSH). Family: AP-2.'),('MA0003.2','TFAP2A','CACGCCCTACGGCGAC','Promoter','Species: Homo sapiens. Class: Basic helix-span-helix factors (bHSH). Family: AP-2.'),('MA0003.3','TFAP2A','CACCCCGGTCCG','Promoter','Species: Homo sapiens. Class: Basic helix-span-helix factors (bHSH). Family: AP-2.'),('MA0003.4','TFAP2A','ACGTCCCTAGCGACT','Promoter','Species: Homo sapiens. Class: Basic helix-span-helix factors (bHSH). Family: AP-2.'),('MA0007.2','AR','AGAGACAGGTTGTTT','Enhancer','Species: Homo sapiens. Class: Nuclear receptors with C4 zinc fingers. Family: Steroid hormone receptors (NR3).'),('MA0009.2','TBXT','TACCATGGTGTGTTCT','Enhancer','Species: Homo sapiens. Class: T-Box factors. Family: Brachyury-related factors.'),('MA0014.2','PAX5','GAGGACAGAGAGGAGAGAC','Promoter','Species: Homo sapiens. Class: Paired box factors. Family: Paired domain only.'),('MA0014.3','PAX5','GCGGACAGCGAG','Promoter','Species: Homo sapiens. Class: Paired box factors. Family: Paired domain only.'),('MA0014.4','PAX5','GCGTGCCT','Promoter','Species: Homo sapiens. Class: Paired box factors. Family: Paired domain only.'),('MA0017.1','NR2F1','TGACCTTAGCTTTTT','Enhancer','Species: Homo sapiens. Class: Nuclear receptors with C4 zinc fingers. Family: RXR-related receptors (NR2).'),('MA0017.2','NR2F1','ACGTGCTAGGTA','Enhancer','Species: Homo sapiens. Class: Nuclear receptors with C4 zinc fingers. Family: RXR-related receptors (NR2).'),('MA0017.3','NR2F1','ACGTAGCGTAG','Enhancer','Species: Homo sapiens. Class: Nuclear receptors with C4 zinc fingers. Family: RXR-related receptors (NR2).'),('MA0018.1','CREB1','CTGTGCGTTGCT','Enhancer','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CREB-related factors.'),('MA0018.2','CREB1','TGCCTGAT','Enhancer','Species: Mus musculus, Rattus norvegicus. Class: Basic leucine zipper factors (bZIP). Family: CREB-related factors.'),('MA0018.3','CREB1','GCGTAGCTACGC','Enhancer','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CREB-related factors.'),('MA0024.1','E2F1','TCTGAGTA','Promoter','Species: Homo sapiens. Class: Fork head/winged helix factors. Family: E2F.'),('MA0024.2','E2F1','ACGTACG','Promoter','Species: Homo sapiens. Class: Fork head/winged helix factors. Family: E2F.'),('MA0024.3','E2F1','ATCGACG','Promoter','Species: Homo sapiens. Class: Fork head/winged helix factors. Family: E2F.'),('MA0025.1','NFIL3','ATCGAT','Promoter','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.'),('MA0025.2','NFIL3','ACGTACGTAGCA','Promoter','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.'),('MA0025.3','NFIL3','ACGTGCTG','Promoter','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.'),('MA0098.4','ETS1','ACCGGAAGT','Tryptophan cluster factors','Species: Homo sapiens. Class: Tryptophan cluster factors. Family: Ets-related.'),('MA0099.2','FOS::JUN','TGACTCA','Basic leucine zipper factors (bZIP)','Species: Homo sapiens, Mus musculus, Rattus norvegicus. Class: Basic leucine zipper factors (bZIP). Family: Fos-related::Jun-related.'),('MA0102.3','CEBPA','ATTGCACAATA','Basic leucine zipper factors (bZIP)','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.'),('MA0102.4','CEBPA','TTATTAGCACAATAT','Basic leucine zipper factors (bZIP)','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.'),('MA0102.5','CEBPA','ATTGCACAAT','Basic leucine zipper factors (bZIP)','Species: Homo sapiens. Class: Basic leucine zipper factors (bZIP). Family: CEBP-related.');
/*!40000 ALTER TABLE `regulatory_motifs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-29  1:51:31
