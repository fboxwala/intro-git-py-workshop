import caduceus.core as c

snakes = c.build_snakes('data/snakes_by_name.csv', 'data/snake_stats.csv')

c.print_snakes_by_weight(snakes)

print('')

birds = c.build_birds('data/birds_by_name.csv', 'data/bird_stats.csv')

c.print_birds_by_wingspan(birds)
