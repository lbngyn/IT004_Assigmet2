DROP DATABASE IF EXISTS TRUONGHOC2; 
CREATE DATABASE TRUONGHOC2;
USE TRUONGHOC2;
SET NAMES utf8;

DROP TABLE IF EXISTS TRUONG ;
CREATE TABLE TRUONG(
    MATR INT PRIMARY KEY,
	TENTR NVARCHAR(50) NOT NULL,
    DCHITR NVARCHAR(100) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE INDEX IX_TRUONG_MATR ON TRUONG (MATR);

DROP TABLE IF EXISTS HS;
CREATE TABLE HS(
    MAHS INT PRIMARY KEY,
    HO NVARCHAR(50) NOT NULL,
    TEN NVARCHAR(50) NOT NULL,
    CCCD NVARCHAR(20),
    NTNS DATE NOT NULL,
    DCHI_HS NVARCHAR(100) NOT NULL,
    CONSTRAINT UQ_HS_CCCD UNIQUE (CCCD)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE INDEX IX_HS_MAHS ON HS (MAHS);

DROP TABLE IF EXISTS HOC;
CREATE TABLE HOC(
    MATR INT,
    MAHS INT,
    NAMHOC INT,
    DIEMTB DECIMAL(3, 1) NOT NULL,
    XEPLOAI NVARCHAR(20) NOT NULL,
    KQUA NVARCHAR(20) NOT NULL,
    PRIMARY KEY (MATR, MAHS, NAMHOC),
    CONSTRAINT FK_HOC_MATR FOREIGN KEY (MATR) REFERENCES TRUONG(MATR),
    CONSTRAINT FK_HOC_MAHS FOREIGN KEY (MAHS) REFERENCES HS(MAHS)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE INDEX IX_HOC_MATR_MAHS_NAMHOC ON HOC (MATR, MAHS, NAMHOC);

CREATE INDEX IX_TRUONG_TENTR ON TRUONG (TENTR);
CREATE INDEX IX_HOC_XEPLOAI ON HOC (XEPLOAI);
CREATE INDEX IX_HOC_NAMHOC ON HOC (NAMHOC);