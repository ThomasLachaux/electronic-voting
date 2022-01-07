from rich.console import Console
from rich.markdown import Markdown
import shutil


def print_title(title):
  console = Console()
  console.clear()

  columns, rows = shutil.get_terminal_size()
  print('═' * columns)
  console.print(title, justify='center')
  print('═' * columns)
  print()
  print()

  # console.print(Markdown('# 🗳️  Menu principal'))