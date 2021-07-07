from Unitex.wrapper import Unitex

utx = Unitex('Serbian-Latin')

stats = utx.get_stats('test dir/ranka korpus helou/temp1.txt')

print(stats)
