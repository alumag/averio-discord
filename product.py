from DiscordHooks import Hook, Embed, EmbedField


class EmbedFieldInline(EmbedField):
    """Inline version for EmbedField"""
    __items__ = ('name', 'value', 'inline')

    @property
    def inline(self) -> bool:
        return True


class Product(object):
    """
    Represent a Product from averio website
    """

    def __init__(self, product: str, link: str, old_price: float,
                 new_price: float, percent: float):
        self.product = product
        self.link = link
        self.old_price = str(old_price)
        self.new_price = str(new_price)
        self.percent = str(percent)

    @property
    def embed(self):
        """
        Serialize the product into single message
        :return: Embed
        """
        return Embed(
            title=self.product,
            description="",
            url=self.link,
            fields=self.fields
        )

    @property
    def fields(self):
        """
        Embed Fields of NewPrice, OldPrice and Percent
        :return: list of EmbedFieldInline
        """
        return [
            EmbedFieldInline(name="NewPrice", value=self.new_price),
            EmbedFieldInline(name="OldPrice", value=self.old_price),
            EmbedFieldInline(name="Percent", value=f"{self.percent}%")
        ]

    @property
    def embeds(self):
        """
        List of embedded content.
        :return: Single item list.
        """
        return [self.embed]

    def send(self, webhook_url: str, username: str=None, icon: str=None):
        """
        Send the webhook,
        Use default username and icon
        """
        hook = Hook(hook_url=webhook_url, embeds=self.embeds)
        if username is not None:
            hook.username = username
        if icon is not None:
            hook.avatar_url = icon
        hook.execute()

    def __eq__(self, other):
        """Check two Products name equality"""
        if not isinstance(other, Product):
            return False
        return self.product == other.product

    def __hash__(self):
        return hash(self.product)
