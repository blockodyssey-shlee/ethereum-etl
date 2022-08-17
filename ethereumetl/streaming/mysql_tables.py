#  MIT License
#
#  Copyright (c) 2020 Evgeny Medvedev, evge.medvedev@gmail.com
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from sqlalchemy import Table, Column, BigInteger, String, Numeric, \
    MetaData, TIMESTAMP

metadata = MetaData()

# SQL schema is here https://github.com/blockchain-etl/ethereum-etl-postgres/tree/master/schema

BLOCKS = Table(
    'BLOCKS', metadata,
    Column('BLOCK_TIMESTAMP', BigInteger),
    Column('BLOCK_LOCALTIME', TIMESTAMP),
    Column('BLOCK_NUMBER', BigInteger),
    Column('BLOCK_HASH', String, primary_key=True),
    Column('PARENT_HASH', String),
    Column('NONCE', String),
    Column('SHA3_UNCLES', String),
    Column('LOGS_BLOOM', String),
    Column('TRANSACTIONS_ROOT', String),
    Column('STATE_ROOT', String),
    Column('RECEIPTS_ROOT', String),
    Column('MINER', String),
    Column('DIFFICULTY', Numeric(38)),
    Column('TOTAL_DIFFICULTY', Numeric(38)),
    Column('SIZE', BigInteger),
    Column('EXTRA_DATA', String),
    Column('GAS_LIMIT', BigInteger),
    Column('GAS_USED', BigInteger),
    Column('TRANSACTION_COUNT', BigInteger),
    Column('BASE_FEE_PER_GAS', BigInteger),
)

TRANSACTIONS = Table(
    'TRANSACTIONS', metadata,
    Column('TRANSACTION_HASH', String, primary_key=True),
    Column('NONCE', BigInteger),
    Column('TRANSACTION_INDEX', BigInteger),
    Column('FROM_ADDRESS', String),
    Column('TO_ADDRESS', String),
    Column('VALUE', Numeric(38)),
    Column('GAS', BigInteger),
    Column('GAS_PRICE', BigInteger),
    Column('INPUT', String),
    Column('RECEIPT_CUMULATIVE_GAS_USED', BigInteger),
    Column('RECEIPT_GAS_USED', BigInteger),
    Column('RECEIPT_CONTRACT_ADDRESS', String),
    Column('RECEIPT_ROOT', String),
    Column('RECEIPT_STATUS', BigInteger),
    Column('BLOCK_TIMESTAMP', TIMESTAMP),
    Column('BLOCK_NUMBER', BigInteger),
    Column('BLOCK_HASH', String),
    Column('MAX_FEE_PER_GAS', BigInteger),
    Column('MAX_PRIORITY_FEE_PER_GAS', BigInteger),
    Column('TRANSACTION_TYPE', String),
    Column('RECEIPT_EFFECTIVE_GAS_PRICE', BigInteger),
)

LOGS = Table(
    'LOGS', metadata,
    Column('LOG_INDEX', BigInteger, primary_key=True),
    Column('TRANSACTION_HASH', String, primary_key=True),
    Column('TRANSACTION_INDEX', BigInteger),
    Column('ADDRESS', String),
    Column('DATA', String),
    Column('TOPIC0', String),
    Column('TOPIC1', String),
    Column('TOPIC2', String),
    Column('TOPIC3', String),
    Column('BLOCK_TIMESTAMP', TIMESTAMP),
    Column('BLOCK_NUMBER', BigInteger),
    Column('BLOCK_HASH', String),
)

TOKEN_TRANSFERS = Table(
    'TOKEN_TRANSFERS', metadata,
    Column('TOKEN_ADDRESS', String),
    Column('FROM_ADDRESS', String),
    Column('TO_ADDRESS', String),
    Column('VALUE', Numeric(38)),
    Column('TRANSACTION_HASH', String, primary_key=True),
    Column('LOG_INDEX', BigInteger, primary_key=True),
    Column('BLOCK_TIMESTAMP', TIMESTAMP),
    Column('BLOCK_NUMBER', BigInteger),
    Column('BLOCK_HASH', String),
)

# python3 ethereumetl.py stream --provider-uri http://EN:8551 --period-seconds 1 --lag 10 --output=mysql+mysqldb://root:1111@DB_HOST:3306/DATABASE

# TABLE SCHEMA
# CREATE TABLE BLOCKS (
#     `BLOCK_TIMESTAMP` NUMERIC(38,0) NOT NULL,
#     `BLOCK_LOCALTIME` TIMESTAMP NOT NULL,
#     `BLOCK_NUMBER` INT(8) NOT NULL,
#     `BLOCK_HASH` VARCHAR(66) NOT NULL,
#     `PARENT_HASH` VARCHAR(66),
#     `NONCE` VARCHAR(42),
#     `SHA3_UNCLES` VARCHAR(66),
#     `LOGS_BLOOM` TEXT,
#     `TRANSACTIONS_ROOT` VARCHAR(66),
#     `STATE_ROOT` VARCHAR(66),
#     `RECEIPTS_ROOT` VARCHAR(66),
#     `MINER` VARCHAR(42),
#     `DIFFICULTY` NUMERIC(38,0),
#     `TOTAL_DIFFICULTY` NUMERIC(38,0),
#     `SIZE` INT(8),
#     `EXTRA_DATA` TEXT,
#     `GAS_LIMIT` INT(8),
#     `GAS_USED` INT(8),
#     `TRANSACTION_COUNT` INT(8),
#     `BASE_FEE_PER_GAS` INT(8),
#     PRIMARY KEY (`BLOCK_HASH`),
#     INDEX (`BLOCK_TIMESTAMP` DESC),
#     UNIQUE INDEX (`BLOCK_NUMBER` DESC)
# );

# CREATE TABLE TRANSACTIONS (
#     `TRANSACTION_HASH` VARCHAR(66) NOT NULL,
#     `NONCE` INT(8) NOT NULL,
#     `TRANSACTION_INDEX` INT(8) NOT NULL,
#     `FROM_ADDRESS` VARCHAR(42) NOT NULL,
#     `TO_ADDRESS` VARCHAR(42),
#     `VALUE` NUMERIC(38,0),
#     `GAS` INT(8),
#     `GAS_PRICE` INT(8),
#     `INPUT` TEXT,
#     `RECEIPT_CUMULATIVE_GAS_USED` INT(8),
#     `RECEIPT_GAS_USED` INT(8),
#     `RECEIPT_CONTRACT_ADDRESS` VARCHAR(42),
#     `RECEIPT_ROOT` VARCHAR(66),
#     `RECEIPT_STATUS` INT(8),
#     `BLOCK_TIMESTAMP` TIMESTAMP NOT NULL,
#     `BLOCK_NUMBER` INT(8) NOT NULL,
#     `BLOCK_HASH` VARCHAR(66) NOT NULL,
#     `MAX_FEE_PER_GAS` INT(8),
#     `MAX_PRIORITY_FEE_PER_GAS` INT(8),
#     `TRANSACTION_TYPE` VARCHAR(42),
#     `RECEIPT_EFFECTIVE_GAS_PRICE` INT(8),
#     PRIMARY KEY (`TRANSACTION_HASH`),
#     INDEX (`BLOCK_TIMESTAMP` DESC),
#     INDEX (`FROM_ADDRESS`, `BLOCK_TIMESTAMP` DESC),
#     INDEX (`TO_ADDRESS`, `BLOCK_TIMESTAMP` DESC)
# );

# CREATE TABLE LOGS (
#     `LOG_INDEX` INT(8) NOT NULL,
#     `TRANSACTION_HASH` VARCHAR(66) NOT NULL,
#     `TRANSACTION_INDEX` INT(8) NOT NULL,
#     `ADDRESS` VARCHAR(42),
#     `DATA` TEXT,
#     `TOPIC0` VARCHAR(66),
#     `TOPIC1` VARCHAR(66),
#     `TOPIC2` VARCHAR(66),
#     `TOPIC3` VARCHAR(66),
#     `BLOCK_TIMESTAMP` TIMESTAMP NOT NULL,
#     `BLOCK_NUMBER` INT(8) NOT NULL,
#     `BLOCK_HASH` VARCHAR(66) NOT NULL,
#     PRIMARY KEY (`TRANSACTION_HASH`,`LOG_INDEX`),
#     INDEX (`BLOCK_TIMESTAMP` DESC),
#     INDEX (`ADDRESS`, `BLOCK_TIMESTAMP` DESC)
# );

# CREATE TABLE TOKEN_TRANSFERS (
#     `TOKEN_ADDRESS` VARCHAR(42) NOT NULL,
#     `FROM_ADDRESS` VARCHAR(42),
#     `TO_ADDRESS` VARCHAR(42),
#     `VALUE` NUMERIC(38,0),
#     `TRANSACTION_HASH` VARCHAR(66) NOT NULL,
#     `LOG_INDEX` INT(8) NOT NULL,
#     `BLOCK_TIMESTAMP` TIMESTAMP NOT NULL,
#     `BLOCK_NUMBER` INT(8) NOT NULL,
#     `BLOCK_HASH` VARCHAR(66) NOT NULL,
#     PRIMARY KEY (`TRANSACTION_HASH`,`LOG_INDEX`),
#     INDEX (`BLOCK_TIMESTAMP` DESC),
#     INDEX (`TOKEN_ADDRESS`, `BLOCK_TIMESTAMP` DESC),
#     INDEX (`FROM_ADDRESS`, `BLOCK_TIMESTAMP` DESC),
#     INDEX (`TO_ADDRESS`, `BLOCK_TIMESTAMP` DESC)
# );