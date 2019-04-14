from loguru import logger


def main():
    logger.info("情報")
    logger.opt(raw=True).info("ここはフォーマットに従わない\n")


if __name__ == '__main__':
    main()

