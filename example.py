import caduceus.core as c

snakes = c.build_snakes('data/snakes_by_name.csv', 'data/snake_stats.csv')

weight_s = '\nSnakes Sorted by Weight\n'
print(weight_s)
c.print_snakes_by_weight(snakes)

length_s = '\nSnakes Sorted by Length\n'
print(length_s)
c.print_snakes_by_length(snakes)
