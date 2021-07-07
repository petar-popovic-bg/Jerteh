from Unitex.wrapper import Unitex

utx = Unitex('Serbian-Latin')

stats = utx.get_stats('temp1.txt')

print(stats)
