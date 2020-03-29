import argparse
import time

from averio_query import get_new_products

SLEEP_TIME = 30
SLEEP_TIME_BETWEEN_POSTS = 0.25


def parse_arguments():
    """
    :return: arguments
    """
    parser = argparse.ArgumentParser(
        description="Discord application for averio notifications.")
    parser.add_argument("webhook_url", type=str,
                        help="Webhook URL for notifications")
    parser.add_argument("--username", dest="username", type=str, default=None,
                        help="Discord webhook username")
    parser.add_argument("--icon", dest="icon", type=str, default=None,
                        help="Discord webhook icon picture URL"
                             " (must be HTTPS)")
    return parser.parse_args()


def main(webhook_url: str, username=None, icon=None):
    """
    Get the new products from averio website every SLEEP_TIME seconds,
    The post it trough a discord webhook.
    """
    for products in get_new_products():
        for product in products:
            product.send(webhook_url, username, icon)
            time.sleep(SLEEP_TIME_BETWEEN_POSTS)
        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    args = parse_arguments()
    main(args.webhook_url, args.username, args.icon)
