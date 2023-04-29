import pyperclip

import os.path

from datetime import datetime

from random import choice

from urllib.request import urlopen

class DailyQuotePlugin:

    """

    A JetBrains plugin that displays a daily quote in the IDE.

    """

    def __init__(self):

        self.quotes_url = "https://raw.githubusercontent.com/akhiltak/inspirational-quotes/master/Quotes.txt"

        self.quotes_file_path = os.path.join(os.path.expanduser("~"), ".daily_quote_quotes.txt")

        self.author_file_path = os.path.join(os.path.expanduser("~"), ".daily_quote_authors.txt")

        self.last_update_file_path = os.path.join(os.path.expanduser("~"), ".daily_quote_last_update.txt")

        self.quote = ""

        self.author = ""

        self._update_quotes()

    def _update_quotes(self):

        """

        Downloads and stores the latest quotes from the quotes URL.

        """

        try:

            with urlopen(self.quotes_url) as quotes_url:

                quotes = quotes_url.read().decode("utf-8").split("\n%\n")

                quote = choice(quotes)

                self.quote, self.author = quote.split("\n- ")

                self._save_quotes(quotes)

                self._save_author(self.author)

                self._save_last_update()

        except:

            self.quote = "Error: Could not retrieve quote."

    def _save_quotes(self, quotes):

        """

        Saves the list of quotes to a file.

        """

        with open(self.quotes_file_path, "w") as quotes_file:

            quotes_file.write("\n%\n".join(quotes))

    def _save_author(self, author):

        """

        Saves the author of the current quote to a file.

        """

        with open(self.author_file_path, "w") as author_file:

            author_file.write(author)

    def _save_last_update(self):

        """

        Saves the date and time of the last quote update to a file.

        """

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.last_update_file_path, "w") as last_update_file:

            last_update_file.write(now)

    def get_quote(self):

        """

        Returns the current quote.

        """

        return self.quote

    def get_author(self):

        """

        Returns the author of the current quote.

        """

        return self.author

    def get_last_update(self):

        """

        Returns the date and time of the last quote update.

        """

        try:

            with open(self.last_update_file_path, "r") as last_update_file:

                last_update = last_update_file.read()

                return last_update

        except:

            return "Unknown"

    def copy_quote(self):

        """

        Copies the current quote and author to the clipboard.

        """

        quote_with_author = f"{self.quote}\n- {self.author}"

        pyperclip.copy(quote_with_author)

if __name__ == '__main__':

    plugin = DailyQuotePlugin()

    print(plugin.get_quote())

